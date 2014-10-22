%define docdir %{_datadir}/doc

Name:		flex1d
Version:	%{_version}
Release:	1%{?dist}
Summary:	Fourier filtering in 1D while solving the flexure equation
Group:		Applications/Engineering
License:	GPLv3
URL:		http://csdms.colorado.edu/wiki/Model:Flex1D
# The Flex1D source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/flex1d/trunk
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		%{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
Flex1D employs Fourier filtering in 1D while solving the flexure
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
install -m755 load1dandes %{buildroot}%{_datadir}/%{name}/ # patch?
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 AUTHORS ChangeLog COPYING INSTALL NEWS README \
	%{buildroot}%{docdir}/%{name}-%{version}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{docdir}/%{name}-%{version}/
%{_bindir}/%{name}
%{_datadir}/%{name}/load1dandes

%changelog
* Fri Sep 26 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package
- Configure for CSDMS custom install location (/usr/local/csdms)
