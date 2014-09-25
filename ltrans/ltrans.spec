Name:		ltrans
Version:	%{_version}
Release:	1%{?dist}
Summary:	An off-line particle-tracking model that runs with the stored predictions of a 3D hydrodynamic model
Group:		Applications/Engineering
License:	MIT
URL:		http://csdms.colorado.edu/wiki/Model:LTRANS
# The LTRANS source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/ltrans/trunk
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:		/usr

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
The Larval TRANSport Lagrangian model (LTRANS) is an off-line
particle-tracking model that runs with the stored predictions of a 3D
hydrodynamic model, specifically the Regional Ocean Modeling System
(ROMS). Although LTRANS was built to simulate oyster larvae, it can
easily be adapted to simulate passive particles and other planktonic
organisms. LTRANS is written in Fortran 90 and is designed to track
the trajectories of particles in three dimensions. It includes a 4th
order Runge-Kutta scheme for particle advection and a random
displacement model for vertical turbulent particle motion. Reflective
boundary conditions, larval behavior, and settlement routines are also
included.

%prep
%setup -q

%build
make # deparallelize

%install
rm -rf %{buildroot}
make install DEST_DIR=%{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%{_bindir}/run_%{name}
#%{_libdir}/lib%{name}.so
#%{_datadir}/

%changelog
* Wed Sep 24 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package
