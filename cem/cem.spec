%define waves waves
%define deltas deltas
%define docdir %{_datadir}/doc
%define lib32dir %{_prefix}/lib

Name:		cem
Version:	%{_version}
Release:	4%{?dist}
Summary:	The Coastline Evolution Model from Duke University
Group:		Applications/Engineering
License:	BSD
URL:		http://csdms.colorado.edu/wiki/Model:CEM
# The CEM source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/cem/trunk
Source0:	%{name}-%{version}.tar.gz
# Patch0 turns off use of g++ in building CEM.
Patch0:		%{name}-cmakecxx.patch
# Patch1 allows the -DLIB_SUFFIX option to CMake.
# Patch1:		%{name}-cmakelibsuffix.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		%{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

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
#%patch1

%build
%cmake .
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 AUTHORS ChangeLog COPYING INSTALL NEWS README \
	%{buildroot}%{docdir}/%{name}-%{version}/

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

* Fri Sep 26 2014 Mark Piper <mark.piper@colorado.edu>
- Configure for CSDMS custom install location (/usr/local/csdms)

* Thu Aug 28 2014 Mark Piper <mark.piper@colorado.edu>
- Make package relocatable

* Tue Aug 26 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package
