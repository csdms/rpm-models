#! /bin/bash
#
# Builds binary and source RPMs for a model in the CSDMS repository.
#
# Arguments:
#   -m is the model name (required)
#   -t is the tagged model version (optional)
#   -h shows the help message
#
# Usage:
#   $ bash build_model_rpm.sh -m hydrotrend -t 3.0.2
#   $ bash build_model_rpm.sh -h
#
# Mark Piper (mark.piper@colorado.edu)

# Store the directory from which this script is called. This will be
# used to reference relative directories.
# See: http://stackoverflow.com/a/246128
topdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Help text.
help="Usage: bash build_model_rpm [-m <model name>] [-t <model tag>]"

# Get arguments, parse into variables.
while getopts ":m:t:h" opt; do
    case $opt in
	m)
	    model=$OPTARG
	    echo "Model selected: $model"
	    ;;
	t)
	    tag=$OPTARG
	    echo "Tag selected: $tag"
	    ;;
	h)
	    echo -e $help
	    exit 0
	    ;;
	\?) # Catches flag != -m, -t, or -h.
	    echo "Invalid option: -$OPTARG" >&2
	    echo -e $help
	    exit 2 # invalid option
	    ;;
	:) # Catches no args for -m and -t.
	    echo "Option -$OPTARG requires an argument." >&2
	    echo -e $help
	    exit 3 # no arg for -m or -t
	    ;;
    esac
done
shift $((OPTIND - 1))

# Model is required. Exit if a model isn't specified.
if [ -z $model ]; then
   echo "A model must be specified with the '-m' flag."
   echo -e $help
   exit 4 # model not specified
fi

# If the model requested isn't present, issue a message and exit.
if [ ! -d $topdir/$model ]; then
   echo "The model $model cannot be found."
   exit 5 # model not present
fi

# Issue a message if tag is empty. Assign a default to tag.
if [ -z $tag ]; then
   tag="head"
   echo "No tag selected, assuming '$tag'"
fi

# Set up standard rpmbuild directories in $HOME (or wipe them, if 
# already present).
echo "Setting up rpmbuild directory structure"
test -d $HOME/rpmbuild && rpmdev-wipetree || rpmdev-setuptree

# Get the (exported) model source from CSDMS.
echo "Getting $model source"
$topdir/$model/get_source.sh

# Change to rpmbuild/SOURCES. Make a tarball from the source.
echo "Making $model tarball"
cd $HOME/rpmbuild/SOURCES
mv trunk $model-$tag
tar -zcf $model-$tag.tar.gz $model-$tag
rm -rf $model-$tag

# Place the patch(es) (if any) for the model in rpmbuild/SOURCES.
echo "Applying patches"
$topdir/$model/apply_patches.sh

# Change to the rpmbuild directory. Place the model spec file in 
# rpmbuild/SPECS. Build source and binary packages.
echo "Building RPM"
cd $HOME/rpmbuild
cp $topdir/$model/$model.spec SPECS
rpmbuild -ba SPECS/$model.spec

# Success!
### TODO Include an explanatory message
exit 0
