%define _glib2 2.15.2
%define major 0.10
%define majorminor 0.10

%define bname gstreamer%{majorminor}

%define libname %mklibname gstreamer-plugins-base %{major}
%define oldlibname %mklibname gstapp0.10_ 0
%define olddevelname %mklibname -d gstapp0.10_ 0
%define gstver 0.10.36
%define build_libvisual 1

Summary:	GStreamer Streaming-media framework plug-ins
Name:		%{bname}-plugins-base
Version:	0.10.36
Release:	3
License:	LGPLv2+
Group:		Sound
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gst-plugins-base/0.10/gst-plugins-base-%{version}.tar.xz
Patch0:		align.patch
URL:		http://gstreamer.freedesktop.org/
Provides:	%{bname}-plugin-libs = %{EVRD}
Obsoletes:	%{bname}-plugin-libs < %{EVRD}
#gw for the pixbuf plugin
BuildRequires:	gtk+2-devel
BuildRequires:	glib2-devel >= %{_glib2}
#gw qt example
BuildRequires:	qt4-devel
BuildRequires:	libpng-devel >= 1.2.4
BuildRequires:	liborc-devel >= 0.4.5
BuildRequires:	libvorbis-devel >= 1.0
BuildRequires:	libtheora-devel
%ifarch %{ix86}
BuildRequires:	nasm => 0.90
%endif
BuildRequires:	libcheck-devel
BuildRequires:	valgrind
BuildRequires:	libgstreamer-devel >= %{gstver}
BuildRequires:	gtk-doc
BuildRequires:	mesaglu-devel
BuildRequires:	libxv-devel
BuildRequires:	libalsa-devel
BuildRequires:	gobject-introspection-devel
#gw we need some fonts for the tests
BuildRequires:	fonts-ttf-dejavu
Provides:	%{bname}-audiosrc
Provides:	%{bname}-audiosink
Provides:	%{bname}-alsa = %{EVRD}
Obsoletes:	%{bname}-alsa < %{EVRD}
Provides:	%{bname}-plugins = %{EVRD}
Obsoletes:	%{bname}-plugins < %{EVRD}
Provides:	%{bname}-vorbis = %{EVRD}
Obsoletes:	%{bname}-vorbis < %{EVRD}
Provides:	%{bname}-x11 = %{EVRD}
Obsoletes:	%{bname}-x11 < %{EVRD}
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
Obsoletes:	%{oldlibname}
Conflicts:	gir-repository < 0.6.5-3

%description -n %{libname}
This package contain the basic audio and video playback library and
the interfaces library.

%files -n %{libname}
%{_libdir}/libgstaudio-%{majorminor}.so.0*
%{_libdir}/libgstapp-%{majorminor}.so.0*
%{_libdir}/libgstcdda-%{majorminor}.so.0*
%{_libdir}/libgstfft-%{majorminor}.so.0*
%{_libdir}/libgstinterfaces-%{majorminor}.so.0*
%{_libdir}/libgstnetbuffer-%{majorminor}.so.0*
%{_libdir}/libgstpbutils-%{majorminor}.so.0*
%{_libdir}/libgstriff-%{majorminor}.so.0*
%{_libdir}/libgstrtp-%{majorminor}.so.0*
%{_libdir}/libgstrtsp-%{majorminor}.so.0*
%{_libdir}/libgsttag-%{majorminor}.so.0*
%{_libdir}/libgstsdp-%{majorminor}.so.0*
%{_libdir}/libgstvideo-%{majorminor}.so.0*
%{_libdir}/girepository-1.0/GstApp-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstAudio-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstFft-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstInterfaces-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstNetbuffer-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstPbutils-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstRiff-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstRtp-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstRtsp-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstSdp-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstTag-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstVideo-%{majorminor}.typelib

%package -n %{libname}-devel
Summary:	GStreamer Plugin Library Headers
Group:		Development/C
Conflicts:	gir-repository < 0.6.5-3
Requires:	%{libname} = %{version}
# gw is required at build time for make check
Requires:	%{name} = %{version}
Requires:	libgstreamer-devel >= %{gstver}
Provides:	libgstreamer-plugins-base-devel = %{version}-%{release}
Provides:	libgstreamer%{majorminor}-plugins-base-devel = %{version}-%{release}
Obsoletes:	%{olddevelname}

%description -n %{libname}-devel
GStreamer support libraries header files.

%files -n %{libname}-devel
%doc docs/libs/html docs/plugins/html
%{_includedir}/gstreamer-%{majorminor}/gst/app/
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
%{_libdir}/pkgconfig/gstreamer-app-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-audio-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-cdda-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-fft-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-floatcast-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-interfaces-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-netbuffer-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-pbutils-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-base-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-riff-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-rtp-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-rtsp-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-sdp-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-tag-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-video-%{majorminor}.pc
%{_libdir}/libgstaudio-%{majorminor}.so
%{_libdir}/libgstapp-%{majorminor}.so
%{_libdir}/libgstcdda-%{majorminor}.so
%{_libdir}/libgstfft-%{majorminor}.so
%{_libdir}/libgstinterfaces-%{majorminor}.so
%{_libdir}/libgstnetbuffer-%{majorminor}.so
%{_libdir}/libgstpbutils-%{majorminor}.so
%{_libdir}/libgstriff-%{majorminor}.so
%{_libdir}/libgstrtp-%{majorminor}.so
%{_libdir}/libgstrtsp-%{majorminor}.so
%{_libdir}/libgsttag-%{majorminor}.so
%{_libdir}/libgstsdp-%{majorminor}.so
%{_libdir}/libgstvideo-%{majorminor}.so
%{_datadir}/gtk-doc/html/*
%{_datadir}/gir-1.0/GstApp-%{majorminor}.gir
%{_datadir}/gir-1.0/GstAudio-%{majorminor}.gir
%{_datadir}/gir-1.0/GstFft-%{majorminor}.gir
%{_datadir}/gir-1.0/GstInterfaces-%{majorminor}.gir
%{_datadir}/gir-1.0/GstNetbuffer-%{majorminor}.gir
%{_datadir}/gir-1.0/GstPbutils-%{majorminor}.gir
%{_datadir}/gir-1.0/GstRiff-%{majorminor}.gir
%{_datadir}/gir-1.0/GstRtp-%{majorminor}.gir
%{_datadir}/gir-1.0/GstRtsp-%{majorminor}.gir
%{_datadir}/gir-1.0/GstSdp-%{majorminor}.gir
%{_datadir}/gir-1.0/GstTag-%{majorminor}.gir
%{_datadir}/gir-1.0/GstVideo-%{majorminor}.gir
###


### GNOME VFS 2 ###
%package -n %{bname}-gnomevfs
Summary:	GStreamer plug-ins for GNOME VFS input and output
Group:		System/Libraries
Requires:	gnome-vfs2 > 1.9.4.00
Requires:	%{bname}-plugins-base = %{version}
BuildRequires:	gnome-vfs2-devel > 1.9.4.00

%description -n %{bname}-gnomevfs
Plug-Ins for reading and writing through GNOME VFS.

%files -n %{bname}-gnomevfs
%{_libdir}/gstreamer-%{majorminor}/libgstgnomevfs.so

### CDPARANOIA ###
%package -n %{bname}-cdparanoia
Summary:	Gstreamer plugin for CD audio input using CDParanoia IV
Group:		Sound
Requires:	%{name} = %{version}
BuildRequires:	libcdda-devel

%description -n %{bname}-cdparanoia
Plugin for ripping audio tracks using cdparanoia under GStreamer

%files -n %{bname}-cdparanoia
%{_libdir}/gstreamer-%{majorminor}/libgstcdparanoia.so

%if %{build_libvisual}
%package -n %{bname}-libvisual
Summary:	GStreamer visualisations plug-in based on libvisual
Group:		Video
Requires:	%{name} = %{version}
BuildRequires:	libvisual-devel >= 0.4

%description -n %{bname}-libvisual
This plugin makes visualisations based on libvisual available for
GStreamer applications.

%files -n %{bname}-libvisual
%{_libdir}/gstreamer-%{majorminor}/libgstlibvisual.so
%endif

%prep
%setup -q -n gst-plugins-base-%{version}
%apply_patches

%build
%configure2_5x --disable-dependency-tracking \
  --enable-experimental \
  --with-package-name='Mandriva %{name} package' \
  --with-package-origin='http://www.mandriva.com/' \
  --enable-libvisual
%make

%check
cd tests/check
#gw check fail with a gconf error in 0.10.21
#make check

%install
%__rm -rf %{buildroot} gst-plugins-base-%{majorminor}.lang
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
%find_lang gst-plugins-base-%{majorminor}
# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
%__rm -f %{buildroot}%{_libdir}/gstreamer-%{majorminor}/*.la
%__rm -f %{buildroot}%{_libdir}/gstreamer-%{majorminor}/*.a
%__rm -f %{buildroot}%{_libdir}/*.a
%__rm -f %{buildroot}%{_libdir}/*.la

%clean
%__rm -rf %{buildroot}

%files -f gst-plugins-base-%{majorminor}.lang
%doc AUTHORS COPYING README NEWS
%{_bindir}/gst-discoverer-%{majorminor}
%{_bindir}/gst-visualise-%{majorminor}
%{_datadir}/gst-plugins-base/license-translations.dict
%{_mandir}/man1/gst-visualise-%{majorminor}.1*
%{_libdir}/gstreamer-%{majorminor}/libgstffmpegcolorspace.so
# non-core plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstapp.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiorate.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioresample.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiotestsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecodebin.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecodebin2.so
%{_libdir}/gstreamer-%{majorminor}/libgstencodebin.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdp.so
%{_libdir}/gstreamer-%{majorminor}/libgstgio.so
%{_libdir}/gstreamer-%{majorminor}/libgstpango.so
%{_libdir}/gstreamer-%{majorminor}/libgstplaybin.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubparse.so
%{_libdir}/gstreamer-%{majorminor}/libgsttcp.so
%{_libdir}/gstreamer-%{majorminor}/libgstvolume.so
%{_libdir}/gstreamer-%{majorminor}/libgstadder.so
%{_libdir}/gstreamer-%{majorminor}/libgsttypefindfunctions.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideotestsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgsttheora.so
%{_libdir}/gstreamer-%{majorminor}/libgstogg.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideorate.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoscale.so
%{_libdir}/gstreamer-%{majorminor}/libgstvorbis.so
%{_libdir}/gstreamer-%{majorminor}/libgstximagesink.so
%{_libdir}/gstreamer-%{majorminor}/libgstxvimagesink.so
%{_libdir}/gstreamer-%{majorminor}/libgstalsa.so

%changelog
* Fri Jun 15 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 0.10.36-1
- New version 0.10.36

* Thu Jun 16 2011 Götz Waschk <waschk@mandriva.org> 0.10.35-1mdv2011.0
+ Revision: 685482
- new version
- xz tarball from gnome

* Sat May 14 2011 Funda Wang <fwang@mandriva.org> 0.10.34-1
+ Revision: 674510
- new version 0.10.34

* Wed May 11 2011 Funda Wang <fwang@mandriva.org> 0.10.33-1
+ Revision: 673390
- v4l1 does not support with latest kernel
- bump br
- update to new version 0.10.33

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sat Jan 22 2011 Götz Waschk <waschk@mandriva.org> 0.10.32-1
+ Revision: 632280
- new version
- drop patch 1
- bump gstreamer dep
- add encodebin

* Fri Dec 17 2010 Götz Waschk <waschk@mandriva.org> 0.10.31-2mdv2011.0
+ Revision: 622530
- fix gir file

* Thu Dec 02 2010 Götz Waschk <waschk@mandriva.org> 0.10.31-1mdv2011.0
+ Revision: 604693
- new version

* Fri Nov 12 2010 Götz Waschk <waschk@mandriva.org> 0.10.30.4-1mdv2011.0
+ Revision: 596489
- new version
- update file list

* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 0.10.30.2-3mdv2011.0
+ Revision: 593627
- suggest common provides rather than hardcode package name

* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 0.10.30.2-2mdv2011.0
+ Revision: 593554
- prefer packagekit rather than codein for codec installation

* Thu Oct 21 2010 Götz Waschk <waschk@mandriva.org> 0.10.30.2-1mdv2011.0
+ Revision: 587159
- new prerelease
- drop patches
- bump gstreamer dep
- add gst-discoverer

* Thu Sep 16 2010 Götz Waschk <waschk@mandriva.org> 0.10.30-3mdv2011.0
+ Revision: 578984
- fix build with new gtk+
- fix tabs in Makefiles

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 0.10.30-2mdv2011.0
+ Revision: 563391
- rebuild for new gobject-introspection

* Thu Jul 15 2010 Götz Waschk <waschk@mandriva.org> 0.10.30-1mdv2011.0
+ Revision: 553737
- new version
- bump gstreamer dep
- replace dep on liboil by orc

* Wed Apr 28 2010 Götz Waschk <waschk@mandriva.org> 0.10.29-1mdv2010.1
+ Revision: 539983
- new version
- bump gstreamer dep

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 0.10.28-1mdv2010.1
+ Revision: 516899
- new version
- drop source 1
- bump gstreamer dep

* Sun Mar 07 2010 Götz Waschk <waschk@mandriva.org> 0.10.27-1mdv2010.1
+ Revision: 515554
- new version
- add missing source file
- bump deps
- update build deps

* Thu Feb 11 2010 Götz Waschk <waschk@mandriva.org> 0.10.26-1mdv2010.1
+ Revision: 504213
- new version
- bump gstreamer dep

* Wed Jan 27 2010 Götz Waschk <waschk@mandriva.org> 0.10.25.2-1mdv2010.1
+ Revision: 497403
- new version
- drop patches
- bump gstreamer dep
- update file list

* Thu Nov 12 2009 Götz Waschk <waschk@mandriva.org> 0.10.25-3mdv2010.1
+ Revision: 465235
- volume setting fixes for bug #55552

* Tue Oct 06 2009 Götz Waschk <waschk@mandriva.org> 0.10.25-2mdv2010.0
+ Revision: 454453
- add conflicts with old gir-repository

* Mon Oct 05 2009 Götz Waschk <waschk@mandriva.org> 0.10.25-1mdv2010.0
+ Revision: 454337
- new version
- bump gstreamer dep
- add introspection support

* Fri Sep 25 2009 Olivier Blin <oblin@mandriva.com> 0.10.24-2mdv2010.0
+ Revision: 449041
- disable valgrind on mips & arm (from Arnaud Patard)
- fix alignment access in fftw stuff for mips (from Arnaud Patard)

* Wed Aug 05 2009 Götz Waschk <waschk@mandriva.org> 0.10.24-1mdv2010.0
+ Revision: 409950
- new version
- bump gstreamer dep

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 0.10.23-1mdv2010.0
+ Revision: 374127
- new version
- drop patch

* Fri Apr 03 2009 Götz Waschk <waschk@mandriva.org> 0.10.22-3mdv2009.1
+ Revision: 363701
- really apply the patch
- BS bump

  + Rafael da Veiga Cabral <cabral@mandriva.com>
    - security fix for CVE-2009-0586

* Tue Jan 20 2009 Götz Waschk <waschk@mandriva.org> 0.10.22-1mdv2009.1
+ Revision: 331724
- new version
- add libgstapp

* Sat Oct 11 2008 Götz Waschk <waschk@mandriva.org> 0.10.21-1mdv2009.1
+ Revision: 292258
- new version
- bump deps
- drop patch
- disable checks

* Thu Aug 07 2008 Frederic Crozat <fcrozat@mandriva.com> 0.10.20-2mdv2009.0
+ Revision: 266432
- Remove patch1 (no longer used)
- Patch0: ensure translated text is encoded in UTF-8 (GNOME bug #546822)

* Thu Jun 19 2008 Götz Waschk <waschk@mandriva.org> 0.10.20-1mdv2009.0
+ Revision: 226204
- new version
- bump deps
- disable ppc patch

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 09 2008 Götz Waschk <waschk@mandriva.org> 0.10.19-2mdv2009.0
+ Revision: 204940
- enable experimental gio element (requested by Eelco Bosselaar)
- bump glib2 dep

* Tue Apr 08 2008 Götz Waschk <waschk@mandriva.org> 0.10.19-1mdv2009.0
+ Revision: 192415
- new version
- bump deps

* Thu Mar 13 2008 Götz Waschk <waschk@mandriva.org> 0.10.17-3mdv2008.1
+ Revision: 187336
- add Mandriva branding

* Wed Mar 12 2008 Frederic Crozat <fcrozat@mandriva.com> 0.10.17-2mdv2008.1
+ Revision: 187220
- Suggests codeina and configure gstreamer to use it as codec installer helper

* Wed Jan 30 2008 Götz Waschk <waschk@mandriva.org> 0.10.17-1mdv2008.1
+ Revision: 160275
- new version

* Tue Jan 29 2008 Götz Waschk <waschk@mandriva.org> 0.10.16-1mdv2008.1
+ Revision: 160019
- update file list
- new version
- bump deps
- drop patch 0
- add build conflict with old version

* Wed Jan 16 2008 Götz Waschk <waschk@mandriva.org> 0.10.15-2mdv2008.1
+ Revision: 153614
- patch to fix theora element with our libtheora version
- add missing make call
- update file list

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix mesaglu-devel BR
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Jérôme Soyer <saispo@mandriva.org>
    - New release

* Fri Aug 03 2007 Götz Waschk <waschk@mandriva.org> 0.10.14-1mdv2008.0
+ Revision: 58653
- new version
- bump deps
- update file list

* Thu Jun 07 2007 Götz Waschk <waschk@mandriva.org> 0.10.13-1mdv2008.0
+ Revision: 36515
- new version
- bump deps
- update file list


* Mon Mar 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.10.12-2mdv2007.1
+ Revision: 146602
- move devel doc in -devel

* Thu Mar 08 2007 Götz Waschk <waschk@mandriva.org> 0.10.12-1mdv2007.1
+ Revision: 138474
- fix buildrequires
- new version
- update file list
- bump deps
- the devel package requires the main package
- add docs

* Sun Dec 10 2006 Christiaan Welvaart <spturtle@mandriva.org> 0.10.11-2mdv2007.1
+ Revision: 94487
- patch1: fix tests on ppc

* Thu Dec 07 2006 Götz Waschk <waschk@mandriva.org> 0.10.11-1mdv2007.1
+ Revision: 92014
- new version
- bump deps
- update file list
- enable checks
- Import gstreamer0.10-plugins-base

* Mon Oct 09 2006 Götz Waschk <waschk@mandriva.org> 0.10.10-1mdv2007.1
- update file list
- bump deps
- New version 0.10.10

* Tue Aug 15 2006 Götz Waschk <waschk@mandriva.org> 0.10.9-1mdv2007.0
- New release 0.10.9

* Thu Aug 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.10.8-3mdv2007.0
- fix buildrequires for x86_64

* Wed Jul 19 2006 Jerome Martin <jmartin@mandriva.org> 0.10.8-2mdv2007.0
- fix buildrequires for backport
- fix liboil buildrequire version

* Sun Jun 11 2006 Götz Waschk <waschk@mandriva.org> 0.10.8-1mdv2007.0
- reenable libvisual
- bump deps
- New release 0.10.8

* Thu Jun 08 2006 Götz Waschk <waschk@mandriva.org> 0.10.7-3mdv2007.0
- fix buildrequires

* Fri Jun 02 2006 Götz Waschk <waschk@mandriva.org> 0.10.7-2mdv2007.0
- disable libvisual
- fix buildrequires for new X

* Mon May 15 2006 Götz Waschk <waschk@mandriva.org> 0.10.7-1mdk
- bump deps
- New release 0.10.7

* Sun Apr 30 2006 Götz Waschk <waschk@mandriva.org> 0.10.6-1mdk
- bump deps
- New release 0.10.6

* Tue Mar 14 2006 Götz Waschk <waschk@mandriva.org> 0.10.5-2mdk
- fix devel deps

* Tue Mar 14 2006 Götz Waschk <waschk@mandriva.org> 0.10.5-1mdk
- fix buildrequires
- New release 0.10.5

* Mon Feb 13 2006 Götz Waschk <waschk@mandriva.org> 0.10.3-1mdk
- New release 0.10.3

* Tue Jan 17 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdk
- add cdparanoia plugin
- New release 0.10.2

* Thu Dec 29 2005 Götz Waschk <waschk@mandriva.org> 0.10.1-2mdk
- fix buildrequires

* Wed Dec 28 2005 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdk
- update file list
- improve description
- New release 0.10.1

* Tue Dec 06 2005 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdk
- initial package

