%define rel             4
%define name            libwpg
%define ups_version     0.1.3
%define version         0.1.3
%define release         %mkrel %{rel}
%define api_version     0.1
%define lib_major       1
%define lib_name        %mklibname wpg- %{api_version} %{lib_major}
%define lib_name_devel  %mklibname -d wpg

Name: %{name}
Summary: Library for importing and converting Corel WordPerfect(tm) Graphics images
Epoch: 1
Version: %{version}
Release: %{release}
Group: Office
URL: http://libwpg.sf.net/
Source: http://www.go-ooo.org/packages/SRC680/%{name}-%{ups_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
License: LGPLv2+
BuildRequires: libwpd-devel >= 0.8.8
BuildRequires: doxygen

%description
libwpg is a library for reading and converting WPG images

%package tools
Summary: Tools to convert WPG images into other formats
Group: Publishing

%description tools
Tools to convert WPG images into other formats.
Currently supported: raw svg

%package -n %{lib_name}
Summary: Library for importing and converting Corel WordPerfect(tm) Graphics images
Group: System/Libraries

%description -n %{lib_name}
libwpg is a library for reading and converting WPG images

%package -n %{lib_name_devel}
Summary: Files for developing with libwpg
Group: Development/C++
Requires: %{lib_name}
Requires: libwpd-devel >= 0.8.0
Provides: libwpg-devel = %{epoch}:%{version}-%{release}

%description -n %{lib_name_devel}
Includes and definitions for developing with libwpg.

%package docs
Summary: Documentation of libwpg API
Group: Development/C++

%description docs
Documentation of libwpg API for developing with libwpg

%prep
%setup -q -n %{name}-%{ups_version}

%build
%configure2_5x
%make

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/%{_libdir}/libwpg*.la

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files tools
%defattr(755,root,root,755)
%{_bindir}/wpg2*

%files -n %{lib_name}
%defattr(644,root,root,755)
%doc ChangeLog README COPYING AUTHORS
%{_libdir}/libwpg*.so.*

%files -n %{lib_name_devel}
%defattr(644,root,root,755)
%{_libdir}/libwpg*.so
%{_libdir}/pkgconfig/libwpg*.pc
%{_includedir}/libwpg-0.1/libwpg

%files docs
%defattr(644,root,root,755)
%{_docdir}/libwpg/*
