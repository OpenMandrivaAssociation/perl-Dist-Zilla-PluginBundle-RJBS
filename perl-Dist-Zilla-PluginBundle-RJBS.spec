%define upstream_name    Dist-Zilla-PluginBundle-RJBS
%define upstream_version 5.004

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	See what the mantissa for an rjbs-style version is today

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires:	perl(Dist::Zilla::Plugin::Repository)
BuildRequires:	perl(Dist::Zilla::Plugin::TaskWeaver)
BuildRequires:	perl(Dist::Zilla::Plugin::BumpVersionFromGit)
BuildRequires:	perl(Dist::Zilla::PluginBundle::Git)
BuildRequires:	perl(Pod::Elemental)
BuildRequires:	perl(Pod::Elemental::Transformer::List)
BuildRequires:	perl(Pod::Weaver)
BuildArch:	noarch

%description
This is the plugin bundle that RJBS uses. It is equivalent to:

  [@Filter]
  bundle = @Classic
  remove = PodVersion
  remove = MetaYAML

  [AutoVersion]
  [MetaJSON]
  [NextRelease]
  [PodWeaver]
  [Repository]

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*




