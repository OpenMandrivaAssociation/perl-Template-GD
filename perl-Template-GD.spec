%define upstream_name    Template-GD
%define upstream_version 2.66

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	GD plugin(s) for the Template Toolkit
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Template)
BuildArch:	noarch

%description
The Template-GD distribution provides a number of Template Toolkit plugin
modules to interface with Lincoln Stein's GD modules. These in turn provide an
interface to Thomas Boutell's GD graphics library.

These plugins were distributed as part of the Template Toolkit until version
2.15 released in February 2006. At this time they were extracted into this
separate distribution.

For general information on the Template Toolkit see the documentation for the
Template module or http://template-toolkit.org. For information on using
plugins, see Template::Plugins and "USE" in Template::Manual::Directives.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Template
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.660.0-1mdv2010.0
+ Revision: 405530
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.66-4mdv2009.0
+ Revision: 258460
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.66-3mdv2009.0
+ Revision: 246500
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.66-1mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.66-1mdv2007.0
+ Revision: 111253
- Import perl-Template-GD

* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.66-1mdv2007.1
- first mdv release

