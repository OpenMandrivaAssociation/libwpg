%define api		0.2
%define major	2
%define libname        %mklibname wpg %{api} %{major}
%define develname  %mklibname -d wpg

Summary:	Library for importing and converting Corel WordPerfect(tm) Graphics images
Name:		libwpg
Epoch:		1
Version:	0.2.1
Release:	1
Group:		Office
License:	LGPLv2+
URL:		http://libwpg.sf.net/
Source0:	http://downloads.sourceforge.net/project/libwpg/libwpg/libwpg-%{version}/%{name}-%{version}.tar.xz

BuildRequires: doxygen
BuildRequires: pkgconfig(libwpd-0.9)

%description
libwpg is a library for reading and converting WPG images

%package tools
Summary: Tools to convert WPG images into other formats
Group: Publishing

%description tools
Tools to convert WPG images into other formats.
Currently supported: raw svg

%package -n %{libname}
Summary: Library for importing and converting Corel WordPerfect(tm) Graphics images
Group: System/Libraries

%description -n %{libname}
libwpg is a library for reading and converting WPG images

%package -n %{develname}
Summary: Files for developing with libwpg
Group: Development/C++
Requires: %{libname} = %{EVRD}
Provides: libwpg-devel = %{EVRD}

%description -n %{develname}
Includes and definitions for developing with libwpg.

%package docs
Summary: Documentation of libwpg API
Group: Development/C++

%description docs
Documentation of libwpg API for developing with libwpg

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make 
#LIBS='-lwpd-stream-0.9'

%install
%makeinstall_std

%files tools
%doc ChangeLog README COPYING AUTHORS
%{_bindir}/wpg2*

%files -n %{libname}
%{_libdir}/libwpg-%{api}.so.%{major}*

%files -n %{develname}
%{_libdir}/libwpg*.so
%{_libdir}/pkgconfig/libwpg*.pc
%{_includedir}/*

%files docs
%{_docdir}/libwpg/*


%changelog
* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 1:0.2.0-1mdv2011.0
+ Revision: 662200
- update file list
- new version 0.2.0

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.3-5
+ Revision: 661554
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.3-4mdv2011.0
+ Revision: 602616
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.3-3mdv2010.1
+ Revision: 520948
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:0.1.3-2mdv2010.0
+ Revision: 425878
- rebuild

* Sun Aug 17 2008 Emmanuel Andry <eandry@mandriva.org> 1:0.1.3-1mdv2009.0
+ Revision: 272948
- New version

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 1:0.1.2-1mdv2009.0
+ Revision: 217192
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 06 2008 Funda Wang <fwang@mandriva.org> 1:0.1.2-1mdv2008.1
+ Revision: 145929
- New version 0.1.2

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Wed Aug 29 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1:0.1.0-6mdv2008.0
+ Revision: 74904
- Fix epoch handling.

* Wed Aug 29 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1:0.1.0-5mdv2008.0
+ Revision: 74823
- New upstream: 0.1.0 final.

* Fri Aug 03 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.1.0.cvs20070608-5mdv2008.0
+ Revision: 58635
- Remove the ~ from the version tag.

* Fri Jun 29 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.1.0~cvs20070608-4mdv2008.0
+ Revision: 45882
- Added provides for -devel (64b stuff).

* Tue Jun 26 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.1.0~cvs20070608-3mdv2008.0
+ Revision: 44716
- Fix requires from -devel to lib_name
- Fix package groups.
- Add buildrequires to libwpd-0.8_8-devel.
- Adapted for Mandriva.
- Import libwpg



* Fri Apr 20 2007 Fridrich Strba <fridrich.strba@bluewin.ch>
- Add documentation packaging
- Make doc and stream optional

* Tue Jan 27 2004 Fridrich Strba <fridrich.strba@bluewin.ch>
- Create rpm spec according to the rpm spec of libwpD
- of Rui M. Seabra
