# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%global srcname ansible_role_openstack_operations
%global rolename ansible-role-openstack-operations

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        XXX
Release:        XXX
Summary:        Ansible role to perform OpenStack Day 2 Operations

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/ansible-role-openstack-operations
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-d2to1
Requires:       ansible
%else
BuildRequires:  python%{pyver}-d2to1
Requires:       python3dist(ansible) >= 2
%endif
Requires:       ansible-pacemaker

%description

Ansible role to perform OpenStack Day 2 Operations

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{pyver_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{pyver_install}


%files
%doc README*
%license LICENSE
%{pyver_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog

