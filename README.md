[![Build Status](https://travis-ci.org/csdms/rpm_models.svg?branch=master)](https://travis-ci.org/csdms/rpm_models)

rpm_models
==========

Recipes for building binary and source RPMs for CSDMS models.

**Requirements**

These recipes are designed for Linux distros
that are compatible with Red Hat Enterprise Linux
(e.g., CentOS, Fedora).
To install CSDMS models on Mac OS X,
please see the
[csdms/homebrew-models](https://github.com/csdms/homebrew-models)
project.

**Preparation**

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

**Building a package**

To create RPMs for a model,
call `build_rpm` with the model name as a parameter.
For example, to build `hydrotrend`:

```bash
$ build_rpm hydrotrend
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
the RPMs will be located in the directories:

* **~/rpmbuild/RPMS** (binary)
* **~/rpmbuild/SRPMS** (source)

on your machine.

**Installation**

Install the package with `rpm`.
For example,

```bash
$ sudo rpm -ivp hydrotrend-head-1.el6.x86_64.rpm
```

Check that the package was installed successfully:

```bash
$ hydrotrend --version
HydroTrend version 3.0.5
```
