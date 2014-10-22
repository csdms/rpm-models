%define lib32dir %{_prefix}/lib

Name:		child
Version:	%{_version}
Release:	4%{?dist}
Summary:	A landscape evolution model
Group:		Applications/Engineering
License:	GPLv2
URL:		http://csdms.colorado.edu/wiki/Model:CHILD
# The CHILD source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/child/trunk
Source0:	%{name}-%{version}.tar.gz
# This patch allows the -DLIB_SUFFIX option to CMake.
# Patch0:		%{name}-cmakelibsuffix.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		%{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
CHILD computes the time evolution of a topographic surface z(x,y,t) 
by fluvial and hillslope erosion and sediment transport.

%prep
%setup -q
#%patch0

%build
%cmake .
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%check
ctest

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{_includedir}/
%{lib32dir}/

%changelog
* Wed Oct 22 2014 Mark Piper <mark.piper@colorado.edu> - %{_version}-4
- Install all CSDMS software into %lib32dir

* Fri Sep 26 2014 Mark Piper <mark.piper@colorado.edu>
- Configure for CSDMS custom install location (/usr/local/csdms)

* Thu Aug 28 2014 Mark Piper <mark.piper@colorado.edu>
- Make package relocatable

* Tue Aug 26 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package

