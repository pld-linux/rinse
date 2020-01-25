Summary:	A utility designed to install a minimal RPM-based distribution within a local directory
Name:		rinse
Version:	3.0.2
Release:	1
License:	GPL, Artistic
Group:		Development/Tools
Source0:	http://collab-maint.alioth.debian.org/rinse/download/%{name}_%{version}.tar.gz
# Source0-md5:	51c7875ae363ed35963e3b9fad344dd1
URL:		http://collab-maint.alioth.debian.org/rinse/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_prefix}/lib

%description
The rinse utility is designed to install a minimal RPM-based
distribution of GNU/Linux within a local directory. The purpose and
usage are analogous to the 'debootstrap' utility familiar to users of
Debian GNU/Linux.

%prep
%setup -qc
mv %{name}/* .

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.packages
%attr(755,root,root) %{_sbindir}/rinse
%{_mandir}/man8/rinse.8*
%defattr(755,root,root,755)
%{_libexecdir}/%{name}

# bash-completion
/etc/bash_completion.d/rinse
