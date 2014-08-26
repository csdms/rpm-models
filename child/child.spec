Name:		child
Version:	%{_version}
Release:	1%{?dist}
Summary:	A landscape evolution model
Group:		Applications/Engineering
License:	GPLv2
URL:		http://csdms.colorado.edu/wiki/Model:CHILD
# The CHILD source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/child/trunk
Source0:	%{name}-%{version}.tar.gz
# This patch allows the -DLIB_SUFFIX option to CMake.
Patch0:		%{name}-cmakelibsuffix.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif
#Requires:

%description
CHILD computes the time evolution of a topographic surface z(x,y,t) 
by fluvial and hillslope erosion and sediment transport.

%prep
%setup -q
%patch0

%build
%cmake . -DLIB_SUFFIX=64
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%check
ctest

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_includedir}/%{name}/ChildInterface/bmi_model_%{name}.h
%{_includedir}/%{name}/ChildInterface/%{name}.h
%{_includedir}/%{name}/ChildInterface/%{name}Interface.h
%{_includedir}/%{name}/Classes.h
%{_includedir}/%{name}/Definitions.h
%{_includedir}/%{name}/Erosion/erosion.h
%{_includedir}/%{name}/Geometry/geometry.h
%{_includedir}/%{name}/Inclusions.h
%{_includedir}/%{name}/Mathutil/mathutil.h
%{_includedir}/%{name}/MeshElements/meshElements.h
%{_includedir}/%{name}/Predicates/predicates.h
%{_includedir}/%{name}/Template_model.h
%{_includedir}/%{name}/compiler.h
%{_includedir}/%{name}/errors/errors.h
%{_includedir}/%{name}/globalFns.h
%{_includedir}/%{name}/tArray/tArray.cpp
%{_includedir}/%{name}/tArray/tArray.h
%{_includedir}/%{name}/tArray/tArray2.h
%{_includedir}/%{name}/tEolian/tEolian.h
%{_includedir}/%{name}/tFloodplain/tFloodplain.h
%{_includedir}/%{name}/tIDGenerator/tIDGenerator.h
%{_includedir}/%{name}/tInputFile/tInputFile.h
%{_includedir}/%{name}/tLNode/tLNode.h
%{_includedir}/%{name}/tList/tList.h
%{_includedir}/%{name}/tList/tListFwd.h
%{_includedir}/%{name}/tListInputData/tListInputData.h
%{_includedir}/%{name}/tLithologyManager/tLithologyManager.h
%{_includedir}/%{name}/tMatrix/tMatrix.cpp
%{_includedir}/%{name}/tMatrix/tMatrix.h
%{_includedir}/%{name}/tMesh/ParamMesh_t.h
%{_includedir}/%{name}/tMesh/TipperTriangulator.h
%{_includedir}/%{name}/tMesh/heapsort.h
%{_includedir}/%{name}/tMesh/tMesh.cpp
%{_includedir}/%{name}/tMesh/tMesh.h
%{_includedir}/%{name}/tMesh/tMesh2.cpp
%{_includedir}/%{name}/tMeshList/tMeshList.h
%{_includedir}/%{name}/tOption/tOption.h
%{_includedir}/%{name}/tOutput/tOutput.cpp
%{_includedir}/%{name}/tOutput/tOutput.h
%{_includedir}/%{name}/tPtrList/tPtrList.h
%{_includedir}/%{name}/tRunTimer/tRunTimer.h
%{_includedir}/%{name}/tStorm/tStorm.h
%{_includedir}/%{name}/tStratGrid/tStratGrid.h
%{_includedir}/%{name}/tStreamMeander/meander.h
%{_includedir}/%{name}/tStreamMeander/tStreamMeander.h
%{_includedir}/%{name}/tStreamNet/tStreamNet.h
%{_includedir}/%{name}/tTimeSeries/tTimeSeries.h
%{_includedir}/%{name}/tUplift/tUplift.h
%{_includedir}/%{name}/tVegetation/tVegetation.h
%{_includedir}/%{name}/tWaterSedTracker/tWaterSedTracker.h
%{_includedir}/%{name}/trapfpe.h
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Aug 26 2014 Mark Piper <mark.piper@colorado.edu>
- Initial version of the package
