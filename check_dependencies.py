#! /usr/bin/python
#
# Checks that the packages required to build an RPM for a given model
# are present on the system.
#
# Usage:
#   $ python check_dependencies.sh --help
#   $ python check_dependencies.sh -m "hydrotrend"
#
# Mark Piper (mark.piper@colorado.edu)

import sys
import os.path
from subprocess import call
import argparse

class CheckDependencies:
    '''
    Checks dependencies for building an RPM for a given model.
    '''
    def __init__(self, model_name):
        self.model_name = model_name
        self.debian_check()

        # Read dependencies for all models.
        if self.is_debian:
            self.dependencies_file = "config/dependencies_debian.txt"
            self.distro = "Debian"
            self.package_tool = "apt-get"
        else:
            self.dependencies_file = "config/dependencies.txt"
            self.distro = "RHEL"
            self.package_tool = "yum"
        self.dependencies = self.read(self.dependencies_file)

        # Read additional dependencies for the requested model.
        if self.model_name != None:
            self.model_dependencies_file = self.model_name + "/dependencies.txt"
            if os.path.isfile(self.model_dependencies_file):
                subdependencies = self.read(self.model_dependencies_file)
                self.dependencies.extend(subdependencies)

        # Check that the dependencies are met.
        self.check()
        print("All required packages are installed.")

    def debian_check(self):
        ''' 
        True if this is a Debian-based Linux system.
        '''
        self.is_debian = (call(["test", "-f", "/etc/debian_version"]) == 0)

    def read(self, fname):
        '''
        Reads a list of package names, as strings, from a file.
        '''
        with open(fname, "r") as f:
            deps = f.read().split("\n")
        deps.pop(0) # remove first and
        deps.pop()  # last items from list
        return deps

    def check_with_package_tool(self, package):
        '''
        Calls the distro-specific package tool to check whether the given
        package is installed.
        '''
        if self.is_debian:
            return call(["dpkg-query", "-W", package])
        else:
            return call(["rpm", "-q", "--quiet", package])

    def check(self):
        '''
        Checks for required packages.
        '''
        print("Checking " + self.distro + "-compatible dependencies:")
        for package in self.dependencies:
            print(" - " + package)
            ret = self.check_with_package_tool(package)
            if ret > 0:
                print("The package '" + package + "' is required. "
                      "Install it with:\n$ sudo " + self.package_tool
                      + " install " + package)
                sys.exit(1) # package not installed

#-----------------------------------------------------------------------------

# Allow only Linuxen.
if not sys.platform.startswith('linux'):
    print("Error: this OS is not supported.")
    sys.exit(1) # not Linux

# Which model is being checked?
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model",
                    help="the name of the model to check")
args = parser.parse_args()

CheckDependencies(args.model)
