#
# rpm spec file for sussen 
#

Summary: GNOME2 client for Nessus Security Scanner
Name: sussen
Version: 0.3
Release: 1
License: GPL
Group: Applications/Security
Packager: Loren Bandiera <sussen@starchamber.ca>
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: libgnomeui >= 2.0.0
Requires: libglade2 >= 2.0.0
Requires: glib2 >= 2.0.0
Requires: GConf2 >= 2.0.0
Requires: nessus-libraries
Requires: openssl
BuildRequires: libgnomeui-devel >= 2.0.0
BuildRequires: libglade2-devel >= 2.0.0
BuildRequires: glib2-devel >= 2.0.0
BuildRequires: GConf2-devel >= 2.0.0
BuildRequires: nessus-libraries
BuildRequires: openssl

%description
Sussen is a GNOME 2.2 client for the Nessus Security Scanner

%preq
%setup -q
%build
%configure
%make
%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall
%clean

[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README NEWS
%{_bindir}/sussen
%{_datadir}/about.glade
%{_datadir}/auth.glade
%{_datadir}/cert_druid.glade
%{_datadir}/getting_started.glade
%{_datadir}/policy_manager.glade
%{_datadir}/preferences.glade
%{_datadir}/report_druid.glade
%{_datadir}/report_viewer.glade
%{_datadir}/server_properties.glade
%{_datadir}/session.glade
%{_datadir}/sussen.glade
%{_datadir}/sussen_preferences.glade
%{_datadir}/sussen_preferences_server.glade
%{_datadir}/SANS_Top_20.policy
%{_datadir}/all_but_dangerous_plugins.policy
%{_datadir}/all_plugins.policy
%{_datadir}/auth.png
%{_datadir}/error.png
%{_datadir}/eye.png
%{_datadir}/info.png
%{_datadir}/login.png
%{_datadir}/logout.png
%{_datadir}/nothing.xpm
%{_datadir}/offline.png
%{_datadir}/online.png
%{_datadir}/warning.png

%changelog
* Mon Jun 16 2003 Loren Bandiera <sussen@starchamber.ca>
- updated spec file for sussen v0.3

* Sat Jun 07 2003 Loren Bandiera <sussen@starchamber.ca>
- Make spec file for sussen
