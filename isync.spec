Name:           isync
Version:        1.1.0
Release:        1%{?dist}
Summary:        Tool to synchronize IMAP4 and Maildir mailboxes

License:        GPLv2+
URL:            http://isync.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  libdb-devel
BuildRequires:  openssl-devel

%description
isync is a command line application which synchronizes mailboxes; currently
Maildir and IMAP4 mailboxes are supported.  New messages, message deletions
and flag changes can be propagated both ways.  isync is suitable for use in
IMAP-disconnected mode.

%prep
%setup -q
# Convert to utf-8
for file in ChangeLog; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
# Remove copy of documentation files installed by package's buildsystem.
# Preverred over patching Makefile.am an regenerating Makefile.in due
# to robustness.
rm -r %{buildroot}%{_datadir}/doc/isync

%files
%doc AUTHORS COPYING NEWS README TODO ChangeLog src/mbsyncrc.sample src/compat/isyncrc.sample
%{_bindir}/isync
%{_bindir}/mbsync
%{_bindir}/mdconvert
%{_bindir}/get-cert
%{_mandir}/man1/*

%changelog
* Sat Dec 21 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Updated to new upstream version 1.1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Fabian Affolter <mail@fabian-affolter.ch> 1.0.6-1
- Updated to new upstream version 1.0.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 1.0.5-3
- Change BR: db4-devel to libdb-devel

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 29 2012 Fabian Affolter <mail@fabian-affolter.ch> 1.0.5-1
- Updated to new upstream version 1.0.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.0.4-6
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Fabian Affolter <mail@fabian-affolter.ch> 1.0.4-3
- Preserved time stamps
- Fixed encoding error

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> 1.0.4-2
- rebuild with new openssl

* Sat Feb 23 2008 Lubomir Kundrak <lkundrak@redhat.com> 1.0.4-1
- 1.0.4
- Drop upstreamed patches (all!)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.3-7
- Autorebuild for GCC 4.3

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
