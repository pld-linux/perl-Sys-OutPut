%include	/usr/lib/rpm/macros.perl
Summary:	Sys-OutPut perl module
Summary(pl):	Modu³ perla Sys-OutPut
Name:		perl-Sys-OutPut
Version:	2.1
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sys/Sys-OutPut-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys-OutPut - module to help make output easier.

%description -l pl
Sys-OutPut - modu³ u³atwiaj±cy pisanie na wyj¶cie.

%prep
%setup -q -n Sys-OutPut-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Sys/OutPut.pm
%{_mandir}/man3/*
