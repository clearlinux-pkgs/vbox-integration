#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vbox-integration
Version  : 3
Release  : 3
URL      : https://github.com/clearlinux/vbox-integration/archive/v3.tar.gz
Source0  : https://github.com/clearlinux/vbox-integration/archive/v3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: vbox-integration-bin = %{version}-%{release}
Requires: vbox-integration-license = %{version}-%{release}

%description
No detailed description available

%package bin
Summary: bin components for the vbox-integration package.
Group: Binaries
Requires: vbox-integration-license = %{version}-%{release}

%description bin
bin components for the vbox-integration package.


%package license
Summary: license components for the vbox-integration package.
Group: Default

%description license
license components for the vbox-integration package.


%prep
%setup -q -n vbox-integration-3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1558652342
export GCC_IGNORE_WERROR=1
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1558652342
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/vbox-integration
cp COPYING %{buildroot}/usr/share/package-licenses/vbox-integration/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/install-vbox-lga

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/vbox-integration/COPYING
