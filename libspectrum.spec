Summary:	ZX Spectrum emulator file format library
Summary(pl):	Biblioteka do obs³ugi formatów plików emulatorów ZX Spectrum
Name:		libspectrum
Version:	0.1.0
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://www.srcf.ucam.org/~pak21/spectrum/%{name}-%{version}.tar.gz
URL:		http://www.srcf.ucam.org/~pak21/spectrum/libspectrum.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
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
Summary(pl):	Czê¶æ dla programistów biblioteki libspectrum
Group:		Development/Libraries
Requires:	%{name} = %{version}

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
Requires:	%{name}-devel = %{version}

%description static
The libspectrum-static package contains the static libraries of libspectrum.

%description static -l pl
Statyczna wersja biblioteki libspectrum.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
ln -sf libspectrum.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/libspectrum.so

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspectrum.so.*

%files devel
%defattr(644,root,root,755)
%doc doc/* AUTHORS ChangeLog README THANKS 
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libspectrum.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
