%define major 0
%define libname_orig	lib%{name}
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname -d %{name}

%define tomoe_version 0.6.0

Name:           tomoe-gtk
Summary:        Tomoe-gtk for handwriting recognition
Version:        0.6.0
Release:        %{mkrel 9}
Group:		System/Internationalization
License:	LGPLv2+
URL:		http://tomoe.sourceforge.jp/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/tomoe/%{name}-%{version}.tar.gz
Patch0:		tomoe-gtk-0.6.0-underlink.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	tomoe-devel >= %{tomoe_version}
BuildRequires:	tomoe >= %{tomoe_version}
BuildRequires:	gtk+2-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	gtk-doc
BuildRequires:	python-gobject-devel

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
%patch0 -p1 -b .underlink

%build
# force to regenerate configure
./autogen.sh

%configure2_5x --without-gucharmap
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove docs for sigscheme (they should be installed by %doc)
rm -rf %{buildroot}%{_datadir}/gtk-doc/

%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/lib*.so.*
%{_datadir}/tomoe-gtk/*.png

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%doc doc/reference/html/*
%{_includedir}/tomoe/gtk/*.h
%{_libdir}/lib*.so
%{_libdir}/lib*.*a
%{python_sitearch}/gtk-2.0/*.*a
%{_libdir}/pkgconfig/*.pc

%files python
%defattr(-,root,root)
%{python_sitearch}/gtk-2.0/*.so

