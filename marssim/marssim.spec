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
# This patch allows the -DLIB_SUFFIX option to CMake.
Patch0:		%{name}-cmakelibsuffix.patch
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
%patch0

%build
%cmake . %_cmake_lib_suffix64
make # deparallelize

# No install target given; install manually.
%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_bindir}
install -m755 src/run_marssim %{buildroot}%{_bindir}/
install -d -m755 %{buildroot}%{_libdir}
install -m755 src/libmarssim.so %{buildroot}%{_libdir}/
install -d -m755 %{buildroot}%{_datadir}
install -m755 src/*.mod %{buildroot}%{_datadir}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%check
ctest

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/run_%{name}
%{_libdir}/lib%{name}.so
%{_datadir}/

%changelog
* Tue Sep 23 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package
