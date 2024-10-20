#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
%define keepstatic 1
Name     : libuv
Version  : 1.49.2
Release  : 46
URL      : https://github.com/libuv/libuv/archive/v1.49.2/libuv-1.49.2.tar.gz
Source0  : https://github.com/libuv/libuv/archive/v1.49.2/libuv-1.49.2.tar.gz
Summary  : multi-platform support library with a focus on asynchronous I/O.
Group    : Development/Tools
License  : CC-BY-4.0 MIT
Requires: libuv-lib = %{version}-%{release}
Requires: libuv-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
![libuv][libuv_banner]
## Overview
libuv is a multi-platform support library with a focus on asynchronous I/O. It
was primarily developed for use by [Node.js][], but it's also
used by [Luvit](http://luvit.io/), [Julia](http://julialang.org/),
[uvloop](https://github.com/MagicStack/uvloop), and [others](https://github.com/libuv/libuv/blob/v1.x/LINKS.md).

%package dev
Summary: dev components for the libuv package.
Group: Development
Requires: libuv-lib = %{version}-%{release}
Provides: libuv-devel = %{version}-%{release}
Requires: libuv = %{version}-%{release}

%description dev
dev components for the libuv package.


%package doc
Summary: doc components for the libuv package.
Group: Documentation

%description doc
doc components for the libuv package.


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


%package staticdev
Summary: staticdev components for the libuv package.
Group: Default
Requires: libuv-dev = %{version}-%{release}

%description staticdev
staticdev components for the libuv package.


%prep
%setup -q -n libuv-1.49.2
cd %{_builddir}/libuv-1.49.2
pushd ..
cp -a libuv-1.49.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1729452753
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1729452753
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libuv
cp %{_builddir}/libuv-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libuv/0b475e38bd94d37bcfbfc28ea7fc024bd80a280a || :
cp %{_builddir}/libuv-%{version}/LICENSE-docs %{buildroot}/usr/share/package-licenses/libuv/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb || :
cp %{_builddir}/libuv-%{version}/LICENSE-extra %{buildroot}/usr/share/package-licenses/libuv/7db2a53252ca3d44462e8b3c050c97742d726850 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/pkgconfig/libuv-static.pc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/uv.h
/usr/include/uv/aix.h
/usr/include/uv/bsd.h
/usr/include/uv/darwin.h
/usr/include/uv/errno.h
/usr/include/uv/linux.h
/usr/include/uv/os390.h
/usr/include/uv/posix.h
/usr/include/uv/sunos.h
/usr/include/uv/threadpool.h
/usr/include/uv/tree.h
/usr/include/uv/unix.h
/usr/include/uv/version.h
/usr/include/uv/win.h
/usr/lib64/cmake/libuv/libuvConfig-relwithdebinfo.cmake
/usr/lib64/cmake/libuv/libuvConfig.cmake
/usr/lib64/libuv.so
/usr/lib64/pkgconfig/libuv.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/libuv/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libuv.so.1.0.0
/usr/lib64/libuv.so.1
/usr/lib64/libuv.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libuv/0b475e38bd94d37bcfbfc28ea7fc024bd80a280a
/usr/share/package-licenses/libuv/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb
/usr/share/package-licenses/libuv/7db2a53252ca3d44462e8b3c050c97742d726850

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libuv.a
