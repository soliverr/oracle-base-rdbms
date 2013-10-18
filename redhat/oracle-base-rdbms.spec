
Summary   :  Directory layout for Oracle RDBMS.
Summary(ru_RU.UTF-8)   : Иерархия каталогов для СУБД Oracle.
Name      : oracle-base-rdbms
Version   : 2.0
Release   : 1
Group     : Database

Packager  : Kryazhevskikh Sergey, <soliverr@gmail.com>
License   : GPLv2

BuildArch : noarch
Requires  : oracle-base

Source: %name-%version.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}

%define pkg_build_dir   %_builddir/%name-%version
%define pkg_functions   %pkg_build_dir/_pkg-functions

%description
Directory layout and system groups for Oracle RDBMS.

%description -l ru_RU.UTF-8
Иерархия каталогов и системные группы для СУБД Oracle.

%prep

%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{__install} -d %{buildroot}/var/log/oracle/
%{__install} -d %{buildroot}/db
%{__install} -D oracle-base-rdbms-log-dirs %{buildroot}/usr/bin/oracle-base-rdbms-log-dirs
ORACLE_RDBMS_LOG_BASE_BUILD_DST=%{buildroot} %{buildroot}/usr/bin/oracle-base-rdbms-log-dirs -d

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%pre
%include %{pkg_functions}

if [ $1 -eq 1 ] ; then
  action=install
else
  action=upgrade
fi

preinst "redhat" "$action"


%preun
%include %pkg_functions

if [ $1 -eq 0 ] ; then
  action=remove
else
  action=upgrade
fi

prerm "redhat" "$action"

%post
%include %pkg_functions

if [ $1 -eq 1 ] ; then
  action=configure
else
  action=upgrade
fi

postinst "redhat" "$action"

%postun
%include %pkg_functions

if [ $1 -eq 0 ] ; then
  action=purge
  #chmod -R 2755 /etc/oracle
  #chown -R oracle:oracle /etc/oracle
else
  action=upgrade
fi

postrm "redhat" "$action"


%files
%defattr(-,root,root)
%doc README
%dir %attr(775,oracle,dba) /db
%dir %attr(2770,oracle,dba) /var/log/oracle/*
%dir %attr(2770,oracle,dba) /var/log/oracle/ldap/*
%dir %attr(2770,oracle,dba) /var/log/oracle/network/*
%dir %attr(2770,oracle,dba) /var/log/oracle/rdbms/*
%attr(750,oracle,dba) /usr/bin/*

%changelog
* Fri Oct 18 2013 Kryazhevskikh Sergey <soliverr@gmail.com> - 2.0-1  12:59:28 +0600
- Added `dboper' system group. Closed [ticket:#5]

* Fri Jun 15 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-7  11:42:24 +0600
- Added `diag' directory

* Thu Jun 07 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-6  12:55:19 +0600
- Added `owb' and `mgw' directories

* Thu May 24 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-5  18:16:24 +0600
- List directories to package

* Thu May 24 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-4  17:48:49 +0600 
- Added new directories

* Wed Apr 18 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-3  11:00:29 +0600
- Added `/db' directory
- Directory `rdbms/audit' moved into `/var/log/oracle'

* Tue Mar 13 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-2  15:40:13 +0600
- Added `oracle-base-rdbms-log-dirs' script
	
* Thu Aug 18 2011 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-1  17:22:42 +0600
- Initial version of package
