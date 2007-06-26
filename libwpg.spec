%define name libwpg
%define version 0.1.0~cvs20070608
%define RELEASE 1
%define release     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}

Name: %{name}
Summary: Library for importing and converting Corel WordPerfect(tm) Graphics images
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.gz
Group: System Environment/Libraries
URL: http://libwpg.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
License: LGPL

%description
libwpg is a library for reading and converting WPG images

%if %{!?_without_stream:1}%{?_without_stream:0}
%package tools
Requires: libwpg
Summary: Tools to convert WPG images into other formats
Group: Applications/Publishing

%description tools
Tools to convert WPG images into other formats.
Currently supported: raw svg
%endif

%package devel
Requires: libwpg
Requires: libwpd-devel >= 0.8.0
Summary: Files for developing with libwpg.
Group: Development/Libraries

%description devel
Includes and definitions for developing with libwpg.

%if %{!?_without_docs:1}%{?_without_docs:0}
%package docs
Requires: libwpg
BuildRequires: doxygen
Summary: Documentation of libwpg API
Group: Development/Documentation

%description docs
Documentation of libwpg API for developing with libwpg
%endif

%prep
%__rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}-%{version}

%build
%configure --prefix=%{_prefix} --libdir=%{_libdir} \
        %{?_with_debug:--enable-debug}  \

%__make

%install
umask 022

%__make DESTDIR=$RPM_BUILD_ROOT install
%__rm -rf $RPM_BUILD_ROOT/%{_libdir}/libwpg*.la

%clean
%__rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name}

%files
%defattr(644,root,root,755)
%{_libdir}/libwpg*.so.*
%doc ChangeLog README COPYING AUTHORS

%files tools
%defattr(755,root,root,755)
%{_bindir}/wpg2*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libwpg*.so
%{_libdir}/pkgconfig/libwpg*.pc
%{_includedir}/libwpg-0.1/libwpg

%if %{!?_without_docs:1}%{?_without_docs:0}
%files docs
%{_datadir}/doc/libwpg-0.1.0~cvs20070608/*
%endif
