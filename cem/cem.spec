Name:		cem
Version:	%{_version}
Release:	1%{?dist}
Summary:	The Coastline Evolution Model from Duke University
Group:		Applications/Engineering
License:	BSD
URL:		http://csdms.colorado.edu/wiki/Model:CEM
# The CEM source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/cem/trunk
Source0:	%{name}-%{version}.tar.gz
# Patch0 turns off use of g++ in building CEM.
Patch0:		cem-cmakecxx.patch
# Patch1 allows the -DLIB_SUFFIX option to CMake.
Patch1:		cem-cmakelibsuffix.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}

BuildRequires:	%{_buildrequires}
#Requires:

%global _waves waves
%global _deltas deltas

%description
The Coastline Evolution Model (CEM) addresses predominately sandy,
wave-dominated coastlines on time-scales ranging from years to
millenia and on spatial scales ranging from kilometers to hundreds of
kilometers. Shoreline evolution results from gradients in wave-driven
alongshore sediment transport. At its most basic level, the model
follows the standard 'one-line' modeling approach, where the
cross-shore dimension is collapsed into a single data point. However,
the model allows the plan-view shoreline to take on arbitrary local
orientations, and even fold back upon itself, as complex shapes such
as capes and spits form under some wave climates (distributions of
wave influences from different approach angles). The model can also
represent the geology underlying the sandy coastline and shoreface in
a simplified manner and enables the simulation of coastline evolution
when sediment supply from an eroding shoreface may be constrained. CEM
also supports the simulation of human manipulations to coastline
evolution through beach nourishment or hard structures.

%prep
%setup -q
%patch0
%patch1

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/%{_deltas}
%{_bindir}/%{_waves}
%{_includedir}/bmi_%{name}.h
%{_includedir}/bmi_%{_waves}.h
%{_includedir}/%{_deltas}_api.h
%{_includedir}/%{_deltas}_cli.h
%{_includedir}/%{_waves}_cli.h
%{_libdir}/libbmi%{name}.so
%{_libdir}/libbmi%{_waves}.so
%{_libdir}/pkgconfig/%{_deltas}.pc
%{_libdir}/pkgconfig/%{_waves}.pc
%{_datadir}/%{_deltas}/output/*

%changelog
* Tue Aug 19 2014 Mark Piper <mark.piper@colorado.edu>
- Set up spec file for building package
