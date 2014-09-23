Name:		storm
Version:	%{_version}
Release:	1%{?dist}
Summary:	Windfield simulator for a cyclone
Group:		Applications/Engineering
License:	Other
URL:		http://csdms.colorado.edu/wiki/Model:STORM
# The STORM source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/storm/trunk
Source0:	%{name}-%{version}.tar.gz
# This patch replaces explicit "gfortran" with $FC.
Patch0:		%{name}-fc.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		/usr

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
Storm computes the windfield for a cyclone.

%prep
%setup -q
%patch0

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp %{name} %{buildroot}%{_bindir} # patch?

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Mon Sep 22 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package
