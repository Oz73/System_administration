Name:           test-bash
Version:        1.0
Release:        1%{?dist}
Summary:        Bash скрипт для підрахунку файлів у каталозі /etc

License:        GPL
Group:          Utilities
URL:            http://example.com
Source0:        test_bash.sh

BuildArch:      noarch

%description
Цей RPM-пакет містить Bash скрипт, який підраховує кількість звичайних файлів у каталозі /etc.

%prep

%build

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/test_bash.sh

%files
/usr/bin/test_bash.sh

%changelog
* Fri Oct 08 2024 Oz73 <Oz73@example.com> - 1.0-1
- Initial package
