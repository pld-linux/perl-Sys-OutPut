%include	/usr/lib/rpm/macros.perl
%define	pdir	Sys
%define	pnam	OutPut
Summary:	Sys::OutPut perl module
Summary(pl):	Modu³ perla Sys::OutPut
Name:		perl-Sys-OutPut
Version:	2.1
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys::OutPut - module to help make output easier.

%description -l pl
Sys::OutPut - modu³ u³atwiaj±cy pisanie na wyj¶cie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Sys/OutPut.pm
%{_mandir}/man3/*
