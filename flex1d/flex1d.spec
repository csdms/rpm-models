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
Prefix:		/usr

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/%{name}
#%{_datadir}/%{name}/load1dandes

%changelog
* Tue Sep 9 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package
