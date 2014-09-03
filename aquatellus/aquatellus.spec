Name:		aquatellus
Version:	%{_version}
Release:	1%{?dist}
Summary:	Fluvial-dominated delta sedimentation model
Group:		Applications/Engineering
License:	Other
URL:		http://csdms.colorado.edu/wiki/Model:AquaTellUs
# The AquaTellUs source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/aquatellus/trunk
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		/usr

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
AquaTellUs models fluvial-dominated delta sedimentation using a nested
model approach, with 2D longitudinal profiles embedded as a dynamical
flowpath in a 3D grid-based space. A main channel belt is modeled as a
2D longitudinal profile that responds dynamically to changes in
discharge, sediment load and sea level. Sediment flux is described by
separate erosion and sedimentation components. Multiple grain-size
classes are independently tracked. Erosion flux depends on discharge
and slope, similar to process descriptions used in hill-slope models
and is independent of grain-size. Offshore, where we assume unconfined
flow, the erosion capacity decreases with increasing water depth. The
erosion flux is a proxy for gravity flows in submarine channels close
to the coast and for down-slope diffusion over the entire slope due to
waves, tides and creep. Erosion is restricted to the main
flowpath. Deposition flux depends on the stream velocity and on a
travel-distance factor, which depends on grain size (i.e. settling
velocity). The travel-distance factor is different in the fluvial and
marine domains, which results in a sharp increase of the settling rate
at the river mouth, mimicking bedload dumping. Dynamic boundary
conditions such as climatic changes over time are incorporated by
increasing or decreasing discharge and sediment load for each time
step.

%prep
%setup -q

%build
%cmake . %_cmake_lib_suffix64
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%check
ctest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_includedir}/%{name}_bmi.h
%{_libdir}/lib%{name}.so

%changelog
* Wed Sep 3 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package

