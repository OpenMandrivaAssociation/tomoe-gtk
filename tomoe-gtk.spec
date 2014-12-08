%define debug_package %{nil}

%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}

Name:		tomoe-gtk
Summary:	Tomoe-gtk for handwriting recognition
Version:	0.6.0
Release:	21
Group:		System/Internationalization
License:	LGPLv2+
Url:		http://tomoe.sourceforge.jp/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/tomoe/%{name}-%{version}.tar.gz
Patch0:	tomoe-gtk-0.6.0-underlink.patch
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(tomoe) >= 0.6.0

%description
Tomoe-gtk handwriting recognition.

%package	python
Summary:	Python binding of Tomoe-gtk
Group:		System/Internationalization
Requires:	%{libname} = %{version}-%{release}

%description	python
Python binding of Tomoe-gtk.

%package -n	%{libname}
Summary:	Tomoe-gtk library
Group:		System/Internationalization

%description -n %{libname}
Tomoe-gtk library.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers of %{name} for development.

%prep
%setup -q
%apply_patches
./autogen.sh

%build
export PYTHON=%{__python2}
%configure \
	--disable-static \
	--without-gucharmap
%make

%install
%makeinstall_std

# remove docs for sigscheme (they should be installed by %doc)
rm -rf %{buildroot}%{_datadir}/gtk-doc/

%{find_lang} %{name}

%files -n %{libname} -f %{name}.lang
%{_libdir}/lib*.so.*
%{_datadir}/tomoe-gtk/*.png

%files -n %{devname}
%doc AUTHORS ChangeLog README TODO
%doc doc/reference/html/*
%{_includedir}/tomoe/gtk/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files python
%{python2_sitearch}/gtk-2.0/*.so

