#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Sys
%define		pnam	OutPut
Summary:	Sys::OutPut perl module
Summary(pl.UTF-8):	Moduł perla Sys::OutPut
Name:		perl-Sys-OutPut
Version:	2.1
Release:	11
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	abcb37e8cfdd3a137902fba609b78467
URL:		http://search.cpan.org/dist/Sys-OutPut/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys::OutPut - module to help make output easier.

%description -l pl.UTF-8
Sys::OutPut - moduł ułatwiający pisanie na wyjście.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Sys/OutPut.pm
%{_mandir}/man3/*
