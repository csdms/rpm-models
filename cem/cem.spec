Name:		cem
Version:	head
Release:	1%{?dist}
Summary:	The Coastline Evolution Model from Duke University
Group:		Applications/Engineering
License:	BSD
URL:		http://csdms.colorado.edu/wiki/Model:CEM
# The CEM source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/cem/trunk
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}

#BuildRequires:
#Requires:

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

%build
%cmake .
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
# %doc FLOWCHART NEWS README
# %{_bindir}/%{name}
# %{_includedir}/%{name}_cli.h
# %{_includedir}/bmi_%{name}.h
# %{_libdir}/lib%{name}.so
# %{_libdir}/pkgconfig/%{name}.pc
# %{_datadir}/%{name}/input/*
# %{_datadir}/%{name}/output/*

%changelog
* Tue Aug 12 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package
