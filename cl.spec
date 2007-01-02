Summary:	Console Locker
Name:		cl
Version:	0.1
Release:	0.1
License:	RPL Rebane Public License (beerware)
Group:		Applications/System
Source0:	http://rebane.alkohol.ee/%{name}.c.txt
# Source0-md5:	cf7cc688e32668bc297477a15069e299
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Console locker by Rebane.

%clean
rm -rf $RPM_BUILD_ROOT

%prep
%setup -qcT
cp %{SOURCE0} cl.c

%build
%{__cc} cl.c -o cl -lpam

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install cl $RPM_BUILD_ROOT%{_sbindir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/cl
