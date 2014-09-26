%define docdir %{_datadir}/doc

Name:		flex2d
Version:	%{_version}
Release:	1%{?dist}
Summary:	Fourier filtering in 2D while solving the flexure equation
Group:		Applications/Engineering
License:	GPLv3
URL:		http://csdms.colorado.edu/wiki/Model:Flex2D
# The Flex2D source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/flex2d/trunk
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		%{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
Flex2D employs Fourier filtering in 2D while solving the flexure
equation.

%prep
%setup -q

%build
./bootstrap
%configure LIBS="-lm"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{_datadir}/%{name}
install -m755 load2dandes %{buildroot}%{_datadir}/%{name}/ # patch?
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 AUTHORS %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 ChangeLog %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 COPYING %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 INSTALL %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 NEWS %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 README %{buildroot}%{docdir}/%{name}-%{version}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{docdir}/%{name}-%{version}/
%{_bindir}/%{name}
%{_datadir}/%{name}/load2dandes

%changelog
* Fri Sep 26 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package
- Configure for CSDMS custom install location (/usr/local/csdms)
