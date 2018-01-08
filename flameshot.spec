Name: flameshot
Version: 0.5.0
Release: 2%{?dist}

# Main code: GPLv3
# Logo: Free Art License v1.3
# Button icons: Apache License 2.0
# capture/capturewidget.cpp and capture/capturewidget.h: GPLv2
# regiongrabber.cpp: LGPL
# Qt-Color-Widgets: LGPL/GPL
# More information: https://github.com/lupoDharkael/flameshot#license
License: GPLv3+ and ASL 2.0 and GPLv2 and LGPLv3 and Free Art
Summary: Powerful and simple to use screenshot software

URL: https://github.com/lupoDharkael/flameshot
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# https://github.com/lupoDharkael/flameshot/pull/69
Patch100: %{name}-0.5.0-fix-desktop.patch

# https://github.com/lupoDharkael/flameshot/pull/68
Patch101: %{name}-0.5.0-add-appdata.patch

BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5DBus)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: qt5-linguist
BuildRequires: gcc-c++
BuildRequires: gcc

%description
Powerful and simple to use screenshot software with built-in
editor with advanced features.

%prep
%autosetup -p1
mkdir %{_target_platform}

%build
pushd %{_target_platform}
    %qmake_qt5 PREFIX=%{_prefix} CONFIG+=packaging ..
popd

%make_build -C %{_target_platform}

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}
%find_lang Internationalization --with-qt

%check
appstream-util validate-relax --nonet "%{buildroot}%{_datadir}/appdata/%{name}.appdata.xml"
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f Internationalization.lang
%doc README.md
%license LICENSE img/flameshotLogoLicense.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/icons/%{name}.png

%changelog
* Mon Jan 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-2
- Minor SPEC fixes.

* Sat Jan 06 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-1
- Initial SPEC release.
