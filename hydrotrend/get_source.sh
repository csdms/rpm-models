#!/bin/bash
# Gets the source code for a model.
# Mark Piper (mark.piper@colorado.edu)

target_dir=$HOME/rpmbuild/SOURCES
svn export --quiet https://csdms.colorado.edu/svn/$model/trunk $target_dir
exit 0
