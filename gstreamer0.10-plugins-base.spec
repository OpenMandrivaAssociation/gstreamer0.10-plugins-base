%define version 0.10.24
%define release %mkrel 1
%define         _glib2          2.15.2
%define major 0.10
%define majorminor 0.10
%define bname gstreamer0.10
%define name %bname-plugins-base
%define libname %mklibname gstreamer-plugins-base %major
%define oldlibname  %mklibname gstapp0.10_ 0
%define olddevelname %mklibname -d gstapp0.10_ 0
%define gstver 0.10.23.1
%define build_libvisual 1

Summary: 	GStreamer Streaming-media framework plug-ins
Name: 		%name
Version: 	%version
Release: 	%release
License: 	LGPLv2+
Group: 		Sound
Source: 	http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.bz2
Patch0: 	align.patch
URL:            http://gstreamer.freedesktop.org/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root 
Provides:	%bname-plugin-libs
Obsoletes:	%bname-plugin-libs
#gw for the pixbuf plugin
BuildRequires:  gtk+2-devel
BuildRequires:  glib2-devel >= %_glib2
BuildRequires: libpng-devel >= 1.2.4-4mdk
BuildRequires: liboil-devel >= 0.3.6
BuildRequires: libvorbis-devel >= 1.0-4mdk
BuildRequires: libtheora-devel
%ifarch %ix86
BuildRequires: nasm => 0.90
%endif
BuildRequires: libcheck-devel
%ifnarch %arm %mips
BuildRequires: valgrind
%endif
BuildRequires: libgstreamer-devel >= %gstver
BuildRequires: gtk-doc
%if %mdkversion > 200700
BuildRequires: libmesaglu-devel
BuildRequires: libxv-devel
%else
BuildRequires: mesaglu-devel
BuildRequires: X11-devel
%endif
BuildRequires: libalsa-devel
#gw we need some fonts for the tests
BuildRequires: fonts-ttf-dejavu
Provides:	%bname-audiosrc
Provides:	%bname-audiosink
Provides: %bname-alsa
Obsoletes: %bname-alsa
Provides: %bname-plugins
Obsoletes: %bname-plugins
Provides: %bname-vorbis
Obsoletes: %bname-vorbis
Provides: %bname-x11
Obsoletes: %bname-x11
Suggests: codeina
Conflicts: %bname-plugins-bad < 0.10.10


%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of reference plugins, base classes for other
plugins, and helper libraries:
 * device plugins: x(v)imagesink, alsa, v4lsrc, cdparanoia
 * containers: ogg
 * codecs: vorbis, theora
 * text: textoverlay, subparse
 * sources: audiotestsrc, videotestsrc, gnomevfssrc
 * network: tcp
 * typefind
 * audio processing: audioconvert, adder, audiorate, audioscale, volume
 * visualisation: libvisual
 * video processing: ffmpegcolorspace
 * aggregate elements: decodebin, playbin

%prep
%setup -q -n gst-plugins-base-%{version}
%patch0 -p1 -b .align

%build
%configure2_5x --disable-dependency-tracking \
  --enable-experimental \
  --with-package-name='Mandriva %name package' \
  --with-package-origin='http://www.mandriva.com/' \
	--enable-libvisual --with-install-plugins-helper="%{_bindir}/codeina"
%make

%check
cd tests/check
#gw check fail with a gconf error in 0.10.21
#make check

%install
rm -rf %buildroot gst-plugins-base-%majorminor.lang
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
%find_lang gst-plugins-base-%majorminor
# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT


%files -f gst-plugins-base-%majorminor.lang
%defattr(-, root, root)
%doc AUTHORS COPYING README NEWS
%{_bindir}/gst-visualise-%majorminor
%{_mandir}/man1/gst-visualise-%majorminor.1*
%{_libdir}/gstreamer-%{majorminor}/libgstffmpegcolorspace.so
# non-core plugins without external dependencies
%_libdir/gstreamer-%majorminor/libgstapp.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiorate.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioresample.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiotestsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecodebin.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecodebin2.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdp.so
%{_libdir}/gstreamer-%{majorminor}/libgstgio.so
%{_libdir}/gstreamer-%{majorminor}/libgstpango.so
%{_libdir}/gstreamer-%{majorminor}/libgstplaybin.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubparse.so
#%{_libdir}/gstreamer-%{majorminor}/libgstsinesrc.so
%{_libdir}/gstreamer-%{majorminor}/libgsttcp.so
%{_libdir}/gstreamer-%{majorminor}/libgstvolume.so
%{_libdir}/gstreamer-%{majorminor}/libgstadder.so
%{_libdir}/gstreamer-%{majorminor}/libgsttypefindfunctions.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideotestsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgsttheora.so
%{_libdir}/gstreamer-%{majorminor}/libgstogg.so
%{_libdir}/gstreamer-%{majorminor}/libgstqueue2.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideo4linux.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideorate.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoscale.so
%{_libdir}/gstreamer-%{majorminor}/libgstvorbis.so
%{_libdir}/gstreamer-%{majorminor}/libgstximagesink.so
%{_libdir}/gstreamer-%{majorminor}/libgstxvimagesink.so
%{_libdir}/gstreamer-%{majorminor}/libgstalsa.so

%package -n %libname
Group: 		System/Libraries
Summary: 	GStreamer plugin libraries
Obsoletes: %oldlibname

%description -n %libname
This package contain the basic audio and video playback library and
the interfaces library.

%files -n %libname
%defattr(-, root, root)
%_libdir/libgstaudio-%majorminor.so.0*
%_libdir/libgstapp-%majorminor.so.0*
%_libdir/libgstcdda-%majorminor.so.0*
%_libdir/libgstfft-%majorminor.so.0*
%_libdir/libgstinterfaces-%majorminor.so.0*
%_libdir/libgstnetbuffer-%majorminor.so.0*
%_libdir/libgstpbutils-%majorminor.so.0*
%_libdir/libgstriff-%majorminor.so.0*
%_libdir/libgstrtp-%majorminor.so.0*
%_libdir/libgstrtsp-%majorminor.so.0*
%_libdir/libgsttag-%majorminor.so.0*
%_libdir/libgstsdp-%majorminor.so.0*
%_libdir/libgstvideo-%majorminor.so.0*


%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%package -n %libname-devel
Summary: 	GStreamer Plugin Library Headers
Group: 		Development/C
Requires: 	%{libname} = %{version}
Requires:	%libname = %version
# gw is required at build time for make check
Requires:	%name = %version
Requires:	libgstreamer-devel >= %gstver
Provides:	libgstreamer-plugins-base-devel = %version-%release
Provides:	libgstreamer%majorminor-plugins-base-devel = %version-%release
Obsoletes: %olddevelname

%description -n %libname-devel
GStreamer support libraries header files.

%files -n %libname-devel
%defattr(-, root, root)
%doc docs/libs/html docs/plugins/html
%_includedir/gstreamer-%majorminor/gst/app/
%{_includedir}/gstreamer-%{majorminor}/gst/audio
%{_includedir}/gstreamer-%{majorminor}/gst/cdda/
%{_includedir}/gstreamer-%{majorminor}/gst/fft
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces
%{_includedir}/gstreamer-%{majorminor}/gst/netbuffer
%{_includedir}/gstreamer-%{majorminor}/gst/pbutils
%{_includedir}/gstreamer-%{majorminor}/gst/riff
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp
%{_includedir}/gstreamer-%{majorminor}/gst/sdp
%{_includedir}/gstreamer-%{majorminor}/gst/tag/
%{_includedir}/gstreamer-%{majorminor}/gst/video/
%{_includedir}/gstreamer-%{majorminor}/gst/floatcast/
%{_includedir}/gstreamer-%{majorminor}/gst/rtp
%{_libdir}/pkgconfig/gstreamer-app-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-audio-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-cdda-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-fft-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-floatcast-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-interfaces-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-netbuffer-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-pbutils-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-plugins-base-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-riff-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-rtp-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-rtsp-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-sdp-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-tag-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-video-%majorminor.pc
%_libdir/libgstaudio-%majorminor.so
%_libdir/libgstapp-%majorminor.so
%_libdir/libgstcdda-%majorminor.so
%_libdir/libgstfft-%majorminor.so
%_libdir/libgstinterfaces-%majorminor.so
%_libdir/libgstnetbuffer-%majorminor.so
%_libdir/libgstpbutils-%majorminor.so
%_libdir/libgstriff-%majorminor.so
%_libdir/libgstrtp-%majorminor.so
%_libdir/libgstrtsp-%majorminor.so
%_libdir/libgsttag-%majorminor.so
%_libdir/libgstsdp-%majorminor.so
%_libdir/libgstvideo-%majorminor.so
%_datadir/gtk-doc/html/*
###



### GNOME VFS 2 ###
%package -n %bname-gnomevfs
Summary: GStreamer plug-ins for GNOME VFS input and output
Group: System/Libraries
Requires: gnome-vfs2 > 1.9.4.00
Requires: %bname-plugins-base = %{version}
BuildRequires: gnome-vfs2-devel > 1.9.4.00

%description -n %bname-gnomevfs
Plug-Ins for reading and writing through GNOME VFS.

%files -n %bname-gnomevfs
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstgnomevfs.so


### CDPARANOIA ###
%package -n %bname-cdparanoia
Summary: Gstreamer plugin for CD audio input using CDParanoia IV
Group: Sound
Requires: %name = %{version}
BuildRequires: libcdda-devel

%description -n %bname-cdparanoia
Plugin for ripping audio tracks using cdparanoia under GStreamer

%files -n %bname-cdparanoia
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstcdparanoia.so

%if %build_libvisual
%package -n %bname-libvisual
Summary: GStreamer visualisations plug-in based on libvisual
Group: Video
Requires: %name = %{version}
BuildRequires: libvisual-devel >= 0.4

%description -n %bname-libvisual
This plugin makes visualisations based on libvisual available for
GStreamer applications.

%files -n %bname-libvisual
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstlibvisual.so
%endif


