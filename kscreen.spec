Name:           kscreen
Epoch:          1
Version:        1.0.1
Release:        4%{?dist}
Summary:        KDE Display Management software
# KDE e.V. may determine that future GPL versions are accepted
License:        GPLv2 or GPLv3
URL:            http://www.kde.org/ 
Source0:        http://download.kde.org/stable/kscreen/kscreen-%{version}.tar.bz2
Requires:       libkscreen%{?_isa} = %{epoch}:%{version}
BuildRequires:  kdelibs4-devel
BuildRequires:  libkscreen-devel
BuildRequires:  qjson-devel >= 0.8.1
BuildRequires:  gettext

%description
KCM and KDED modules for managing displays in KDE.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kscreen
%find_lang kcm_displayconfiguration
%find_lang plasma_applet_org.kde.plasma.kscreen


%files -f kscreen.lang -f kcm_displayconfiguration.lang -f plasma_applet_org.kde.plasma.kscreen.lang
%doc COPYING
%{_kde4_bindir}/kscreen-console
%{_kde4_libdir}/kde4/kcm_kscreen.so
%{_kde4_libdir}/kde4/kded_kscreen.so
%{_kde4_libdir}/kde4/plasma_applet_kscreen.so
%{_kde4_appsdir}/kcm_kscreen/
%{_kde4_datadir}/kde4/services/kcm_kscreen.desktop
%{_kde4_datadir}/kde4/services/kded/kscreen.desktop
%{_kde4_datadir}/kde4/services/plasma-applet-kscreen-qml.desktop
%{_kde4_datadir}/kde4/services/plasma-applet-kscreen.desktop
%{_kde4_datadir}/kde4/apps/plasma/packages/org.kde.plasma.kscreen.qml
%{_kde4_datadir}/icons/hicolor/*/actions/*


%changelog
* Wed Aug 14 2013 Than Ngo <than@redhat.com> - 1:1.0.1-4
- fix URL

* Fri Aug 09 2013 Dan Vrátil <dvratil@redhat.com> 1:1.0.1-3
- fix Source0 URL

* Wed Aug 07 2013 Than Ngo <than@redhat.com> - 1:1.0.1-2
- rebuilt

* Thu Aug 01 2013 Dan Vrátil <dvratil@redhat.com> 1:1.0.1-1
 - kscreen 1:1.0.1-1

* Mon Jun 17 2013 Dan Vrátil <dvratil@redhat.com> 1:1.0-1
 - kscreen 1:1.0-1

* Thu May 02 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.92-1
 - update to 1:0.0.92-1
 
* Tue Apr 23 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.82.git20130424-1
 - dev git build

* Mon Apr 08 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.81-2
 - Explicitely depend on the same version of libkscreen

* Wed Mar 27 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.81-1
 - Update to 1:0.0.81-1

* Mon Jan 28 2013 Rex Dieter <rdieter@fedoraproject.org> 1:0.0.71-3
- drop Provides: kde-display-management, Conflicts: kded_randrmonitor

* Thu Jan 24 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.71-2
 - add Provides and Conflicts fields so make sure radrmonitor and
   kscreen never run side by side

* Sun Jan 20 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.71-1
 - update to 0.0.71 - first official release
 - install kscreen-console, which has been moved from libkscreen
 - the KCM is now called kcm_kscreen

* Wed Jan 09 2013 Dan Vrátil <dvratil@redhat.com> 0.9.0-5.20121228git
 - Update description, we don't ship the Plasma applet yet
 - Provides kde-display-management, a metapackage for KScreen and kded_randrmonitor
 - Conflicts with kded_randrmonitor

* Wed Jan 09 2013 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-4.20121228git
- BR: qjson-devel >= 0.8.1
- License: GPLv2 or GPLv3
- tighten %%files

* Wed Jan 01 2013 Dan Vrátil <dvratil@redhat.com> 0.9.0-3.20121228git
 - Added qjson-devel to BuildRequires

* Fri Dec 28 2012 Dan Vrátil <dvratil@redhat.com> 0.9.0-2.20121228git
 - Fixed URL

* Fri Dec 28 2012 Dan Vrátil <dvratil@redhat.com> 0.9.0-1.20121228git
 - Fixed versioning
 - Added instructions how to obtain sources
 - Removed 'rm -rf $RPM_BUILD_ROOT'

* Wed Dec 26 2012 Dan Vrátil <dvratil@redhat.com> 20121226gitb31ab08-1
 - Initial SPEC
