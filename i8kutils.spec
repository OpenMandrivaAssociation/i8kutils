%define	name	i8kutils
%define	version	1.27
%define	release	%mkrel 4

Version: 	%{version}
Summary: 	Dell laptop SMM BIOS support
Name: 		%{name}
Release: 	%{release}
License: 	GPLv2+
Group: 		Monitoring
Source: 	http://ftp.debian.org/debian/pool/main/i/i8kutils/%{name}_%{version}.tar.gz
URL: 		http://people.debian.org/~dz/i8k/	
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	tcl
Requires:	tk

%description
This package contains a user-space programs for accessing the SMM BIOS
of Dell Inspiron and Latitude laptops. The SMM BIOS is used on many recent
laptops to implement APM functionalities and to access custom hardware,
for example cooling fans and volume buttons.

Also provided is a cool and useful plugin for gkrellm.
Note that you need the "Dell Laptop" option compiled into your kernel
(included in the main kernel tree since 2.4.14-pre8)


%prep
%setup -q 

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_bindir
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README.*
%{_bindir}/*
