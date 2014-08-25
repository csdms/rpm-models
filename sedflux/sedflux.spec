Name:		sedflux
Version:	%{_version}
Release:	1%{?dist}
Summary:	Basin-filling stratigraphic model
Group:		Applications/Engineering
License:	GPLv2
URL:		http://csdms.colorado.edu/wiki/Model:Sedflux
# The Sedflux source can be checked out from GitHub:
# $ git clone https://github.com/mcflugen/sedflux.git
Source0:	%{name}-%{version}.tar.gz
# This patch allows the -DLIB_SUFFIX option to CMake.
Patch0:		%{name}-cmakelibsuffix.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif
#Requires:

%description 
Sedflux-2.0 is the newest version of the Sedflux
basin-filling model. Sedflux-2.0 provides a framework within which
individual process-response models of disparate time and space
resolutions communicate with one another to deliver multi grain sized
sediment load across a continental margin.

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
#ctest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/avulsion
%{_bindir}/bing
%{_bindir}/bio
%{_bindir}/compact
%{_bindir}/create_hydro
%{_bindir}/diffusion
%{_bindir}/earthquake
%{_bindir}/flow
%{_bindir}/flow_2d
%{_bindir}/flow_3d
%{_bindir}/getfloor
%{_bindir}/inflow
%{_bindir}/muds
%{_bindir}/plume
%{_bindir}/plume_run_file
%{_bindir}/pseudoplume
%{_bindir}/read_hydro
%{_bindir}/read_usgs
%{_bindir}/sakura
%{_bindir}/sed-print-input
%{_bindir}/sed2binary
%{_bindir}/sedextract
%{_bindir}/sedflux
%{_bindir}/sedflux-make-bathy
%{_bindir}/sedflux-make-sequence
%{_bindir}/sedflux-read-hydro
%{_bindir}/sedrescale
%{_bindir}/sedwheeler
%{_bindir}/squall
%{_bindir}/subside
%{_bindir}/write_test_file
%{_includedir}/bmi_avulsion.h
%{_includedir}/bmi_plume.h
%{_includedir}/bmi_sedflux.h
%{_includedir}/bmi_sedflux2d.h
%{_includedir}/bmi_sedflux3d.h
%{_includedir}/ew-2.0/avulsion.h
%{_includedir}/ew-2.0/avulsion_api.h
%{_includedir}/ew-2.0/bing.h
%{_includedir}/ew-2.0/bio.h
%{_includedir}/ew-2.0/compact.h
%{_includedir}/ew-2.0/diffusion.h
%{_includedir}/ew-2.0/earthquake.h
%{_includedir}/ew-2.0/eh_utils.h
%{_includedir}/ew-2.0/failure.h
%{_includedir}/ew-2.0/flow.h
%{_includedir}/ew-2.0/inflow.h
%{_includedir}/ew-2.0/muds.h
%{_includedir}/ew-2.0/plume_approx.h
%{_includedir}/ew-2.0/plume_local.h
%{_includedir}/ew-2.0/plume_types.h
%{_includedir}/ew-2.0/plumeinput.h
%{_includedir}/ew-2.0/plumevars.h
%{_includedir}/ew-2.0/sakura.h
%{_includedir}/ew-2.0/sed.h
%{_includedir}/ew-2.0/sed/csdms.h
%{_includedir}/ew-2.0/sed/datadir_path.h
%{_includedir}/ew-2.0/sed/etk_addrem.h
%{_includedir}/ew-2.0/sed/etk_keyvalue.h
%{_includedir}/ew-2.0/sed/sed_cell.h
%{_includedir}/ew-2.0/sed/sed_column.h
%{_includedir}/ew-2.0/sed/sed_const.h
%{_includedir}/ew-2.0/sed/sed_cube.h
%{_includedir}/ew-2.0/sed/sed_diag.h
%{_includedir}/ew-2.0/sed/sed_epoch.h
%{_includedir}/ew-2.0/sed/sed_hydro.h
%{_includedir}/ew-2.0/sed/sed_hydrotrend.h
%{_includedir}/ew-2.0/sed/sed_process.h
%{_includedir}/ew-2.0/sed/sed_property.h
%{_includedir}/ew-2.0/sed/sed_property_file.h
%{_includedir}/ew-2.0/sed/sed_river.h
%{_includedir}/ew-2.0/sed/sed_sediment.h
%{_includedir}/ew-2.0/sed/sed_signal.h
%{_includedir}/ew-2.0/sed/sed_tripod.h
%{_includedir}/ew-2.0/sed/sed_wave.h
%{_includedir}/ew-2.0/sedflux.h
%{_includedir}/ew-2.0/sedflux_api.h
%{_includedir}/ew-2.0/squall.h
%{_includedir}/ew-2.0/subside.h
%{_includedir}/ew-2.0/subside_api.h
%{_includedir}/ew-2.0/utils/complex.h
%{_includedir}/ew-2.0/utils/eh_data_record.h
%{_includedir}/ew-2.0/utils/eh_dlm_file.h
%{_includedir}/ew-2.0/utils/eh_file_utils.h
%{_includedir}/ew-2.0/utils/eh_get_opt.h
%{_includedir}/ew-2.0/utils/eh_glib.h
%{_includedir}/ew-2.0/utils/eh_grid.h
%{_includedir}/ew-2.0/utils/eh_input_val.h
%{_includedir}/ew-2.0/utils/eh_io.h
%{_includedir}/ew-2.0/utils/eh_key_file.h
%{_includedir}/ew-2.0/utils/eh_logging.h
%{_includedir}/ew-2.0/utils/eh_macros.h
%{_includedir}/ew-2.0/utils/eh_mem.h
%{_includedir}/ew-2.0/utils/eh_messages.h
%{_includedir}/ew-2.0/utils/eh_misc.h
%{_includedir}/ew-2.0/utils/eh_ndgrid.h
%{_includedir}/ew-2.0/utils/eh_num.h
%{_includedir}/ew-2.0/utils/eh_opt_context.h
%{_includedir}/ew-2.0/utils/eh_polygon.h
%{_includedir}/ew-2.0/utils/eh_project.h
%{_includedir}/ew-2.0/utils/eh_rand.h
%{_includedir}/ew-2.0/utils/eh_scanner.h
%{_includedir}/ew-2.0/utils/eh_sequence.h
%{_includedir}/ew-2.0/utils/eh_status_bar.h
%{_includedir}/ew-2.0/utils/eh_str.h
%{_includedir}/ew-2.0/utils/eh_symbol_table.h
%{_includedir}/ew-2.0/utils/eh_thread_pool.h
%{_includedir}/ew-2.0/utils/eh_types.h
%{_includedir}/ew-2.0/utils/f2c.h
%{_includedir}/ew-2.0/utils/utils.h
%{_includedir}/ew-2.0/xshore.h
%{_libdir}/libavulsion.so
%{_libdir}/libbing.so
%{_libdir}/libbio.so
%{_libdir}/libbmiplume.so
%{_libdir}/libbmisedflux2d.so
%{_libdir}/libbmisedflux3d.so
%{_libdir}/libcompact.so
%{_libdir}/libdiffusion.so
%{_libdir}/libfailure.so
%{_libdir}/libflow.so
%{_libdir}/libinflow.so
%{_libdir}/libmuds.so
%{_libdir}/libplume.so
%{_libdir}/libquake.so
%{_libdir}/libsakura.so
%{_libdir}/libsedflux-2.0.so
%{_libdir}/libsedflux.so
%{_libdir}/libsquall.so
%{_libdir}/libsubside.so
%{_libdir}/libutils.so
%{_libdir}/libxshore.so
%{_libdir}/pkgconfig/avulsion.pc
%{_libdir}/pkgconfig/plume.pc
%{_libdir}/pkgconfig/sed.pc
%{_libdir}/pkgconfig/sedflux.pc
%{_libdir}/pkgconfig/sedflux2d.pc
%{_libdir}/pkgconfig/sedflux3d.pc
%{_libdir}/pkgconfig/utils.pc

%changelog
* Sun Aug 24 2014 Mark Piper <mark.piper@colorado.edu>
- Set up spec file for building package
