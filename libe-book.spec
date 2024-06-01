%define api 0.1
%define major 1
%define oldlibname %mklibname e-book %{api} %{major}
%define libname %mklibname e-book
%define devname %mklibname e-book -d

Name: libe-book
Version: 0.1.3
Release: 9
Source0: http://netcologne.dl.sourceforge.net/project/libebook/libe-book-%{version}/libe-book-%{version}.tar.xz
Summary: Library for import of reflowable e-book formats
URL: http://libebook.sf.net/
License: MPL 2.0
Group: System/Libraries
Patch0: http://svnweb.mageia.org/packages/cauldron/libe-book/current/SOURCES/libe-book-0.1.3-icu-true.patch
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(icu-io)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblangtag)
BuildRequires: gperf
BuildRequires: doxygen
BuildRequires: boost-devel

%description
Library for import of reflowable e-book formats.

%package -n %{libname}
Summary: Library for import of reflowable e-book formats
Group: System/Libraries
# Renamed after 5.0
%rename %{oldlibname}

%description -n %{libname}
Library for import of reflowable e-book formats.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1

%build
%configure --disable-werror LIBS=-lboost_system
sed -i \
	-e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
	libtool

%make_build

%install
%make_install

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%doc %{_docdir}/%{name}
