# Note

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
