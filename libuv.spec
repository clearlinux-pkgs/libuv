#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
#
Name     : libuv
Version  : 1.45.0
Release  : 38
URL      : https://github.com/libuv/libuv/archive/v1.45.0/libuv-1.45.0.tar.gz
Source0  : https://github.com/libuv/libuv/archive/v1.45.0/libuv-1.45.0.tar.gz
Summary  : multi-platform support library with a focus on asynchronous I/O.
Group    : Development/Tools
License  : CC-BY-4.0 MIT
Requires: libuv-lib = %{version}-%{release}
Requires: libuv-license = %{version}-%{release}
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
%setup -q -n libuv-1.45.0
cd %{_builddir}/libuv-1.45.0
pushd ..
cp -a libuv-1.45.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685635714
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%autogen --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1685635714
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libuv
cp %{_builddir}/libuv-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libuv/0b475e38bd94d37bcfbfc28ea7fc024bd80a280a || :
cp %{_builddir}/libuv-%{version}/LICENSE-docs %{buildroot}/usr/share/package-licenses/libuv/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb || :
cp %{_builddir}/libuv-%{version}/LICENSE-extra %{buildroot}/usr/share/package-licenses/libuv/7db2a53252ca3d44462e8b3c050c97742d726850 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/lib64/libuv.so.1.0.0
/usr/lib64/libuv.so.1
/usr/lib64/libuv.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libuv/0b475e38bd94d37bcfbfc28ea7fc024bd80a280a
/usr/share/package-licenses/libuv/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb
/usr/share/package-licenses/libuv/7db2a53252ca3d44462e8b3c050c97742d726850
