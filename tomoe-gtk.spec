%define major 0
%define libname_orig	lib%{name}
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname -d %{name}

%define tomoe_version 0.6.0

Name:           tomoe-gtk
Summary:        Tomoe-gtk for handwriting recognition
Version:        0.6.0
Release:        %mkrel 13
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



%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-12mdv2011.0
+ Revision: 670717
- mass rebuild

* Mon Nov 01 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.0-11mdv2011.0
+ Revision: 591585
- rebuild for python 2.7

* Sun Oct 04 2009 Funda Wang <fwang@mandriva.org> 0.6.0-10mdv2010.0
+ Revision: 453274
- rebuild

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 0.6.0-9mdv2009.1
+ Revision: 319855
- let python moudle link with libpython

* Thu Dec 18 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.0-8mdv2009.1
+ Revision: 315489
- rebuild
- add underlink.patch: fix underlinking
- some cleanups, drop unnecessary provides and defines

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 30 2008 Funda Wang <fwang@mandriva.org> 0.6.0-7mdv2008.1
+ Revision: 160126
- Build without gucharmap as it does not like latest libgucharmap
- rebuild against latest gucharmap

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 06 2007 Funda Wang <fwang@mandriva.org> 0.6.0-5mdv2008.0
+ Revision: 59413
- fix requires of python subpackage

* Fri Aug 03 2007 Adam Williamson <awilliamson@mandriva.org> 0.6.0-4mdv2008.0
+ Revision: 58693
- patch from Utumi Hirosi to fix #32264 (incorrect Provides)

* Wed Jul 04 2007 Funda Wang <fwang@mandriva.org> 0.6.0-3mdv2008.0
+ Revision: 48131
- Merge UTUMI Hirosi's python package
- Remove wrong requires
- rename tomoe-gtk
- rename tomoe-gtk
- BR pygtk2

* Sun Jul 01 2007 Funda Wang <fwang@mandriva.org> 0.6.0-2mdv2008.0
+ Revision: 46480
- fix file list
- BR python-gobject-devel
- BR gtk-doc
- corrected tarball dirname
- New version


* Thu Feb 22 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.5.1-2mdv2007.0
+ Revision: 124676
- bump release
- new release
- Import libtomoe-gtk

* Fri Jan 05 2007 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.5.0-1mdv2007.1
- new release

* Fri Dec 01 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.4.0-1mdv2007.1
- new release

* Wed Nov 01 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.3.0-1mdv2007.1
- new release

* Fri Mar 03 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.1.0-3mdk
- add BuildRequires: gtk+2-devel

* Wed Feb 22 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.1.0-2mdk
- use %%mkrel

* Sun Oct 30 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.1.0-1mdk
- first spec for Mandriva Linux

