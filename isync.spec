Name:           isync
Version:        1.0.3
Release:        6%{?dist}
Summary:        Tool to synchronize IMAP4 and Maildir mailboxes

Group:          Applications/Internet
License:        GPLv2+
URL:            http://isync.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         isync-1.0.3-open.patch
Patch1:         isync-1.0.3-args.patch
Patch2:         isync-1.0.3-search.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  db4-devel openssl-devel

%description
isync is a command line application which synchronizes mailboxes; currently
Maildir and IMAP4 mailboxes are supported.  New messages, message deletions
and flag changes can be propagated both ways.  isync is suitable for use in
IMAP-disconnected mode.


%prep
%setup -q
%patch0 -p1 -b .open
%patch1 -p1 -b .args
%patch2 -p1 -b .search


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# Remove copy of documentation files installed by package's buildsystem.
# Preverred over patching Makefile.am an regenerating Makefile.in due
# to robustness.
rm -r $RPM_BUILD_ROOT%{_datadir}/doc/isync


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/isync
%{_bindir}/mbsync
%{_bindir}/mdconvert
%{_bindir}/get-cert
%{_mandir}/man1/*
%doc AUTHORS COPYING NEWS README TODO ChangeLog src/mbsyncrc.sample src/compat/isyncrc.sample


%changelog
* Mon Dec 17 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.3-6
- gmail returns SEARCH with no argument (#420721)

* Sun Dec 16 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.3-5
- mbsync was ignoring option letters from last argument (#425838)

* Sun Sep 09 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.3-3
- Fix code for the case where open() is a macro. (thanks to Marek Mahut)
- Cosmetic fixes. (#282261) (thanks to Till Maas)

* Fri Sep 07 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.3-2
- Added dependency on OpenSSL for SSL/TLS support

* Fri Sep 07 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.3-1
- Initial package
