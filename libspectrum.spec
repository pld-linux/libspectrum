Summary:	ZX Spectrum emulator file format library
Summary(pl):	Biblioteka do obs³ugi formatów plików emulatorów ZX Spectrum
Name:		libspectrum
Version:	0.2.2
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz
# Source0-md5:	30b0e5082b3b9d9f6fc430fd8912c0bd
URL:		http://fuse-emulator.sourceforge.net/libspectrum.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel >= 1.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.7
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libspectrum is a library designed to make the input and output of some
ZX Spectrum emulator files slightly easier. It is intended to be
usable on Unix variants, Win32 and Mac OS X.

%description -l pl
libspectrum jest bibliotek± zaprojektowan±, by u³atwiæ zapis i odczyt
plików wykorzystywanych przez emulatory ZX Spectrum. Mo¿na jej u¿ywaæ
na ró¿nych wariantach systemu Unix, Win32 i Mac OS X.

%package devel
Summary:	ZX Spectrum emulator file format library - development
Summary(pl):	Czê¶æ dla programistów u¿ywaj±cych biblioteki libspectrum
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel >= 1.0
Requires:	glib2-devel >= 2.0.0
Requires:	libgcrypt-devel
Requires:	zlib-devel

%description devel
The libspectrum-devel package contains the header files and documentation
needed to develop applications with libspectrum.

%description devel -l pl
Pakiet libspectrum-devel zawiera pliki nag³ówkowe i dokumentacjê potrzebne
do kompilowania aplikacji korzystaj±cych z libspectrum.

%package static
Summary:	ZX Spectrum emulator file format static library
Summary(pl):	Statyczna biblioteka libspectrum
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
The libspectrum-static package contains the static libraries of libspectrum.

%description static -l pl
Statyczna wersja biblioteki libspectrum.

%prep
%setup -q

# don't BR both glib versions
echo 'AC_DEFUN([AM_PATH_GLIB],[$3])' >> acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_libdir}/libspectrum.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/libspectrum.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libspectrum.la
%{_includedir}/libspectrum.h
%{_mandir}/man3/libspectrum.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
