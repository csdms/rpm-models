#! /usr/bin/python
#
# Builds binary and source RPMs for a model in the CSDMS repository.
#
# Arguments:
#   -m is the model name (required)
#   -t is the tagged model version (optional)
#   -h shows the help message
#
# Usage:
#   $ python build_model_rpm.py --help
#   $ python build_model_rpm.py --model hydrotrend -tag 3.0.2
#
# Mark Piper (mark.piper@colorado.edu)

import sys, os, shutil
import argparse
from subprocess import call
import string
import glob
import shlex

class BuildModelRPM:
    '''
    Calls the distro-specific tool to build an RPM for a model from
    its source code.
    '''
    def __init__(self, model_name, model_version):
        self.topdir = os.path.dirname(os.path.realpath(__file__)) + os.sep

        if model_name == None:
            print("A model must be specified with the '-m' flag.")
            sys.exit(2) # no model

        if not os.path.isdir(self.topdir + model_name):
            print("The model '" + model_name + "' cannot be located.")
            sys.exit(3) # can't find model

        self.model = model_name            
        self.version = "head" if model_version == None else model_version

        # Set up the rpmbuild directory.
        self.rpmbuild = os.getenv("HOME") + os.sep + "rpmbuild" + os.sep
        self.prep_directory()

        # Download the model's source code.
        self.get_source()

        # Make a tarball from the model's source.
        self.make_tarball()

        # Apply patches, if any.
        self.patch()

        # Build the binary and source RPMs.
        self.build()
        print("Success!")

    def prep_directory(self):
        '''
        Prepares the RPM build directory with built-in RPM dev tools.
        Sets up member variables for paths in the build directory.
        '''
        print("Setting up rpmbuild directory structure.")
        if os.path.isdir(self.rpmbuild):
            call(["rpmdev-wipetree"])
        else:
            call(["rpmdev-setuptree"])
        self.sources = self.rpmbuild + "SOURCES" + os.sep
        self.specs = self.rpmbuild + "SPECS" + os.sep

    def get_source(self):
        '''
        Retrieves the model source from an external repository.
        '''
        print("Getting " + self.model + " source.")
        self.source_target = self.sources + self.model + "-" + self.version
        with open(self.topdir + self.model + os.sep + "source.txt", "r") as f:
            cmd = f.readline().strip()
        cmd += " " + self.source_target
        ret = call(cmd, shell=True)
        if ret != 0:
            print("Unable to download model source.")
            sys.exit(4) # can't access source

    def make_tarball(self):
        '''
        Makes a tarball (required by rpmbuild) from the model's source.
        '''
        print("Making tarball.")
        shutil.make_archive(self.source_target, 'gztar', self.sources, \
                            os.path.basename(self.source_target))
        shutil.rmtree(self.source_target)

    def patch(self):
        '''
        Locates and includes patches (if any) for the build process. 
        Patches must use the extension ".patch".
        '''
        print("Applying patches.")
        for patch in glob.glob(self.topdir + self.model + os.sep + "*.patch"):
            shutil.copy(patch, self.sources)

    def build(self):
        '''
        Build binary and source RPMS.
        '''
        print("Building RPMs.")
        spec_file = self.model + ".spec"
        shutil.copy(self.topdir + self.model + os.sep + spec_file, self.specs)
        cmd = "rpmbuild -ba --quiet " + self.specs + spec_file \
            + " --define '_version " + self.version + "'"
        ret = call(shlex.split(cmd))
        if ret != 0:
            print("Error in building model RPM.")
            sys.exit(5) # can't build RPM

#-----------------------------------------------------------------------------

def main():
    '''
    Accepts command-line arguments and passes them to an instance of
    BuildModelRPM.
    '''
    # Allow only Linuxen.
    if not sys.platform.startswith('linux'):
        print("Error: this OS is not supported.")
        sys.exit(1) # not Linux

    # Which model is being built?
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model",
                        help="the name of the model to build")
    parser.add_argument("-t", "--tag",
                        help="the tagged version of the model")
    args = parser.parse_args()

    BuildModelRPM(args.model, args.tag)

if __name__ == "__main__":
    main()
