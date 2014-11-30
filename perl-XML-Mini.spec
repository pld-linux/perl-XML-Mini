#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	XML
%define		pnam	Mini
%include	/usr/lib/rpm/macros.perl
Summary:	XML::Mini - Perl implementation of the XML::Mini XML create/parse interface
Summary(pl.UTF-8):	XML::Mini - implementacja perlowa interfejsu tworzącego/analizującego XML
Name:		perl-XML-Mini
Version:	1.38
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0262295a6812f4ea1a4c13aefa9067c4
URL:		http://search.cpan.org/dist/XML-Mini/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Mini is a set of Perl classes that allow you to access XML data
and create valid XML output with a tree-based hierarchy of elements.
The MiniXML API has both Perl and PHP implementations.

%description -l pl.UTF-8
XML::Mini to zbiór klas Perla pozwalających na dostęp do danych XML
oraz tworzenie poprawnego wyjścia w XML-u z drzewiastą hierarchią
elementów. API MiniXML ma implementacje w Perlu i PHP.

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
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
