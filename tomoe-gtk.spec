%define version 0.6.0
%define release %mkrel 5

%define major 0
%define libname_orig lib%{name}
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

%define tomoe_version 0.6.0

Name:           tomoe-gtk
Summary:        Tomoe-gtk for handwriting recognition
Version:        %{version}
Release:        %{release}
Group:		System/Internationalization
License:	LGPL
URL:		http://sourceforge.jp/projects/tomoe/
Source0:	tomoe-gtk-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:		gucharmap
Requires:		%{libname} = %{version}-%{release}
BuildRequires:		libtomoe-devel >= %{tomoe_version}
BuildRequires:          tomoe >= %{tomoe_version}
BuildRequires:		gtk+2-devel automake pygtk2.0-devel
BuildRequires:		gucharmap-devel gtk-doc python-gobject-devel

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
Provides:	%{libname_orig} = %{version}-%{release}

%description -n %{libname}
Tomoe-gtk library.

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n %{develname}
Headers of %{name} for development.

%prep
%setup -q

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

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README TODO
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
%{python_sitearch}/gtk-2.0/*.a
%{python_sitearch}/gtk-2.0/*.la
%{_libdir}/pkgconfig/*.pc

%files python
%defattr(-,root,root)
%doc COPYING
%{python_sitearch}/gtk-2.0/*.so
