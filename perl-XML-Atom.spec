%define module  XML-Atom
%define name    perl-%{module}
%define release %mkrel 4
%define version 0.28

Name:               %{name}
Version:            %{version}
Release:            %{release}
Summary:            Perl Module for Processing Atom Feeds
License:            GPL or Artistic
Group:              Development/Perl
Url:                http://search.cpan.org/dist/%{module}/
Source:             http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
Requires:         perl(XML::LibXML)
BuildRequires:    perl(MIME::Base64)
BuildRequires:    perl(URI)
BuildRequires:    perl(Class::Data::Inheritable)
BuildRequires:    perl(XML::LibXML)
BuildRequires:    perl(XML::XPath)
BuildRequires:    perl(LWP)
BuildRequires:    perl(LWP::Authen::Wsse)
BuildRequires:    perl(Digest::SHA1)
BuildRequires:    perl(DateTime)
BuildRequires:    perl(HTML::Parser)
BuildArch:        noarch
BuildRoot:        %{_tmppath}/%{name}-%{version}

%description
Perl Module for processing Atoms feed and that provides access to the Atom
API.

%prep
%setup -q -n %{module}-%{version}

%build
SKIP_SAX_INSTALL=1 CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/XML
%{_mandir}/*/*


