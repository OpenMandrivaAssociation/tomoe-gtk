%define version 0.6.0
%define release %mkrel 3

%define major 0
%define libname %mklibname tomoe-gtk %{major}
%define develname %mklibname -d tomoe-gtk

%define tomoe_version 0.6.0

Name:           tomoe-gtk
Summary:        Tomoe-gtk library for handwriting recognition
Version:        %{version}
Release:        %{release}
Group:		System/Internationalization
License:	LGPL
URL:		http://sourceforge.jp/projects/tomoe/
Source0:	tomoe-gtk-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:		gucharmap
BuildRequires:		libtomoe-devel >= %{tomoe_version}
BuildRequires:		gtk+2-devel automake pygtk2.0-devel
BuildRequires:		gucharmap-devel gtk-doc python-gobject-devel

%description
Tomoe-gtk library for handwriting recognition.


%package -n	%{libname}
Summary:	Tomoe-gtk library
Group:		System/Internationalization
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
Tomoe-gtk library.

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n %{develname}
Headers of %{name} for development.

%prep
%setup -q -n tomoe-gtk-%{version}

%build
# force to regenerate configure
./autogen.sh

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove docs for sigscheme (they should be installed by %doc)
rm -rf %{buildroot}%{_datadir}/gtk-doc/

%{find_lang} tomoe-gtk

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -n %{libname} -f tomoe-gtk.lang
%defattr(-,root,root)
%doc COPYING
%doc doc/reference/html/*
%{_libdir}/lib*.so.*
%{_datadir}/tomoe-gtk/*.png

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_includedir}/tomoe/gtk/*.h
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*.pc
