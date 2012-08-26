#
%define		_state		stable
%define		orgname		filelight
%define		qtver		4.8.0

Summary:	K Desktop Environment - Disk usage statistics
Name:		kde4-filelight
Version:	4.9.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	984f85e7d62796b608742d398b111903
URL:		http://www.kde.org/
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	openssl-devel
Requires:	kde4-kdebase-workspace >= %{version}
Obsoletes:	kde4-kdeutils-filelight
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Disk usage statistics.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/filelight
%attr(755,root,root) %{_libdir}/kde4/filelightpart.so
%{_desktopdir}/kde4/filelight.desktop
%{_datadir}/apps/filelight
%{_datadir}/apps/filelightpart
%{_datadir}/config/filelightrc
%{_iconsdir}/hicolor/*x*/apps/filelight.png
%{_iconsdir}/hicolor/*x*/actions/view_filelight.png
%{_datadir}/kde4/services/filelightpart.desktop
