# Note

The file **dependencies.txt** lists the packages needed to build an RPM
on a RHEL-based Linux distribution (e.g., CentOS).
The file **dependencies_debian.txt** lists packages required for
Debian-based distributions (e.g., Ubuntu).

The file **macros.cmake**,
containing the definition of the `%cmake` macro for `rpmbuild`,
is provided here because
it's not included in the CMake package
on the Ubuntu 12.04 LTS virtual machine
used by Travis CI.
This file is not needed
for RHEL and CentOS
because the `%cmake` macro is included in the CMake package
used on these distros.
