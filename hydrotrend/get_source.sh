#!/bin/bash
# Gets the source code for a model.
# Mark Piper (mark.piper@colorado.edu)

target_dir=$HOME/rpmbuild/SOURCES
svn export --quiet https://csdms.colorado.edu/svn/hydrotrend/trunk $target_dir
test -d $target_dir/trunk
exit $?
