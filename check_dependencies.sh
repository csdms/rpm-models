#! /bin/bash 
#
# Checks that the packages required to build an RPM are present on the
# system.
#
# Usage:
#   $ bash check_dependencies.sh
#
# Mark Piper (mark.piper@colorado.edu)

required_msg() {
    echo "The package '$package' is required. Install it with:"
    echo $install_msg $package
}

debian=false
if [ -f /etc/debian_version ]; then
    debian=true
fi

# Build the list of dependencies.
required="subversion cmake gcc"
if $debian; then
    echo "Checking Debian-compatible dependencies:"
    required="$required g++"
    install_msg="$ sudo apt-get install"
    for package in $required; do
	if ! dpkg-query -W $package; then
	    required_msg
	    exit 1 # package not present
	fi
    done
else
    echo "Checking RHEL-compatible dependencies:"
    required="$required rpm-build rpmdevtools rpmlint gcc-c++"
    install_msg="$ sudo yum install"
    for package in $required; do
	echo " - $package"
	if ! rpm -q --quiet $package; then
	    required_msg
	    exit 1 # package not present
	fi
    done
fi

echo "All required pacakges are installed."
exit 0
