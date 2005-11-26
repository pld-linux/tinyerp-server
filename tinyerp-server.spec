Summary:	Tiny ERP - free ERP and CRM software (server)
Summary(pl):	Tiny ERP - darmowe oprogramowanie ERP i CRM (serwer)
Name:		tinyerp-server
Version:	3.1.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://tinyerp.org/download/sources/%{name}-%{version}.tar.gz
# Source0-md5:	9d4a0d90a29a089368c3fc24c9f4b8bc
URL:		http://tinyerp.org/
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-libxml2
BuildRequires:	python-libxslt
BuildRequires:	python-psycopg
BuildRequires:  rpmbuild(macros) >= 1.219
#Requires:	graphviz
#Requires:	python-Imaging
Requires:	python-libxml2
Requires:	python-libxslt
Requires:	python-psycopg
#Requires:	python-pyparsing
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tiny ERP is a complete ERP and CRM. The main features are accounting
(analytic and financial), stock management, sales and purchases
management, tasks automation, marketing campaigns, help desk, POS,
etc. Technical features include a distributed server, flexible
workflows, an object database, a dynamic GUI, customizable reports,
and SOAP and XML-RPC interfaces.

%description -l pl
Tiny ERP to pe³ny ERP i CRM. G³ówne mo¿liwo¶ci to rozliczenia
(analityczne i finansowe), zarz±dzanie magazynem, zarz±dzanie
sprzeda¿± i zakupami, automatyzacja zadañ, kampanie reklamowe, help
desk, POS itp. Techniczne mo¿liwo¶ci obejmuj± serwer rozproszony,
elastyczne przep³ywy prac, obiektow± bazê danych, dynamiczne GUI,
konfigurowalne raporty oraz interfejsy SOAP i XML-RPC.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--prefix=/usr \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

#%%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{INSTALL,README*}
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/tinyerp_server
%{_mandir}/man?/*
