%define lib32dir %{_prefix}/lib

Name:		sedflux
Version:	%{_version}
Release:	3%{?dist}
Summary:	Basin-filling stratigraphic model
Group:		Applications/Engineering
License:	GPLv2
URL:		http://csdms.colorado.edu/wiki/Model:Sedflux
# The Sedflux source can be checked out from GitHub:
# $ git clone https://github.com/mcflugen/sedflux.git
Source0:	%{name}-%{version}.tar.gz
# This patch allows the -DLIB_SUFFIX option to CMake.
# Patch0:		%{name}-cmakelibsuffix.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		%{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description 
Sedflux-2.0 is the newest version of the Sedflux basin-filling
model. Sedflux-2.0 provides a framework within which individual
process-response models of disparate time and space resolutions
communicate with one another to deliver multi grain sized sediment
load across a continental margin.

%package -n avulsion
Summary:	Stream avulsion model
Group:		Applications/Engineering
URL:            http://csdms.colorado.edu/wiki/Model:Avulsion

%description -n avulsion
Avulsion dictates the movement of rivermouths along a coastline 
by modeling the changes of river channel angles through the 
floodplain as a stochastic random walk process.

%package -n plume
Summary:        Hypopycnal sediment plume
Group:          Applications/Engineering
URL:            http://csdms.colorado.edu/wiki/Model:Plume

%description -n plume
Plume simulates the sediment transport and deposition of several 
grainsize classes from a river mouth entering into a marine basin 
by creating a turbulent jet. The model forms a hypopycnal plume. 
The model allows for plume deflection due to systematic currents 
or Coriolis force.

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
#ctest

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post -n avulsion
/sbin/ldconfig
%postun -n avulsion
/sbin/ldconfig

%post -n plume
/sbin/ldconfig
%postun -n plume
/sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{_includedir}/
%{lib32dir}/

%files -n avulsion
%defattr(-,root,root,-)
%{_bindir}/avulsion
%{lib32dir}/libavulsion.so
%{lib32dir}/libbing.so
%{lib32dir}/libbio.so
%{lib32dir}/libbmiplume.so
%{lib32dir}/libcompact.so
%{lib32dir}/libdiffusion.so
%{lib32dir}/libfailure.so
%{lib32dir}/libflow.so
%{lib32dir}/libinflow.so
%{lib32dir}/libmuds.so
%{lib32dir}/libplume.so
%{lib32dir}/libquake.so
%{lib32dir}/libsakura.so
%{lib32dir}/libsedflux-2.0.so
%{lib32dir}/libsedflux.so
%{lib32dir}/libsquall.so
%{lib32dir}/libsubside.so
%{lib32dir}/libutils.so
%{lib32dir}/libxshore.so
%{lib32dir}/pkgconfig/avulsion.pc
%{lib32dir}/pkgconfig/sed.pc
%{lib32dir}/pkgconfig/utils.pc
%{_includedir}/bmi_avulsion.h
%{_includedir}/ew-2.0/avulsion*.h
%{_includedir}/ew-2.0/utils/

%files -n plume
%defattr(-,root,root,-)
%{_bindir}/plume
%{lib32dir}/libavulsion.so
%{lib32dir}/libbing.so
%{lib32dir}/libbio.so
%{lib32dir}/libbmiplume.so
%{lib32dir}/libcompact.so
%{lib32dir}/libdiffusion.so
%{lib32dir}/libfailure.so
%{lib32dir}/libflow.so
%{lib32dir}/libinflow.so
%{lib32dir}/libmuds.so
%{lib32dir}/libplume.so
%{lib32dir}/libquake.so
%{lib32dir}/libsakura.so
%{lib32dir}/libsedflux-2.0.so
%{lib32dir}/libsedflux.so
%{lib32dir}/libsquall.so
%{lib32dir}/libsubside.so
%{lib32dir}/libutils.so
%{lib32dir}/libxshore.so
%{lib32dir}/pkgconfig/plume.pc
%{lib32dir}/pkgconfig/sed.pc
%{lib32dir}/pkgconfig/utils.pc
%{_includedir}/bmi_plume.h
%{_includedir}/ew-2.0/plume*.h
%{_includedir}/ew-2.0/utils/

%changelog
* Wed Oct 22 2014 Mark Piper <mark.piper@colorado.edu> - %{_version}-3
- Install all CSDMS software into %lib32dir

* Thu Aug 28 2014 Mark Piper <mark.piper@colorado.edu>
- Produce separate RPMs for avulsion and plume
- Make package relocatable

* Tue Aug 26 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package

