%define docdir %{_datadir}/doc

Name:		adi-2d
Version:	%{_version}
Release:	2%{?dist}
Summary:	Advection Diffusion Implicit (ADI) method for solving 2D diffusion equation
Group:		Applications/Engineering
License:	GPLv3
URL:		http://csdms.colorado.edu/wiki/Model:ADI-2D
# The ADI-2D source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/adi-2d/trunk
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		%_prefix}

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
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
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

%changelog
* Fri Sep 26 2014 Mark Piper <mark.piper@colorado.edu>
- Configure for CSDMS custom install location (/usr/local/csdms)

* Tue Sep 2 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package

