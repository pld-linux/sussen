#
# todo:
#
# - anjuta is used, so ac/am stuff is screwed up...
# - nessus-config should be used in Makefile.am (i.e. to not link with
#   libpcap-nessus.so)!
# - nessus paths and optflags in src/Makefile.am
#
Summary:	GNOME client for Nessus Security Scanner
Summary(pl):	Klient skanera bezpieczeñstwa Nessusa dla GNOME
Name:		sussen
Version:	0.3
Release:	1.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/sussen/%{name}-%{version}.tar.gz
# Source0-md5:	f7a6d8ecbce00a3a67a1bfe6ac3ebe1c
Patch0:		%{name}-nessus.patch
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
%patch -p1

%build
%{__gettextize}
%{__libtoolize}
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} \
	sussen_LDADD="\\\$(GNOME_LIBS) `nessus-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/sussen
%{_datadir}/sussen
%{_pixmapsdir}/sussen
