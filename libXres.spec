#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXres
Version  : 1.0.7
Release  : 5
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXres-1.0.7.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXres-1.0.7.tar.gz
Summary  : X Resource Information Extension Library
Group    : Development/Tools
License  : MIT
Requires: libXres-lib
Requires: libXres-doc
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

%description dev
dev components for the libXres package.


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


%prep
%setup -q -n libXres-1.0.7

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/XRes.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
