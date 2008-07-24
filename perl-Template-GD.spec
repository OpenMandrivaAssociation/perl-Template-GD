%define module  Template-GD
%define name    perl-%{module}
%define version 2.66
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        GD plugin(s) for the Template Toolkit
License:        Artistic
group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Template/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Template)
buildArch:      noarch
buildRoot:      %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Template
%{_mandir}/*/*


