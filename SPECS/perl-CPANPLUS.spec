Name:           perl-CPANPLUS
Version:        0.9916
Release:        4%{?dist}
Summary:        API & CLI access to the CPAN mirrors
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CPANPLUS/
Source0:        http://www.cpan.org/modules/by-module/CPANPLUS/CPANPLUS-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Log::Message)
BuildRequires:  perl(Package::Constants)
BuildRequires:  perl(Object::Accessor)
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Term::UI)
BuildRequires:  perl(DBIx::Simple)
BuildRequires:  perl(DBD::SQLite)
Requires:       perl(Log::Message)
Requires:       perl(Package::Constants)
Requires:       perl(Object::Accessor)
Requires:       perl(Archive::Extract)
Requires:       perl(Term::UI)
Requires:       perl(DBIx::Simple)
Requires:       perl(DBD::SQLite)
Requires:       perl(Module::Pluggable)
#cpanp cannot install any packages that look like core https://github.com/jib/cpanplus-devel/blob/18efaed3b4b9e307795a41cd1b11177a456f5187/lib/CPANPLUS/Module.pm#L437
Requires:       perl(blib)
Requires:       perl(FindBin)
Requires:       perl(Devel::Peek)
#Install common build systems for script
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(Module::Build)
Requires:       perl(Module::Build::Tiny)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The CPANPLUS library is an API to the CPAN mirrors and a collection of
interactive shells, commandline programs, etc, that use this API.

%prep
%setup -q -n CPANPLUS-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Sun Mar 02 2025 Michael R. Davis <mrdvt92@yahoo.com> 0.9916-1
- Specfile autogenerated by cpanspec 1.78.
