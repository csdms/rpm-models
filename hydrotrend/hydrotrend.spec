%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc

Name:		hydrotrend
Version:	%{_version}
Release:	4%{?dist}
Summary:	A hydrological water balance and transport model
Group:		Applications/Engineering
License:	GPLv3
URL:		http://csdms.colorado.edu/wiki/Model:HydroTrend
# The HydroTrend source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/hydrotrend/trunk
Source0:	%{name}-%{version}.tar.gz
# This patch allows the -DLIB_SUFFIX option to CMake.
#Patch0:		%{name}-cmakelibsuffix.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		%{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
HydroTrend is a climate-driven hydrological water balance and transport
model that simulates water discharge and sediment load at a river outlet.

%prep
%setup -q
#%patch0

%build
%cmake .
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m755 README FLOWCHART %{buildroot}%{docdir}/%{name}-%{version}/

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
%{_datadir}/

%changelog
* Wed Oct 22 2014 Mark Piper <mark.piper@colorado.edu> - %{_version}-4
- Install all CSDMS software into %lib32dir

* Wed Sep 24 2014 Mark Piper <mark.piper@colorado.edu>
- Configure for CSDMS custom install location (/usr/local/csdms)

* Thu Aug 28 2014 Mark Piper <mark.piper@colorado.edu>
- Make package relocatable

* Tue Aug 26 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package

