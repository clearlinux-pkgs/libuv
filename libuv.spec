#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libuv
Version  : 1.42.0
Release  : 32
URL      : https://github.com/libuv/libuv/archive/v1.42.0/libuv-1.42.0.tar.gz
Source0  : https://github.com/libuv/libuv/archive/v1.42.0/libuv-1.42.0.tar.gz
Summary  : multi-platform support library with a focus on asynchronous I/O.
Group    : Development/Tools
License  : CC-BY-4.0 MIT
Requires: libuv-lib = %{version}-%{release}
Requires: libuv-license = %{version}-%{release}

%description
![libuv][libuv_banner]
## Overview
libuv is a multi-platform support library with a focus on asynchronous I/O. It
was primarily developed for use by [Node.js][], but it's also
used by [Luvit](http://luvit.io/), [Julia](http://julialang.org/),
[pyuv](https://github.com/saghul/pyuv), and [others](https://github.com/libuv/libuv/blob/v1.x/LINKS.md).

%package dev
Summary: dev components for the libuv package.
Group: Development
Requires: libuv-lib = %{version}-%{release}
Provides: libuv-devel = %{version}-%{release}
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
%setup -q -n libuv-1.42.0
cd %{_builddir}/libuv-1.42.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1626794403
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1626794403
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libuv
cp %{_builddir}/libuv-1.42.0/LICENSE %{buildroot}/usr/share/package-licenses/libuv/848f7398f89046426a7ba23cb56cd3c93c030c64
cp %{_builddir}/libuv-1.42.0/LICENSE-docs %{buildroot}/usr/share/package-licenses/libuv/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/uv.h
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
/usr/share/package-licenses/libuv/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb
/usr/share/package-licenses/libuv/848f7398f89046426a7ba23cb56cd3c93c030c64
