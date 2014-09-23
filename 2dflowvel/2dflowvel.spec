Name:		2dflowvel
Version:	%{_version}
Release:	1%{?dist}
Summary:	Tidal and wind-driven coastal circulation routine
Group:		Applications/Engineering
License:	Other
URL:		http://csdms.colorado.edu/wiki/Model:2DFLOWVEL
# The 2DFLOWVEL source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/2dflowvel/trunk
Source0:	%{name}-%{version}.tar.gz
# This patch replaces explicit "gfortran" with $FC.
Patch0:		%{name}-fc.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		/usr

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
Two-dimensional unsteady nonlinear tidal & wind-driven coastal circulation
model.

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
* Thu Sep 11 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package
