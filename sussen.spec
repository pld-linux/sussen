Summary:	GNOME client for Nessus Security Scanner
Summary(pl):	Klient skanera bezpieczeñstwa Nessusa dla GNOME
Name:		sussen
Version:	0.5.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	a01ad46aa2b301119efa158378e60034
URL:		http://sussen.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	libgnomeui-devel >= 2.3.3
BuildRequires:	libtool
BuildRequires:	nessus-libs-devel >= 2.0.6a
BuildRequires:	openssl-devel >= 0.9.7b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sussen is a GNOME client for the Nessus Security Scanner.

%description -l pl
Sussen jest klientem skanera bezpieczeñstwa Nessusa dla ¶rodowiska
GNOME.

%prep
%setup -q

%build
%{__gettextize}
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
	gnomemenudir=%{_applnkdir}/Network

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/sussen
%{_datadir}/sussen
%{_pixmapsdir}/sussen
%{_applnkdir}/Network/*.desktop
