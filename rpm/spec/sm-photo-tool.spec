Name:           sm-photo-tool
Version:        1.10
Release:        1
Summary:        Smugmug client
Group:          Applications/Multimedia
License:        GPL
URL:            http://code.google.com/p/sm-photo-tool/
Source0:        %{name}-%{version}.tar.gz
Patch0:         %{name}-1.10-license.patch
BuildRoot:      %{_tmppath}/%{name}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python
Requires:       python >= 2.3

%description
Smugmug client

%prep
%setup -q
%patch -p1 -b .license

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_usr}/share/%{name}/
install -d -m 755 %{buildroot}%{_usr}/share/doc/%{name}-%{version}/
install -d -m 755 %{buildroot}%{_usr}/bin/
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/
install -m 644 LICENSE.TXT %{buildroot}%{_usr}/share/doc/%{name}-%{version}/
install -m 644 smugmugrc %{buildroot}%{_usr}/share/doc/%{name}-%{version}/
install -m 755 sm-photo-tool.py %{buildroot}%{_usr}/bin/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(755, root, root) %{_usr}/bin/%{name}
%{_usr}/share/doc/%{name}-%{version}/LICENSE.TXT
%{_usr}/share/doc/%{name}-%{version}/smugmugrc

%changelog
* Sat Apr  1 2006 Jesus Rodriguez <jmrodri at gmail dot com> 1.10-1
- initial rpm release
