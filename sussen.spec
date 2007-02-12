Summary:	GNOME client for Nessus Security Scanner
Summary(pl.UTF-8):	Klient skanera bezpieczeństwa Nessusa dla GNOME
Name:		sussen
Version:	0.24
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dev.mmgsecurity.com/downloads/sussen/%{name}-%{version}.tar.gz
# Source0-md5:	f7ef78c80d535192226767650d2324ca
URL:		http://dev.mmgsecurity.com/projects/sussen/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.4
BuildRequires:	dotnet-gtk-sharp2-gnome-devel >= 2.4
BuildRequires:	gnet-devel
BuildRequires:	libgnomedb-devel >= 1.0.0
BuildRequires:	libgnomeui-devel >= 2.3.3
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1
BuildRequires:	nessus-libs-devel >= 2.0.6a
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sussen is a tool that checks for vulnerabilities and configuration
issues on computer systems.

%description -l pl.UTF-8
Sussen jest narzędziem do wyszukiwania dziur w zabezpieczeniach oraz
problemów z konfigracją w różnych systemach komputerowych.

%prep
%setup -q

%build
%{__libtoolize}
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} \
	sussen_LDADD="\\\$(SUSSENMODS_LIBS) `nessus-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomemenudir=%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/%{name}
%{_mandir}/man1/*
%attr(755,root,root) %{_libdir}/*.so
%{_pixmapsdir}/sussen-icon.png
%{_desktopdir}/*.desktop
%{_pkgconfigdir}/*.pc
%{_docdir}/%{name}
%{_libdir}/mono/gac/*
%{_libdir}/monodoc/sources/*
%{_libdir}/dbus-1.0/services/*
%{_libdir}/%{name}/
%{_libdir}/*.la
%{_datadir}/application-registry/*
%{_libdir}/bonobo/servers/*.server
