Summary:	GNOME client for Nessus Security Scanner
Name:		sussen
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	libgnomeui-devel >= 2.3.3
BuildRequires:	nessus-libs-devel >= 2.0.6a
BuildRequires:	openssl-devel >= 0.9.7b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sussen is a GNOME client for the Nessus Security Scanner.

%prep
%setup -q

%build
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL README NEWS
%attr(755,root,root) %{_bindir}/sussen
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
