%define api	0.2
%define major	2
%define libname	%mklibname wpg %{api} %{major}
%define devname	%mklibname -d wpg

Summary:	Library for importing and converting Corel WordPerfect(tm) Graphics images
Name:		libwpg
Epoch:		1
Version:	0.2.1
Release:	3
Group:		Office
License:	LGPLv2+
Url:		http://libwpg.sf.net/
Source0:	http://downloads.sourceforge.net/project/libwpg/libwpg/libwpg-%{version}/%{name}-%{version}.tar.xz

BuildRequires:	doxygen
BuildRequires:	pkgconfig(libwpd-0.9)

%description
libwpg is a library for reading and converting WPG images

%package tools
Summary:	Tools to convert WPG images into other formats
Group:		Publishing

%description tools
Tools to convert WPG images into other formats.
Currently supported: raw svg

%package -n %{libname}
Summary:	Library for importing and converting Corel WordPerfect(tm) Graphics images
Group:		System/Libraries

%description -n %{libname}
libwpg is a library for reading and converting WPG images

%package -n %{devname}
Summary:	Files for developing with libwpg
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	libwpg-devel = %{EVRD}

%description -n %{devname}
Includes and definitions for developing with libwpg.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make 

%install
%makeinstall_std

%files tools
%doc ChangeLog README COPYING AUTHORS
%{_bindir}/wpg2*

%files -n %{libname}
%{_libdir}/libwpg-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/libwpg*.so
%{_libdir}/pkgconfig/libwpg*.pc
%{_includedir}/*
%doc %{_docdir}/libwpg/*

