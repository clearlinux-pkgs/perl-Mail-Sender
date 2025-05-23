#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Mail-Sender
Version  : 0.903
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/Mail-Sender-0.903.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/Mail-Sender-0.903.tar.gz
Summary  : '(DEPRECATED) module for sending mails with attachments through an SMTP server'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Mail-Sender-license = %{version}-%{release}
Requires: perl-Mail-Sender-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Mail::Sender - (DEPRECATED) module for sending mails with attachments
through an SMTP server

%package dev
Summary: dev components for the perl-Mail-Sender package.
Group: Development
Provides: perl-Mail-Sender-devel = %{version}-%{release}
Requires: perl-Mail-Sender = %{version}-%{release}

%description dev
dev components for the perl-Mail-Sender package.


%package license
Summary: license components for the perl-Mail-Sender package.
Group: Default

%description license
license components for the perl-Mail-Sender package.


%package perl
Summary: perl components for the perl-Mail-Sender package.
Group: Default
Requires: perl-Mail-Sender = %{version}-%{release}

%description perl
perl components for the perl-Mail-Sender package.


%prep
%setup -q -n Mail-Sender-0.903
cd %{_builddir}/Mail-Sender-0.903

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mail-Sender
cp %{_builddir}/Mail-Sender-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Mail-Sender/a13a10f7ca2ebf34644ad35913ac26eb98a2ed2b || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mail::Sender.3
/usr/share/man/man3/Mail::Sender::CType::Ext.3
/usr/share/man/man3/Mail::Sender::CType::Win32.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Mail-Sender/a13a10f7ca2ebf34644ad35913ac26eb98a2ed2b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
