[![Build Status](https://travis-ci.org/csdms/rpm_models.svg?branch=master)](https://travis-ci.org/csdms/rpm_models)

rpm_models
==========

Recipes for building binary and source RPMs for CSDMS models.

## Requirements

These recipes are designed for Linux distros
that are compatible with Red Hat Enterprise Linux
(e.g., CentOS, Fedora).
To install CSDMS models on Mac OS X,
please see the
[csdms/homebrew-models](https://github.com/csdms/homebrew-models)
project.

To build and install the tools in this project,
the mandatory and default packages in the 
"Development Tools" group (such as `make`, `gcc`, and `rpm-build`) 
are required,
as well as the optional `cmake`, `git` and `rpmdevtools` packages.
Install them with:
```bash
$ sudo yum groupinstall "development tools"
$ sudo yum install cmake git rpmdevtools
```

## Preparation

Download and install the `packagebuilder` Python package from the
[csdms/packagebuilder](https://github.com/csdms/packagebuilder)
repository:
```bash
$ git clone https://github.com/csdms/packagebuilder.git
$ cd packagebuilder
$ sudo python setup.py install
```
This installs the script `build_rpm`,
which can be used to build the RPMs for a model.

To separate the CSDMS software stack from other programs,
it's designed to be installed 
in the directory **/usr/local/csdms**,
although this is optional.
Set the environment variable `CSDMS_DIR`:
```bash
$ export CSDMS_DIR=/usr/local/csdms
```
to the installation path on your machine.
`CSDMS_DIR` is used by several recipes in this project.

The `QA_RPATHS` environment variable may also need to be set:
```bash
$ export QA_RPATHS=19
```
for building RPMs.

## Building a package

To create RPMs for a model,
call `build_rpm` with the model name as a parameter.
For example, to build `hydrotrend`:

```bash
$ build_rpm hydrotrend --prefix=$CSDMS_DIR
```
The `build_rpm` script
downloads the source 
(the HEAD revision on the trunk branch) 
for the specified model 
from a hosted repository (CSDMS or GitHub),
then calls
[rpmbuild](http://www.rpm.org/max-rpm-snapshot/rpmbuild.8.html)
to create binary and source RPMs for the model.
On success,
RPMs will be located in the directories
**~/rpmbuild/RPMS** (binary) and
**~/rpmbuild/SRPMS** (source)
on your machine.

## Installation

Install the package from the binary RPM with `rpm`.
For example:
```bash
$ sudo rpm -ivh hydrotrend-head-1.el6.x86_64.rpm
```

Check that the package was installed successfully:
```bash
$ hydrotrend --version
HydroTrend version 3.0.5
```

## The CSDMS repository

Built versions of all of the models in this project are available 
from the CSDMS repository, 
[http://csdms.colorado.edu/repo/](http://csdms.colorado.edu/repo/).
See the [README.md](http://csdms.colorado.edu/repo/README.md) file
for instructions on how to install these packages 
on your machine.

## About CSDMS

[CSDMS](http://csdms.colorado.edu/wiki/Main_Page),
the Community Surface Dynamics Modeling System,
is an NSF-funded project that supports a diverse community
of users and developers
of earth and ocean system models. 
CSDMS develops, integrates, archives and disseminates
earth system models and tools to an international community
with the goal of building the frameworks necessary
to model the earth system.
Modelers use CSDMS for access
to hundreds of open source surface dynamics models and tools,
as well as model metadata.
