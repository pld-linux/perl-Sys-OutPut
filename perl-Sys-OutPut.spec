%include	/usr/lib/rpm/macros.perl
Summary:	Sys-OutPut perl module
Summary(pl):	Modu³ perla Sys-OutPut
Name:		perl-Sys-OutPut
Version:	2.1
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sys/Sys-OutPut-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Sys-OutPut - module to help make output easier. 

%description -l pl
Sys-OutPut - modu³ u³atwiaj±cy pisanie na wyj¶cie.

%prep
%setup -q -n Sys-OutPut-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Sys/OutPut
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Sys/OutPut.pm
%{perl_sitearch}/auto/Sys/OutPut

%{_mandir}/man3/*
