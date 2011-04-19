Name:    task-scanning
Version: 2011.0
Release: %mkrel 1
Summary: Metapackage for scanning
Group:   Graphics
License: GPL
#
Requires: scanner-gui
Requires: sane-backends
Suggests: xsane-gimp

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies and recommended additions for scanning.

%files


