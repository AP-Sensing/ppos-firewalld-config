BuildArch:      noarch
Name:           ppos-firewalld-config
Version:        1.1.0
Release:        1
License:        GPLv3
Summary:        RPM containing the PhotonPonyOS firewalld configuration.
Distribution:   PhotonPonyOS

URL:            https://github.com/AP-Sensing/ppos-firewalld-config/tree/ppos38
Vendor:         AP Sensing
Packager:       AP Sensing
Provides:       ppos-firewalld-config = %{version}-%{release}

Requires:       firewalld
Requires:       systemd
Requires(post): firewalld

%{?systemd_requires}

Source0: %{_sourcedir}/firewalld-ppos.conf
Source1: %{_sourcedir}/ppos.xml
Source2: %{_sourcedir}/ppos-firewalld-zone.service
Source3: %{_sourcedir}/42-ppos-firewalld-zone.preset
Source4: %{_sourcedir}/ppos-firewalld-set-default-zone

# Zone docs: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-working_with_zones

%description
RPM containing the PhotonPonyOS firewalld configuration.

%prep

%build

%install
# Zone
install -d -m 755 $RPM_BUILD_ROOT/usr/lib/firewalld/zones
install -m 644 %{_sourcedir}/ppos.xml $RPM_BUILD_ROOT/usr/lib/firewalld/zones/

# Config
install -d -m 755 $RPM_BUILD_ROOT/etc/firewalld
install -m 644 %{_sourcedir}/firewalld-ppos.conf $RPM_BUILD_ROOT/etc/firewalld/

# Service
install -d -m 755 $RPM_BUILD_ROOT/usr/lib/systemd/system
install -m 644 %{_sourcedir}/ppos-firewalld-zone.service $RPM_BUILD_ROOT/usr/lib/systemd/system

# Service preset
install -d -m 755 $RPM_BUILD_ROOT/usr/lib/systemd/system-preset
install -m 644 %{_sourcedir}/42-ppos-firewalld-zone.preset $RPM_BUILD_ROOT/usr/lib/systemd/system-preset

# Zone update script
install -d -m 755 $RPM_BUILD_ROOT/usr/bin/
install -m 755 %{_sourcedir}/ppos-firewalld-set-default-zone $RPM_BUILD_ROOT/usr/bin

%post
%systemd_post ppos-firewalld-zone.service

%postun
%systemd_postun_with_restart ppos-firewalld-zone.service

%preun
%systemd_preun ppos-firewalld-zone.service

%files
%attr(0644, root, root) /etc/firewalld/firewalld-ppos.conf
%attr(0644, root, root) /usr/lib/firewalld/zones/ppos.xml

%attr(644, root, root) /usr/lib/systemd/system/ppos-firewalld-zone.service
%attr(644, root, root) /usr/lib/systemd/system-preset/42-ppos-firewalld-zone.preset

%attr(755, root, root) /usr/bin/ppos-firewalld-set-default-zone

%changelog
* Thu Jan 19 2024 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.1.0-1
- Added port 5001 for the gateway

* Thu Jan 11 2024 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.0.0-1
- Initial release