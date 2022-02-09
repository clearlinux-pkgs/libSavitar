#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libSavitar
Version  : 4.13.1
Release  : 38
URL      : https://github.com/Ultimaker/libSavitar/archive/4.13.1/libSavitar-4.13.1.tar.gz
Source0  : https://github.com/Ultimaker/libSavitar/archive/4.13.1/libSavitar-4.13.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0
Requires: libSavitar-lib = %{version}-%{release}
Requires: libSavitar-license = %{version}-%{release}
Requires: libSavitar-python = %{version}-%{release}
Requires: libSavitar-python3 = %{version}-%{release}
Requires: pugixml
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : pugixml-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : sip-bin
BuildRequires : sip-dev
BuildRequires : sip-python3

%description
Introduction
------------
libSavitar is a c++ implementation of 3mf loading with SIP python bindings.

%package dev
Summary: dev components for the libSavitar package.
Group: Development
Requires: libSavitar-lib = %{version}-%{release}
Provides: libSavitar-devel = %{version}-%{release}
Requires: libSavitar = %{version}-%{release}

%description dev
dev components for the libSavitar package.


%package lib
Summary: lib components for the libSavitar package.
Group: Libraries
Requires: libSavitar-license = %{version}-%{release}

%description lib
lib components for the libSavitar package.


%package license
Summary: license components for the libSavitar package.
Group: Default

%description license
license components for the libSavitar package.


%package python
Summary: python components for the libSavitar package.
Group: Default
Requires: libSavitar-python3 = %{version}-%{release}
Provides: libsavitar-python

%description python
python components for the libSavitar package.


%package python3
Summary: python3 components for the libSavitar package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libSavitar package.


%prep
%setup -q -n libSavitar-4.13.1
cd %{_builddir}/libSavitar-4.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644433858
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1644433858
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libSavitar
cp %{_builddir}/libSavitar-4.13.1/LICENSE %{buildroot}/usr/share/package-licenses/libSavitar/f98c7fffc3fe221e79fa19fe89c74e74c0da1266
cp %{_builddir}/libSavitar-4.13.1/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libSavitar/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/include/pugiconfig.hpp
rm -f %{buildroot}*/usr/include/pugixml.hpp
rm -f %{buildroot}*/usr/lib64/cmake/pugixml/pugixml-config-relwithdebinfo.cmake
rm -f %{buildroot}*/usr/lib64/cmake/pugixml/pugixml-config.cmake
## install_append content
# Don't replace system pugixml
rm -f %{buildroot}/usr/lib64/libpugixml.so*
rm -f %{buildroot}/usr/lib64/haswell/libpugixml.so*
rm -f %{buildroot}/usr/lib64/haswell/avx512_1/libpugixml.so*
## install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/Savitar/Face.h
/usr/include/Savitar/MeshData.h
/usr/include/Savitar/Namespace.h
/usr/include/Savitar/SavitarExport.h
/usr/include/Savitar/Scene.h
/usr/include/Savitar/SceneNode.h
/usr/include/Savitar/ThreeMFParser.h
/usr/include/Savitar/Types.h
/usr/include/Savitar/Vertex.h
/usr/lib64/cmake/Savitar/Savitar-targets-relwithdebinfo.cmake
/usr/lib64/cmake/Savitar/Savitar-targets.cmake
/usr/lib64/cmake/Savitar/SavitarConfig.cmake
/usr/lib64/cmake/Savitar/SavitarConfigVersion.cmake
/usr/lib64/libSavitar.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSavitar.so.0
/usr/lib64/libSavitar.so.0.1.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libSavitar/f98c7fffc3fe221e79fa19fe89c74e74c0da1266
/usr/share/package-licenses/libSavitar/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
