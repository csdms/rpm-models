#! /usr/bin/env python
#
# Makes binary and source RPMs for all the CSDMS models in this repository.
#
# Example:
#   $ python build_all.py /path/to/rpm_models
#
# Mark Piper (mark.piper@colorado.edu)

import sys, os, shutil
from subprocess import check_call

def build_all(models_dir, prefix):
    '''
    Makes binary and source RPMs for each of the CSDMS models in the
    `rpm_models` repository. The RPMs are copied to "~/tmp".
    '''
    rpm_models_dir = os.path.expanduser(models_dir)
    install_prefix = "/usr/local" if prefix == None \
        else os.path.expandvars(prefix)
    rpmbuild_dir = os.path.join(os.path.expanduser("~"), "rpmbuild")
    rpm_dir = os.path.join(rpmbuild_dir, "RPMS", "x86_64")
    srpm_dir = os.path.join(rpmbuild_dir, "SRPMS")
    tmp_dir = os.path.join(os.path.expanduser("~"), "tmp")

    # Get a list of all the models in the repository. (Using the directory
    # name, which is fragile.)
    models = [ f for f in os.listdir(rpm_models_dir) if os.path.isdir(f) \
                   and not f.startswith(".") ]

    # Loop over the list of models, calling `build_rpm` on each, and copying
    # the resulting RPMs to a temporary directory.
    for m in models:
        try:
            check_call(["build_rpm", m, "--prefix", install_prefix, \
                            "--local", rpm_models_dir])
            rpms = []
            rpms.extend(os.listdir(rpm_dir))
            for r in rpms:
                shutil.copy(os.path.join(rpm_dir, r), tmp_dir)
            srpms = []
            srpms.extend(os.listdir(srpm_dir))
            for s in srpms:
                shutil.copy(os.path.join(srpm_dir, s), tmp_dir)
        except:
            print("Error in building RPMs for '" + m + "'")
            sys.exit(1)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("rpm_models_dir",
                        help="the path to the `rpm_models` directory")
    parser.add_argument("--prefix",
                        help="use PREFIX as install path for RPM [/usr/local]")
    args = parser.parse_args()

    build_all(args.rpm_models_dir, prefix=args.prefix)
