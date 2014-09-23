Name:		marssim
Version:	%{_version}
Release:	1%{?dist}
Summary:	Landform evolution model
Group:		Applications/Engineering
License:	Other
URL:		http://csdms.colorado.edu/wiki/Model:MARSSIM
# The MARSSIM source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/marssim/trunk
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		/usr

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
A landform evolution model operating at the drainage basin or larger
scale. Recent model development has targeted planetary applications.

%prep
%setup -q

%build
%cmake .
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/run_%{name}
# /usr/local/lib/libmarssim.so
# /usr/local/include/accretion_globals.mod
# /usr/local/include/area_globals.mod
# /usr/local/include/crater_globals.mod
# /usr/local/include/eolian_globals.mod
# /usr/local/include/erode_globals.mod
# /usr/local/include/lake_globals.mod
# /usr/local/include/lava_globals.mod
# /usr/local/include/marssim_irf.mod
# /usr/local/include/ocean_globals.mod
# /usr/local/include/seddebug_globals.mod
# /usr/local/include/sedroute_globals.mod

%changelog
* Mon Sep 22 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package
