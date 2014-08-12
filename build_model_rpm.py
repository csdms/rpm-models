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

import sys, os
import argparse
from subprocess import call

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
        #print(self.model, self.version)

        # Set up the rpmbuild directory.
        self.rpmbuild = os.path.expanduser("~") + os.sep + "rpmbuild" + os.sep
        #print(self.rpmbuild)
        self.prep_directory()

        # Download the model's source code.
        self.sources_dir = self.rpmbuild + "SOURCES" + os.sep
        self.source = self.sources_dir + "source.txt"
        self.get_source()

        # Make a tarball from the model's source.
        self.make_tarball()

        # Apply patches, if any.
        self.patch()

        # Build the binary and source RPMs.
        self.build()

    def prep_directory(self):
        '''
        Prepares the RPM build directory using built-in RPM dev tools.
        '''
        print("Setting up rpmbuild directory structure.")
        if os.path.isdir(self.rpmbuild):
            call(["rpmdev-wipetree"])
        else:
            call(["rpmdev-setuptree"])

    def get_source(self):
        '''
        Retrieves the model source from an external repository.
        '''
        print("Getting " + self.model + " source.")

    def make_tarball(self):
        '''
        Makes a tarball (required by rpmbuild) from the model's source.
        '''
        print("Making tarball.")

    def patch(self):
        '''
        Includes patches for the build process.
        '''
        print("Applying patches.")

    def build(self):
        '''
        Build binary and source RPMS.
        '''
        print("Building RPMs.")


#-----------------------------------------------------------------------------

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
