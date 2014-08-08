#!/bin/bash
# Gets the source code for a model.
# Mark Piper (mark.piper@colorado.edu)

target=$HOME/rpmbuild/SOURCES
svn export --quiet \
    https://csdms.colorado.edu/svn/hydrotrend/trunk $target/trunk
test -d $target/trunk
exit $?
