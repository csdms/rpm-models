#!/bin/bash
# Applies a patch (or patches) to a model in the RPM build process.
# Mark Piper (mark.piper@colorado.edu)

source_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
target_dir=$HOME/rpmbuild/SOURCES
cp $source_dir/hydrotrend-head-cmakelist.patch $target_dir
exit 0
