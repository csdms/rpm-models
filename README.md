rpm-models
==========

Scripts for building binary and source RPMs for CSDMS models.

**Usage**

Call the bash script `build_model_rpm.sh` with the model name and 
version tag as parameters:

```bash
$ bash build_model_rpm.sh -m hydrotrend -t head
```

The script
downloads the tagged version of the specified model from the
CSDMS repository,
then calls
[rpmbuild](http://www.rpm.org/max-rpm-snapshot/rpmbuild.8.html)
to create the binary and source RPMs.
On success,
the RPMs will be located in the directories:

* **~/rpmbuild/RPMS** (binary)
* **~/rpmbuild/SRPMS** (source)

on your machine.
