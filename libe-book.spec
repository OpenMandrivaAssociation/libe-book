%define api 0.1
%define major 1
%define libname %mklibname e-book %{api} %{major}
%define devname %mklibname e-book -d

Name: libe-book
Version: 0.1.1
Release: 4
Source0: http://netcologne.dl.sourceforge.net/project/libebook/libe-book-%{version}/libe-book-%{version}.tar.xz
Summary: Library for import of reflowable e-book formats
URL: http://libebook.sf.net/
License: MPL 2.0
Group: System/Libraries
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(icu-io)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(zlib)
BuildRequires: gperf
BuildRequires: doxygen
BuildRequires: boost-devel

%description
Library for import of reflowable e-book formats

%package -n %{libname}
Summary: Library for import of reflowable e-book formats
Group: System/Libraries

%description -n %{libname}
Library for import of reflowable e-book formats

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
aclocal -I m4
autoheader
automake -a
autoconf
%configure --disable-werror

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%doc %{_docdir}/%{name}
