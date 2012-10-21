Summary:	The dovecot antispam plugin
Summary(pl.UTF-8):	Wtyczka antyspamowa dla dovecota
Name:		dovecot-antispam
Version:	2.0
Release:	9
License:	GPL v2
Group:		Daemons
Source0:	http://johannes.sipsolutions.net/download/dovecot-antispam/%{name}-%{version}.tar.bz2
# Source0-md5:	14547898759fbd93f2b98304520decc6
Patch0:		dovecot-2.1.patch
URL:		http://johannes.sipsolutions.net/Projects/dovecot-antispam
BuildRequires:	dovecot-devel >= 1:2.0
%requires_eq_to	dovecot dovecot-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The dovecot antispam plugin watches moving mail into and out of the
SPAM folder and tells the spam classifier that it made an error and
needs to re-classify the message (as spam/not spam depending on which
way it was moved).

#%description -l pl.UTF-8

%prep
%setup -q
%patch0 -p1
cp -a antispam-storage-2.0.c antispam-storage-2.1.c

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/dovecot/plugins,%{_mandir}/man7}

%{__make} install \
	INSTALLDIR=%{_libdir}/dovecot/plugins \
	DESTDIR=$RPM_BUILD_ROOT

install -p antispam.7 $RPM_BUILD_ROOT%{_mandir}/man7

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTES
%attr(755,root,root) %{_libdir}/dovecot/plugins/lib90_antispam_plugin.so
%{_mandir}/man7/antispam.7*
