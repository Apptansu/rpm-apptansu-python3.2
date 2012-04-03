Summary: An interpreted, interactive, object-oriented programming language
Name: apptansu-python3.2
Version: 3.2.3rc2
Release: 1%{?dist}
License: Python
Vendor: Apptansu
Group: Development/Languages
#Provides: TODO
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tgz

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: openssl-devel, gmp-devel
BuildRequires: gdbm-devel, zlib-devel, expat-devel
BuildRequires: gcc-c++ libX11-devel glibc-devel
BuildRequires: bzip2 tar /usr/bin/find pkgconfig
BuildRequires: bzip2-devel sqlite-devel
BuildRequires: db4-devel
BuildRequires: libffi-devel

# Without AutoReq: no, the system python gets picked up as a dependency
# possibly due to it being the first one found when resolving shebangs with
# /usr/bin/env python
AutoReq: no
AutoProv: no

%define _prefix /usr/lib/apptansu
# Don't install libraries to lib64 which is where Red Hat wants to put them
# by default. Doing so requires patching sysconfig.py.
%define _libdir %{_prefix}/lib

%define _hardened_build 1

%description
python3.2 for apptansu

%prep
%setup -q -n Python-%{version}

%build
%configure --enable-ipv6 --with-wide-unicode --with-signal-module

%install
rm -rf %{buildroot}
make altinstall DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/bin
ln -s %{_prefix}/bin/python3.2 %{buildroot}/usr/bin/python3.2-apptansu

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_prefix}/*
/usr/bin/python3.2-apptansu

%changelog
* Sun Feb 05 2012 Apptansu <support@apptansu.com> 3.2.3rc2-1
- Initial packaging.
