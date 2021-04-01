#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDB221A6900000011 (keithp@debian.org)
#
Name     : libXres
Version  : 1.2.1
Release  : 17
URL      : https://www.x.org/releases/individual/lib/libXres-1.2.1.tar.gz
Source0  : https://www.x.org/releases/individual/lib/libXres-1.2.1.tar.gz
Source1  : https://www.x.org/releases/individual/lib/libXres-1.2.1.tar.gz.sig
Summary  : X Resource Information Extension Library
Group    : Development/Tools
License  : JSON
Requires: libXres-lib = %{version}-%{release}
Requires: libXres-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32resourceproto)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xextproto)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(resourceproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)

%description
libXRes - X-Resource extension client library
All questions regarding this software should be directed at the
Xorg mailing list:

%package dev
Summary: dev components for the libXres package.
Group: Development
Requires: libXres-lib = %{version}-%{release}
Provides: libXres-devel = %{version}-%{release}
Requires: libXres = %{version}-%{release}

%description dev
dev components for the libXres package.


%package dev32
Summary: dev32 components for the libXres package.
Group: Default
Requires: libXres-lib32 = %{version}-%{release}
Requires: libXres-dev = %{version}-%{release}

%description dev32
dev32 components for the libXres package.


%package lib
Summary: lib components for the libXres package.
Group: Libraries
Requires: libXres-license = %{version}-%{release}

%description lib
lib components for the libXres package.


%package lib32
Summary: lib32 components for the libXres package.
Group: Default
Requires: libXres-license = %{version}-%{release}

%description lib32
lib32 components for the libXres package.


%package license
Summary: license components for the libXres package.
Group: Default

%description license
license components for the libXres package.


%prep
%setup -q -n libXres-1.2.1
cd %{_builddir}/libXres-1.2.1
pushd ..
cp -a libXres-1.2.1 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617298771
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1617298771
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libXres
cp %{_builddir}/libXres-1.2.1/COPYING %{buildroot}/usr/share/package-licenses/libXres/b307e9607ffa7ab6dc4ab7c019d0e62a627b9532
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/XRes.h
/usr/lib64/libXRes.so
/usr/lib64/pkgconfig/xres.pc
/usr/share/man/man3/XRes.3
/usr/share/man/man3/XResQueryClientPixmapBytes.3
/usr/share/man/man3/XResQueryClientResources.3
/usr/share/man/man3/XResQueryClients.3
/usr/share/man/man3/XResQueryExtension.3
/usr/share/man/man3/XResQueryVersion.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXRes.so
/usr/lib32/pkgconfig/32xres.pc
/usr/lib32/pkgconfig/xres.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXRes.so.1
/usr/lib64/libXRes.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXRes.so.1
/usr/lib32/libXRes.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libXres/b307e9607ffa7ab6dc4ab7c019d0e62a627b9532
