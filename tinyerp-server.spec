# NOTE: NOT USABLE!
Summary:	Tiny ERP - free ERP and CRM software (server)
Summary(pl.UTF-8):   Tiny ERP - darmowe oprogramowanie ERP i CRM (serwer)
Name:		tinyerp-server
Version:	3.2.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://tinyerp.org/download/sources/%{name}-%{version}.tgz
# Source0-md5:	4acbbd8e8fac798ea3e9da08e076b465
Patch0:		%{name}-start.patch
URL:		http://tinyerp.org/
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-libxml2
BuildRequires:	python-libxslt
BuildRequires:	python-psycopg
BuildRequires:	python-pydot
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-ReportLab
Requires:	python-libxml2
Requires:	python-libxslt
Requires:	python-psycopg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tiny ERP is a complete ERP and CRM. The main features are accounting
(analytic and financial), stock management, sales and purchases
management, tasks automation, marketing campaigns, help desk, POS,
etc. Technical features include a distributed server, flexible
workflows, an object database, a dynamic GUI, customizable reports,
and SOAP and XML-RPC interfaces.

%description -l pl.UTF-8
Tiny ERP to pełny ERP i CRM. Główne możliwości to rozliczenia
(analityczne i finansowe), zarządzanie magazynem, zarządzanie
sprzedażą i zakupami, automatyzacja zadań, kampanie reklamowe, help
desk, POS itp. Techniczne możliwości obejmują serwer rozproszony,
elastyczne przepływy prac, obiektową bazę danych, dynamiczne GUI,
konfigurowalne raporty oraz interfejsy SOAP i XML-RPC.

%prep
%setup -q -n server
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--prefix=/usr \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/addons/{base/report,base_partner_relation,edi/{report,wizard},sale/report,esale,network/report,account/{data,datas},purchase/report,audittrail,scrum,account.old/{datas,report,project},delivery,product,product_electronic,product_expiry}

cd bin/
for i in `find -name *.xml`; do
	install $i $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/`echo $i | sed 's/\.//'`
done

for i in `find -name *.xsl`; do
	install $i $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/`echo $i | sed 's/\.//'`
done

for i in `find -name *.sql`; do
	install $i $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/`echo $i | sed 's/\.//'`
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
