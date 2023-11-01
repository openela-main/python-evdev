%if 0%{?rhel} && 0%{?rhel} < 8
%bcond_without legacy_python
%endif

Name:           python-evdev
Version:        1.1.2
Release:        3%{?dist}
Summary:        Python bindings for the Linux input handling subsystem

License:        BSD
URL:            https://python-evdev.readthedocs.io
Source0:        https://github.com/gvalkov/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  kernel-headers
%if %{with legacy_python}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Patch01: 0001-input-fix-ioctl-return-value-handling.patch
Patch02: 0001-input-fix-unintended-fallthrough.patch

%global _description \
This package provides python bindings to the generic input event interface in \
Linux. The evdev interface serves the purpose of passing events generated in \
the kernel directly to userspace through character devices that are typically \
located in /dev/input/. \
 \
This package also comes with bindings to uinput, the userspace input subsystem. \
Uinput allows userspace programs to create and handle input devices that can \
inject events directly into the input subsystem. \
 \
In other words, python-evdev allows you to read and write input events on Linux. \
An event can be a key or button press, a mouse movement or a tap on a \
touchscreen.


%description %{_description}


%if %{with legacy_python}
%package -n python2-evdev
Summary:        %{summary}
%{?python_provide:%python_provide python2-evdev}
%description -n python2-evdev %{_description}
%endif

%package -n python3-evdev
Summary:        %{summary}
%{?python_provide:%python_provide python3-evdev}
%description -n python3-evdev %{_description}


#------------------------------------------------------------------------------
%prep
%autosetup -p1

#------------------------------------------------------------------------------
%build
%if %{with legacy_python}
%py2_build
%endif
%py3_build

#------------------------------------------------------------------------------
%install
%if %{with legacy_python}
%py2_install
%endif
%py3_install

#------------------------------------------------------------------------------
%if %{with legacy_python}
%files -n python2-evdev
%license LICENSE
%doc README.rst
%{python2_sitearch}/evdev/
%{python2_sitearch}/evdev-%{version}-py%{python2_version}.egg-info/
%endif

%files -n python3-evdev
%license LICENSE
%doc README.rst
%{python3_sitearch}/evdev/
%{python3_sitearch}/evdev-%{version}-py%{python3_version}.egg-info/


#------------------------------------------------------------------------------
%changelog
* Fri Oct 05 2018 Peter Hutterer <peter.hutterer@redhat.com> 1.1.2-3
- Fix coverity complaints

* Wed Sep 26 2018 Peter Hutterer <peter.hutterer@redhat.com> 1.1.2-2
- Don't build with python2 on RHEL8

* Wed Sep 26 2018 Peter Hutterer <peter.hutterer@redhat.com> 1.1.2-1
- Bump to version 1.1.2

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.0.0-2
- Rebuild with fixed binutils

* Sat Jul 28 2018 Georgi Valkov <georgi.t.valkov@gmail.com> - 1.0.0-1
- Bump to version 1.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Georgi Valkov <georgi.t.valkov@gmail.com> - 0.7.0-1
- Bump to version 0.7.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-2
- Rebuild for Python 3.6

* Sun Jun 05 2016 Georgi Valkov <georgi.t.valkov@gmail.com> - 0.6.1-1
- Initial RPM Release
