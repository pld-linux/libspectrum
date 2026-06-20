#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	ZX Spectrum emulator file format library
Summary(pl.UTF-8):	Biblioteka do obsługi formatów plików emulatorów ZX Spectrum
Name:		libspectrum
Version:	1.6.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz
# Source0-md5:	0a7922641969cfdcbc88b436d519a069
Patch0:		%{name}-pc.patch
URL:		https://fuse-emulator.sourceforge.net/libspectrum.php
BuildRequires:	audiofile-devel >= 0.2.3
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	bzip2-devel >= 1.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.7
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libspectrum is a library designed to make the input and output of some
ZX Spectrum emulator files slightly easier. It is intended to be
usable on Unix variants, Win32 and Mac OS X.

%description -l pl.UTF-8
libspectrum jest biblioteką zaprojektowaną, by ułatwić zapis i odczyt
plików wykorzystywanych przez emulatory ZX Spectrum. Można jej używać
na różnych wariantach systemu Unix, Win32 i Mac OS X.

%package devel
Summary:	ZX Spectrum emulator file format library - development
Summary(pl.UTF-8):	Część dla programistów używających biblioteki libspectrum
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	audiofile-devel >= 0.2.3
Requires:	bzip2-devel >= 1.0
Requires:	glib2-devel >= 2.0.0
Requires:	libgcrypt-devel >= 1.1.42
Requires:	zlib-devel

%description devel
The libspectrum-devel package contains the header files and
documentation needed to develop applications with libspectrum.

%description devel -l pl.UTF-8
Pakiet libspectrum-devel zawiera pliki nagłówkowe i dokumentację
potrzebne do kompilowania aplikacji korzystających z libspectrum.

%package static
Summary:	ZX Spectrum emulator file format static library
Summary(pl.UTF-8):	Statyczna biblioteka libspectrum
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
The libspectrum-static package contains the static libraries of
libspectrum.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libspectrum.

%prep
%setup -q
%patch -P0 -p1

# don't BR both glib versions
echo 'AC_DEFUN([AM_PATH_GLIB],[$3])' >> acinclude.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libspectrum.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%{_libdir}/libspectrum.so.*.*.*
%ghost %{_libdir}/libspectrum.so.18

%files devel
%defattr(644,root,root,755)
%doc doc/libspectrum.txt
%{_libdir}/libspectrum.so
%{_includedir}/libspectrum.h
%{_mandir}/man3/libspectrum.3*
%{_pkgconfigdir}/libspectrum.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libspectrum.a
%endif
