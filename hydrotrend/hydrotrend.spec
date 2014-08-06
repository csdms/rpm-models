Name:		hydrotrend
Version:	head
Release:	1%{?dist}
Summary:	A hydrological water balance and transport model
Group:		Applications/Engineering
License:	GPLv3
URL:		http://csdms.colorado.edu/wiki/Model:HydroTrend
# The HydroTrend source can be checked out from the CSDMS Trac site:
# $ svn co http://csdms.colorado.edu/svn/hydrotrend/trunk
Source0:	%{name}-%{version}.tar.gz
# This patch is temporary until Albert applies it upstream.
Patch0:		hydrotrend-head-cmakelist.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}

#BuildRequires:
#Requires:

%description
HydroTrend is a climate-driven hydrological water balance and transport
model that simulates water discharge and sediment load at a river outlet.

%prep
%setup -q
%patch0

%build
%cmake . -DLIB_SUFFIX=64
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%check
ctest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc FLOWCHART NEWS README
%{_bindir}/%{name}
%{_includedir}/%{name}_cli.h
%{_includedir}/bmi_%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/input/*
%{_datadir}/%{name}/output/*

%changelog
* Wed Aug 6 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package
