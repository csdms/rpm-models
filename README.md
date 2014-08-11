rpm-models
==========

Scripts for building binary and source RPMs for CSDMS models.

**Preparation**

Optionally call the Python script `check_dependencies.py`
to ensure that all the packages needed to build an RPM
are installed on your machine:

```bash
$ python check_dependencies.py --model hydrotrend
```

Be sure to install any required packages.

**Building a package**

To create RPMs for a model,
call the bash script `build_model_rpm.sh` with the model name and 
version tag as parameters:

```bash
$ bash build_model_rpm.sh -m hydrotrend -t head
```

This script
downloads the tagged version of the specified model from the
CSDMS repository,
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
or with a package manager, such as `yum`.
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


