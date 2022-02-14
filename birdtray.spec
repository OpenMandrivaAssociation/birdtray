Summary:        Thunderbird tray and notification system
Name:           birdtray
Version:        1.9.0
Release:        1
License:        GPLv3
Group:          Networking/Mail
URL:            https://github.com/gyunaev/birdtray
Source0:        https://github.com/gyunaev/birdtray/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  qmake5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)

%description
Birdtray is a free system tray notification for new mail for Thunderbird.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build
  
%files
%doc README.md
%license LICENSE.txt
%{_bindir}/birdtray
%{_datadir}/ulduzsoft/
%{_datadir}/applications/com.ulduzsoft.Birdtray.desktop
%{_iconsdir}/hicolor/*/apps/com.ulduzsoft.Birdtray.png
%{_iconsdir}/hicolor/scalable/apps/com.ulduzsoft.Birdtray.svg
%{_metainfodir}/com.ulduzsoft.Birdtray.appdata.xml
