%define name trousers-changer
%define subdir %{?qubes_builder:%{name}/}
%define _builddir %(pwd)/%{subdir}
%{!?version: %define version %(cat %{subdir}version)}

Name:		%{name}
Version:	%{version}
Release:	1%{?dist}
Summary:    	tcsd wrapper for portable installations
Requires:	trousers tpm-tools systemd tpm-extra >= 4.0.0
Requires(post):	systemd
Vendor:		Invisible Things Lab
License:	GPL
URL:		http://www.qubes-os.org

%description
tcsd wrapper for portable installations.

%install
cp -r sbin $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/lib
cp -r systemd $RPM_BUILD_ROOT/usr/lib

%files
/sbin/tpm_id
/sbin/tcsd_changer_identify
/sbin/tcsd_changer_migrate
/usr/lib/systemd/system/tcsd.service.d/trousers-changer.conf

%post
systemctl daemon-reload

%postun
if [ "$1" = 0 ]; then
    systemctl daemon-reload
fi
