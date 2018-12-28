#
# Conditional build:
%bcond_without	static_libs	# don't build static library

Summary:	Utility functions for NetSurf
Summary(pl.UTF-8):	Biblioteka funkcji narzędziowych dla NetSurfa
Name:		libnsutils
Version:	0.0.5
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
# Source0-md5:	c61e10d35e8917ce72ee19516432437a
URL:		http://www.netsurf-browser.org/projects/libnsutils/
BuildRequires:	netsurf-buildsystem >= 1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libnsutils provides a small number of useful utility routines which
require platform-specific implementations.

%description -l pl.UTF-8
Biblioteka libnsutils dostarcza trochę przydatnych funkcji
narzędziowych, wymagających implementacji zależnych od platformy.

%package devel
Summary:	libnsutils library headers
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnsutils
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the include files and other resources you can
use to incorporate libnsutils into applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe pozwalające na używanie biblioteki libnsutils w
swoich programach.

%package static
Summary:	libnsutils static library
Summary(pl.UTF-8):	Statyczna biblioteka libnsutils
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This is package with static libnsutils library.

%description static -l pl.UTF-8
Statyczna biblioteka libnsutils.

%prep
%setup -q

%build
export AR="%{__ar}"
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"

%{__make} \
	Q= \
	PREFIX=%{_prefix} \
	COMPONENT_TYPE=lib-shared

%if %{with static_libs}
%{__make} \
	Q= \
	PREFIX=%{_prefix} \
	COMPONENT_TYPE=lib-static
%endif

%install
rm -rf $RPM_BUILD_ROOT

export AR="%{__ar}"
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"

%{__make} install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib} \
	COMPONENT_TYPE=lib-shared \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib} \
	COMPONENT_TYPE=lib-static \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/libnsutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnsutils.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnsutils.so
%{_includedir}/nsutils
%{_pkgconfigdir}/libnsutils.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libnsutils.a
%endif
