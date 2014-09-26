# Notes on building LTRANS

To build LTRANS, set the `FC`, `NETCDF_INCDIR`, 
and `NETCDF_LIBDIR` environment variables.
On my Centos 6.4 build machine, 
I used:

```bash
$ export FC=$(which gfortran)
$ export NETCDF_INCDIR=/usr/include
$ export NETCDF_LIBDIR=/usr/lib64
```
