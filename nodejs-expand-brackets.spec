%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name expand-brackets

Summary:       Expand POSIX bracket expressions in glob patterns
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       0.1.4
Release:       3%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/expand-brackets
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Expand POSIX bracket expressions (character classes) in glob patterns.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.4-3
- rebuilt

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 0.1.4-2
- Enable scl macros

* Tue Dec 15 2015 Troy Dawson <tdawson@redhat.com> - 0.1.4-1
- Initial package