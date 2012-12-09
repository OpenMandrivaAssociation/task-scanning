Name:    task-scanning
Version: 2011.0
Release: %mkrel 4
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




%changelog
* Tue Apr 19 2011 Antoine Ginies <aginies@mandriva.com> 2011.0-1mdv2011.0
+ Revision: 655949
- bumpo t 2011 release

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2009.1-4mdv2011.0
+ Revision: 607981
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2009.1-3mdv2010.1
+ Revision: 524169
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2009.1-2mdv2010.0
+ Revision: 427283
- rebuild

* Mon Dec 15 2008 Thierry Vignaud <tv@mandriva.org> 2009.1-1mdv2009.1
+ Revision: 314498
- import task-scanning


* Mon Dec 15 2008 Thierry Vignaud <tvignaud@mandriva.com> 2009.1-1mdv2009.1
- initial release
