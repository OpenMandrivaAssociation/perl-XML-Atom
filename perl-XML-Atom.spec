%define upstream_name    XML-Atom
%define upstream_version 0.37

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl Module for Processing Atom Feeds
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

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

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Requires:   perl(XML::LibXML)

%description
Perl Module for processing Atoms feed and that provides access to the Atom
API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
