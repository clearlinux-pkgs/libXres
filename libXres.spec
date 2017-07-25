#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXres
Version  : 1.0.7
Release  : 9
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXres-1.0.7.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXres-1.0.7.tar.gz
Summary  : X Resource Information Extension Library
Group    : Development/Tools
License  : JSON
Requires: libXres-lib
Requires: libXres-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
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
Requires: libXres-lib
Provides: libXres-devel

%description dev
dev components for the libXres package.


%package dev32
Summary: dev32 components for the libXres package.
Group: Default
Requires: libXres-lib32
Requires: libXres-dev

%description dev32
dev32 components for the libXres package.


%package doc
Summary: doc components for the libXres package.
Group: Documentation

%description doc
doc components for the libXres package.


%package lib
Summary: lib components for the libXres package.
Group: Libraries

%description lib
lib components for the libXres package.


%package lib32
Summary: lib32 components for the libXres package.
Group: Default

%description lib32
lib32 components for the libXres package.


%prep
%setup -q -n libXres-1.0.7
pushd ..
cp -a libXres-1.0.7 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1500993377
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1500993377
rm -rf %{buildroot}
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

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXRes.so
/usr/lib32/pkgconfig/32xres.pc
/usr/lib32/pkgconfig/xres.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXRes.so.1
/usr/lib64/libXRes.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXRes.so.1
/usr/lib32/libXRes.so.1.0.0
