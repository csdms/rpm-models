Name:		adi-2d
Version:	%{_version}
Release:	1%{?dist}
Summary:	Advection Diffusion Implicit (ADI) method for solving 2D diffusion equation
Group:		Applications/Engineering
License:	GPLv3
URL:		http://csdms.colorado.edu/wiki/Model:ADI-2D
# The ADI-2D source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/adi-2d/trunk
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		/usr

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
ADI-2D employs an Advection Diffusion Implicit (ADI) method for
solving the 2D diffusion equation.

%prep
%setup -q

%build
./bootstrap
%configure LIBS="-lm"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/%{name}

%changelog
* Tue Sep 2 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package

