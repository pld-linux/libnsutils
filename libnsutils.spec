#
# Conditional build:
%bcond_without	static_libs	# don't build static library

Summary:	Utils functions for netsurf
Summary(pl.UTF-8):	Biblioteka pomocnicza dla netsurfa
Name:		libnsutils
Version:	0.0.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
# Source0-md5:	2782ab67e722f6f61ba263f9ef5b858c
URL:		http://www.netsurf-browser.org/projects/libnsutils/
BuildRequires:	netsurf-buildsystem >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnsutils.

%description -l pl.UTF-8
libnsutils.

%package devel
Summary:	libnsutils library headers
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnsutils
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the include files and other resources you can
use to incorporate libnsutils into applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe pozwalające na używanie biblioteki libnsutils w swoich
programach.

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
%doc COPYING
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
