#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libuv
Version  : 1.30.1
Release  : 14
URL      : https://github.com/libuv/libuv/archive/v1.30.1/libuv-1.30.1.tar.gz
Source0  : https://github.com/libuv/libuv/archive/v1.30.1/libuv-1.30.1.tar.gz
Summary  : Multi-platform support library with a focus on asynchronous I/O
Group    : Development/Tools
License  : CC-BY-4.0 MIT NCSA
Requires: libuv-lib = %{version}-%{release}
Requires: libuv-license = %{version}-%{release}

%description
## Overview
libuv is a multi-platform support library with a focus on asynchronous I/O. It
was primarily developed for use by [Node.js][], but it's also
used by [Luvit](http://luvit.io/), [Julia](http://julialang.org/),
[pyuv](https://github.com/saghul/pyuv), and [others](https://github.com/libuv/libuv/wiki/Projects-that-use-libuv).

%package dev
Summary: dev components for the libuv package.
Group: Development
Requires: libuv-lib = %{version}-%{release}
Provides: libuv-devel = %{version}-%{release}
Requires: libuv = %{version}-%{release}
Requires: libuv = %{version}-%{release}

%description dev
dev components for the libuv package.


%package lib
Summary: lib components for the libuv package.
Group: Libraries
Requires: libuv-license = %{version}-%{release}

%description lib
lib components for the libuv package.


%package license
Summary: license components for the libuv package.
Group: Default

%description license
license components for the libuv package.


%prep
%setup -q -n libuv-1.30.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562142132
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1562142132
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libuv
cp LICENSE %{buildroot}/usr/share/package-licenses/libuv/LICENSE
cp LICENSE-docs %{buildroot}/usr/share/package-licenses/libuv/LICENSE-docs
cp samples/socks5-proxy/LICENSE %{buildroot}/usr/share/package-licenses/libuv/samples_socks5-proxy_LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/uv/errno.h
/usr/include/uv/linux.h
/usr/include/uv/threadpool.h
/usr/include/uv/unix.h
/usr/include/uv/version.h
/usr/lib64/libuv.so
/usr/lib64/pkgconfig/libuv.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libuv.so.1
/usr/lib64/libuv.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libuv/LICENSE
/usr/share/package-licenses/libuv/LICENSE-docs
/usr/share/package-licenses/libuv/samples_socks5-proxy_LICENSE
