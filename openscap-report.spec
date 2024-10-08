%global name        openscap-report
%global module      openscap_report

Name:           %{name}
Version:        0.0.0
Release:        0%{?dist}
Summary:        A tool for generating human-readable reports from (SCAP) XCCDF and ARF results

License:        LGPL-2.1
URL:            https://github.com/OpenSCAP/%{name}
Source0:        https://github.com/OpenSCAP/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%global _description %{expand:
A tool for generating human-readable reports from SCAP XCCDF and ARF results.}

%description %_description

Summary:        %{summary}


%prep
%autosetup -p1 -n %{name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel
sphinx-build -b man docs _build_docs



%install
%pyproject_install
%pyproject_save_files %{module}
install -Dt %{buildroot}%{_mandir}/man8 _build_docs/oscap-report.8


%check
%tox


%files -f %{pyproject_files}
%{_mandir}/man8/oscap-report.*
%{_bindir}/oscap-report
%exclude %{python3_sitelib}/tests/


%changelog
