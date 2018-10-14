Name:		xcb-util-errors
Version:	1.0
Release:	1%{?dist}
Summary:	XCB errors library
Group:		System Environment/Libraries
License:	MIT
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:	pkgconfig(xcb) >= 1.4
BuildRequires:	pkgconfig(xcb-proto)
BuildRequires:	m4

%description
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- errors: utility library that gives human readable names to error
  codes and event codes and also to major and minor numbers

%package 	devel
Summary:	Development and header files for xcb-util-errors
Group:		System Environment/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Development files for xcb-util-errors.

%prep
%setup -q

%build
%configure --with-pic --disable-static --disable-silent-rules
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm %{buildroot}%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%if 0%{?_licensedir:1}
%license COPYING
%else
%doc COPYING
%endif # licensedir
%{_libdir}/*.so.*

%files devel
%doc NEWS
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h

%changelog
* Thu Oct 11 2018 Rodrigo Lourenço <guigo.lourenco@gmail.com> - 1.0-1
- New package.

