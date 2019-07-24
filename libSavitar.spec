#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libSavitar
Version  : 4.1.0
Release  : 5
URL      : https://github.com/Ultimaker/libSavitar/archive/4.1.0/libSavitar-4.1.0.tar.gz
Source0  : https://github.com/Ultimaker/libSavitar/archive/4.1.0/libSavitar-4.1.0.tar.gz
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
BuildRequires : pugixml
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
%setup -q -n libSavitar-4.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563998643
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1563998643
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libSavitar
cp LICENSE %{buildroot}/usr/share/package-licenses/libSavitar/LICENSE
cp cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libSavitar/cmake_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd
## install_append content
rm -f %{buildroot}/usr/lib64/libpugixml.so*
rm -f %{buildroot}/usr/lib64/haswell/libpugixml.so*
rm -f %{buildroot}/usr/lib64/haswell/avx512_1/libpugixml.so*
## install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/pugiconfig.hpp
%exclude /usr/include/pugixml.hpp
%exclude /usr/lib64/cmake/pugixml/pugixml-config-relwithdebinfo.cmake
%exclude /usr/lib64/cmake/pugixml/pugixml-config.cmake
/usr/include/Savitar/Face.h
/usr/include/Savitar/MeshData.h
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
/usr/lib64/libSavitar.so.0.1.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libSavitar/LICENSE
/usr/share/package-licenses/libSavitar/cmake_COPYING-CMAKE-SCRIPTS

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
