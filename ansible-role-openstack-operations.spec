%global srcname ansible_role_openstack_operations
%global rolename ansible-role-openstack-operations

%{!?upstream_version: %global upstream_version %{commit}}
%global commit 274739ee5b0ff702f67af59ec2ff42b78c495bce
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:           %{rolename}
Version:        0.0.1
Release:        0.1%{?alphatag}%{?dist}
Summary:        Ansible role to perform OpenStack Day 2 Operations

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://opendev.org/openstack/ansible-role-openstack-operations
Source0:        https://github.com/openstack/%{rolename}/archive/%{commit}.tar.gz#/%{rolename}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       python3dist(ansible) >= 2
Requires:       ansible-pacemaker

%description

Ansible role to perform OpenStack Day 2 Operations

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{py3_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{py3_install}


%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog
* Thu May 07 2020 RDO <dev@lists.rdoproject.org> 0.0.1-0.1.274739egit
- Update to pre-release 0.0.1 (274739ee5b0ff702f67af59ec2ff42b78c495bce)


