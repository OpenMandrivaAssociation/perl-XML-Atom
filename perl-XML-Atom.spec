%define upstream_name    XML-Atom
%define upstream_version 0.41

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl Module for Processing Atom Feeds
License:	GPLv1+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/XML/XML-Atom-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(URI)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::XPath)
BuildRequires:	perl(LWP)
BuildRequires:	perl(LWP::Authen::Wsse)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(HTML::Parser)

BuildArch:	noarch
Requires:	perl(XML::LibXML)

%description
Perl Module for processing Atoms feed and that provides access to the Atom
API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
SKIP_SAX_INSTALL=1 CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML
%{_mandir}/*/*

%changelog
* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.390.0-1mdv2011.0
+ Revision: 687006
- update to new version 0.39

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.380.0-1
+ Revision: 682200
- update to new version 0.38

* Wed Dec 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.370.0-1mdv2011.0
+ Revision: 483887
- update to 0.37

* Fri Dec 25 2009 Michael Scherer <misc@mandriva.org> 0.360.0-2mdv2010.1
+ Revision: 482289
- fix License

* Wed Dec 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-1mdv2010.1
+ Revision: 481711
- update to 0.36

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.350.0-1mdv2010.0
+ Revision: 401878
- rebuild using %%perl_convert_version

* Sun May 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2010.0
+ Revision: 371363
- update to new version 0.35

* Thu Jan 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2009.1
+ Revision: 327085
- update to new version 0.33

* Mon Nov 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.32-1mdv2009.1
+ Revision: 306237
- update to new version 0.32

* Fri Nov 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2009.1
+ Revision: 303114
- update to new version 0.31

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2009.1
+ Revision: 302725
- new version

* Mon Oct 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.29-1mdv2009.1
+ Revision: 297544
- update to new version 0.29

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.28-4mdv2009.0
+ Revision: 258795
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.28-3mdv2009.0
+ Revision: 246720
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Nov 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.28-1mdv2008.1
+ Revision: 106665
- update to new version 0.28

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.27-1mdv2008.1
+ Revision: 97576
- update to new version 0.27


* Mon Mar 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-2mdv2007.1
+ Revision: 141649
- explicit dependency on perl(XML::LibXML)

* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2007.1
+ Revision: 133532
- fix build dependencies, drop explicit runtime dependencies

* Fri Mar 02 2007 Shlomi Fish  0.25-2mdv2007.1
- Fixed the summary.
- Converted to noarch.

* Fri Mar 02 2007 Shlomi Fish  0.25-1mdv2007.1
- Initial release. Adapted the Feed-Find spec for this one.


