Summary:	Console Locker
Summary(pl.UTF-8):	Blokowanie konsoli
Name:		cl
Version:	0.2
Release:	1
License:	RPL Rebane Public License (beerware)
Group:		Applications/System
Source0:	http://glen.alkohol.ee/cl/%{name}-%{version}.tar.bz2
# Source0-md5:	5570c7f42a628e1181437b9ee51216f9
URL:		http://glen.alkohol.ee/cl/
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Console locker by Rebane.

%description -l pl.UTF-8
Aplikacja autorstwa Rebane do blokowania konsoli linuksowej.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/cl
%attr(4755,root,root) %{_sbindir}/cl
