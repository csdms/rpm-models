[![Build Status](https://travis-ci.org/csdms/rpm-models.svg?branch=master)](https://travis-ci.org/csdms/rpm-models)

rpm-models
==========

Scripts for building binary and source RPMs for CSDMS models.

**Requirements**

These Python scripts are designed to run on Linux
(various RHEL and Debian flavors have been tested).
To install CSDMS models on Mac OS X,
please see the
[csdms/homebrew-models](https://github.com/csdms/homebrew-models)
project.

**Preparation**

Call `check_dependencies.py`
to ensure that all the packages needed to build an RPM
for a particular model
are installed on your machine:

```bash
$ python check_dependencies.py --model hydrotrend
```

Be sure to install any required packages before proceeding.

**Building a package**

To create RPMs for a model,
call `build_rpm.py` with the model name as a parameter:

```bash
$ python build_rpm.py hydrotrend
```

This script
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

Install the package with `rpm`,
or (better) with a package manager, such as `yum`.
For example,

```bash
$ sudo rpm -ivp hydrotrend-head-1.el6.x86_64.rpm
```

or

```bash
$ sudo yum install hydrotrend-head-1.el6.x86_64.rpm
```

Check that the package was installed successfully:

```bash
$ hydrotrend --version
HydroTrend version 3.0.5
```


