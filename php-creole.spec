Summary:	Creole is a database abstraction layer for PHP5
Name:		php-creole
Version:	1.1.0
Release:	0.1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://creole.tigris.org/files/documents/996/34244/creole-%{version}.tar.gz
# Source0-md5:	4d9f44b42403b91aaecf247da41cecf1
URL:		http://creole.phpdb.org/
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Creole is a database abstraction layer for PHP5. It abstracts PHP's
native db-specific API to create more portable code while also
providing developers with a clean fully object-oriented interface
based loosely on the API for Java's JDBC.

There are a number of database abstraction packages for PHP. Creole
draws from experience with several of these -- noteably PEAR::DB,
PEAR::MDB, and ADOdb. Creole was created as a subproject of Propel to
meet specific needs that none of the available abstraction layers were
able to address in any satisfactory way.

%prep
%setup -q -n creole-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
cp -a classes/creole $RPM_BUILD_ROOT%{php_pear_dir}
cp -a classes/jargon $RPM_BUILD_ROOT%{php_pear_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/*