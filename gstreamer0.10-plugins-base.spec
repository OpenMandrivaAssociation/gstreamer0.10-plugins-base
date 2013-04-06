%define bname gstreamer0.10

%define major 0
%define api 0.10
%define libname %mklibname gstreamer-plugins-base %{api} %{major}
%define rosalib %mklibname gstreamer-plugins-base %{api}
%define develname %mklibname gstreamer-plugins-base %{api} -d
%define girname %mklibname gstreamer-plugins-base-gir %{api}

%define oldlibname  %mklibname gstapp0.10_ 0
%define olddevelname %mklibname -d gstapp0.10_ 0

%define build_libvisual 1
%define build_docs 0
%define build_qtexamples 0
%define enable_check 0

Summary:	GStreamer Streaming-media framework plug-ins
Name:		%{bname}-plugins-base
Version:	0.10.36
Release:	6
License:	LGPLv2+
Group:		Sound
URL:		http://gstreamer.freedesktop.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gst-plugins-base/%{api}/gst-plugins-base-%{version}.tar.xz
Patch0:		align.patch

BuildRequires:	cdda-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-0.10) >= 0.10.36
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(xv)
%if %{build_libvisual}
BuildRequires:	pkgconfig(libvisual-0.4) >= 0.4
%endif
%ifarch %ix86
BuildRequires:	nasm => 0.90
%endif
%ifnarch %arm %mips
BuildRequires:	valgrind
%endif
%if %{build_qtexamples}
BuildRequires:	qt4-devel
%endif
%if %{build_docs}
BuildRequires:	gtk-doc
%endif
%if %{enable_check}
#gw we need some fonts for the tests
BuildRequires:	fonts-ttf-dejavu
%endif

# md legacy provides, do_not remove until everything 
# that requires the provide is cleaned up
Provides:	%{bname}-plugins
Suggests:	gst-install-plugins-helper
Conflicts:	%{bname}-plugins-bad < 0.10.10

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

%package -n %{libname}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%mklibname gstreamer-plugins-base0.10
Obsoletes:	%oldlibname
%rename		%{rosalib}

%description -n %{libname}
This package contain the basic audio and video playback library and
the interfaces library.

%package -n %{girname}
Summary:	GObject Introspection interface libraries for %{name}
Group:		System/Libraries
Conflicts:	%mklibname gstreamer-plugins-base 0.10 < 0.10.35-2
Conflicts:	gir-repository < 0.6.5-3

%description -n %{girname}
GObject Introspection interface libraries for %{name}.

%package -n %{develname}
Summary:	GStreamer Plugin Library Headers
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
%if %{enable_check}
# gw is required at build time for make check
Requires:	%{name} = %{version}-%{release}
%endif
Provides:	libgstreamer-plugins-base-devel = %{version}-%{release}
Provides:	libgstreamer%{api}-plugins-base-devel = %{version}-%{release}
Conflicts:	gir-repository < 0.6.5-3
Obsoletes:	%olddevelname

%description -n %{develname}
GStreamer support libraries header files.

%package -n %{bname}-gnomevfs
Summary:	GStreamer plug-ins for GNOME VFS input and output
Group:		System/Libraries
Requires:	gnome-vfs2 > 1.9.4.00
Requires:	%{name} = %{version}-%{release}

%description -n %{bname}-gnomevfs
Plug-Ins for reading and writing through GNOME VFS.

%package -n %{bname}-cdparanoia
Summary:	Gstreamer plugin for CD audio input using CDParanoia IV
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description -n %{bname}-cdparanoia
Plugin for ripping audio tracks using cdparanoia under GStreamer

%if %{build_libvisual}
%package -n %{bname}-libvisual
Summary:	GStreamer visualisations plug-in based on libvisual
Group:		Video
Requires:	%{name} = %{version}-%{release}

%description -n %{bname}-libvisual
This plugin makes visualisations based on libvisual available for
GStreamer applications.
%endif

%prep
%setup -qn gst-plugins-base-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-experimental \
	--with-package-name='%{vendor} %{name} package' \
	--with-package-origin='%{disturl}' \
	--enable-libvisual

%make

%if %{enable_check}
%check
cd tests/check
#gw check fail with a gconf error in 0.10.21
%make check
%endif

%install
%makeinstall_std

%find_lang gst-plugins-base-%{api}

%files -f gst-plugins-base-%{api}.lang
%doc AUTHORS README NEWS
%{_bindir}/gst-discoverer-%{api}
%{_bindir}/gst-visualise-%{api}
%dir %_datadir/gst-plugins-base
%_datadir/gst-plugins-base/license-translations.dict
%{_mandir}/man1/gst-visualise-%{api}.1*
%{_libdir}/gstreamer-%{api}/libgstffmpegcolorspace.so
# non-core plugins without external dependencies
%{_libdir}/gstreamer-%{api}/libgstapp.so
%{_libdir}/gstreamer-%{api}/libgstaudioconvert.so
%{_libdir}/gstreamer-%{api}/libgstaudiorate.so
%{_libdir}/gstreamer-%{api}/libgstaudioresample.so
%{_libdir}/gstreamer-%{api}/libgstaudiotestsrc.so
%{_libdir}/gstreamer-%{api}/libgstdecodebin.so
%{_libdir}/gstreamer-%{api}/libgstdecodebin2.so
%{_libdir}/gstreamer-%{api}/libgstencodebin.so
%{_libdir}/gstreamer-%{api}/libgstgdp.so
%{_libdir}/gstreamer-%{api}/libgstgio.so
%{_libdir}/gstreamer-%{api}/libgstpango.so
%{_libdir}/gstreamer-%{api}/libgstplaybin.so
%{_libdir}/gstreamer-%{api}/libgstsubparse.so
%{_libdir}/gstreamer-%{api}/libgsttcp.so
%{_libdir}/gstreamer-%{api}/libgstvolume.so
%{_libdir}/gstreamer-%{api}/libgstadder.so
%{_libdir}/gstreamer-%{api}/libgsttypefindfunctions.so
%{_libdir}/gstreamer-%{api}/libgstvideotestsrc.so
%{_libdir}/gstreamer-%{api}/libgsttheora.so
%{_libdir}/gstreamer-%{api}/libgstogg.so
%if %mdkversion < 201100
%{_libdir}/gstreamer-%{api}/libgstvideo4linux.so
%endif
%{_libdir}/gstreamer-%{api}/libgstvideorate.so
%{_libdir}/gstreamer-%{api}/libgstvideoscale.so
%{_libdir}/gstreamer-%{api}/libgstvorbis.so
%{_libdir}/gstreamer-%{api}/libgstximagesink.so
%{_libdir}/gstreamer-%{api}/libgstxvimagesink.so
%{_libdir}/gstreamer-%{api}/libgstalsa.so

%files -n %{libname}
%{_libdir}/libgstaudio-%{api}.so.%{major}*
%{_libdir}/libgstapp-%{api}.so.%{major}*
%{_libdir}/libgstcdda-%{api}.so.%{major}*
%{_libdir}/libgstfft-%{api}.so.%{major}*
%{_libdir}/libgstinterfaces-%{api}.so.%{major}*
%{_libdir}/libgstnetbuffer-%{api}.so.%{major}*
%{_libdir}/libgstpbutils-%{api}.so.%{major}*
%{_libdir}/libgstriff-%{api}.so.%{major}*
%{_libdir}/libgstrtp-%{api}.so.%{major}*
%{_libdir}/libgstrtsp-%{api}.so.%{major}*
%{_libdir}/libgsttag-%{api}.so.%{major}*
%{_libdir}/libgstsdp-%{api}.so.%{major}*
%{_libdir}/libgstvideo-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GstApp-%{api}.typelib
%{_libdir}/girepository-1.0/GstAudio-%{api}.typelib
%{_libdir}/girepository-1.0/GstFft-%{api}.typelib
%{_libdir}/girepository-1.0/GstInterfaces-%{api}.typelib
%{_libdir}/girepository-1.0/GstNetbuffer-%{api}.typelib
%{_libdir}/girepository-1.0/GstPbutils-%{api}.typelib
%{_libdir}/girepository-1.0/GstRiff-%{api}.typelib
%{_libdir}/girepository-1.0/GstRtp-%{api}.typelib
%{_libdir}/girepository-1.0/GstRtsp-%{api}.typelib
%{_libdir}/girepository-1.0/GstSdp-%{api}.typelib
%{_libdir}/girepository-1.0/GstTag-%{api}.typelib
%{_libdir}/girepository-1.0/GstVideo-%{api}.typelib

%files -n %{develname}
%doc docs/libs/html docs/plugins/html
%{_includedir}/gstreamer-%{api}/gst/app/
%{_includedir}/gstreamer-%{api}/gst/audio
%{_includedir}/gstreamer-%{api}/gst/cdda/
%{_includedir}/gstreamer-%{api}/gst/fft
%{_includedir}/gstreamer-%{api}/gst/interfaces
%{_includedir}/gstreamer-%{api}/gst/netbuffer
%{_includedir}/gstreamer-%{api}/gst/pbutils
%{_includedir}/gstreamer-%{api}/gst/riff
%{_includedir}/gstreamer-%{api}/gst/rtsp
%{_includedir}/gstreamer-%{api}/gst/sdp
%{_includedir}/gstreamer-%{api}/gst/tag/
%{_includedir}/gstreamer-%{api}/gst/video/
%{_includedir}/gstreamer-%{api}/gst/floatcast/
%{_includedir}/gstreamer-%{api}/gst/rtp
%{_libdir}/pkgconfig/gstreamer-app-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-audio-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-cdda-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-fft-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-floatcast-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-interfaces-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-netbuffer-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-pbutils-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-base-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-riff-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-rtp-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-rtsp-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-sdp-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-tag-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-video-%{api}.pc
%{_libdir}/libgstaudio-%{api}.so
%{_libdir}/libgstapp-%{api}.so
%{_libdir}/libgstcdda-%{api}.so
%{_libdir}/libgstfft-%{api}.so
%{_libdir}/libgstinterfaces-%{api}.so
%{_libdir}/libgstnetbuffer-%{api}.so
%{_libdir}/libgstpbutils-%{api}.so
%{_libdir}/libgstriff-%{api}.so
%{_libdir}/libgstrtp-%{api}.so
%{_libdir}/libgstrtsp-%{api}.so
%{_libdir}/libgsttag-%{api}.so
%{_libdir}/libgstsdp-%{api}.so
%{_libdir}/libgstvideo-%{api}.so
%{_datadir}/gtk-doc/html/*
%{_datadir}/gir-1.0/GstApp-%{api}.gir
%{_datadir}/gir-1.0/GstAudio-%{api}.gir
%{_datadir}/gir-1.0/GstFft-%{api}.gir
%{_datadir}/gir-1.0/GstInterfaces-%{api}.gir
%{_datadir}/gir-1.0/GstNetbuffer-%{api}.gir
%{_datadir}/gir-1.0/GstPbutils-%{api}.gir
%{_datadir}/gir-1.0/GstRiff-%{api}.gir
%{_datadir}/gir-1.0/GstRtp-%{api}.gir
%{_datadir}/gir-1.0/GstRtsp-%{api}.gir
%{_datadir}/gir-1.0/GstSdp-%{api}.gir
%{_datadir}/gir-1.0/GstTag-%{api}.gir
%{_datadir}/gir-1.0/GstVideo-%{api}.gir

%files -n %{bname}-gnomevfs
%{_libdir}/gstreamer-%{api}/libgstgnomevfs.so

%files -n %{bname}-cdparanoia
%{_libdir}/gstreamer-%{api}/libgstcdparanoia.so

%if %{build_libvisual}
%files -n %{bname}-libvisual
%{_libdir}/gstreamer-%{api}/libgstlibvisual.so
%endif

