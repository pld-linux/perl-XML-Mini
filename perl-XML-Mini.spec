#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Mini
Summary:	XML::Mini - Perl implementation of the XML::Mini XML create/parse interface
Summary(pl):	XML::Mini - perlowa implementacja interfejsu tworz±cego/analizuj±cego XML
Name:		perl-XML-Mini
Version:	1.2.7
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Mini is a set of Perl classes that allow you to access XML data
and create valid XML output with a tree-based hierarchy of elements.
The MiniXML API has both Perl and PHP implementations.

%description -l pl
XML::Mini to zbiór klas Perla pozwalaj±cych na dostêp do danych XML
oraz tworzenie poprawnego wyj¶cia w XML z drzewiast± hierarchi±
elementów. API MiniXML ma implementacje w Perlu i PHP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes 
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
