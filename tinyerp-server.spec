# NOTE: NOT USABLE!
Summary:	Tiny ERP - free ERP and CRM software (server)
Summary(pl):	Tiny ERP - darmowe oprogramowanie ERP i CRM (serwer)
Name:		tinyerp-server
Version:	3.2.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://tinyerp.org/download/sources/%{name}-%{version}-rc1.tar.gz
# Source0-md5:	38d91b235b7e3ec1b1f4ac055a18ca91
Patch0:		%{name}-start.patch
URL:		http://tinyerp.org/
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-libxml2
BuildRequires:	python-libxslt
BuildRequires:	python-psycopg
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	python-pydot
Requires:	python-libxml2
Requires:	python-libxslt
Requires:	python-psycopg
Requires:	python-ReportLab
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
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--prefix=/usr \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

install -d $RPM_BUILD_ROOT/%{py_sitescriptdir}/%{name}/addons/{base/report,sale/report,esale,network/report,account/datas,purchase/report}

cd bin/
for i in `find -name *.xml`; do
	install $i $RPM_BUILD_ROOT/%{py_sitescriptdir}/%{name}/`echo $i | sed 's/\.//'`
done

for i in `find -name *.xsl`; do
	install $i $RPM_BUILD_ROOT/%{py_sitescriptdir}/%{name}/`echo $i | sed 's/\.//'`
done

for i in `find -name *.sql`; do
	install $i $RPM_BUILD_ROOT/%{py_sitescriptdir}/%{name}/`echo $i | sed 's/\.//'`
done

#%%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{INSTALL,README*}
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%{_mandir}/man?/*
