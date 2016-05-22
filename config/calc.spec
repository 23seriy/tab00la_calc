#spec file
Summary:        A calc app that rocks!
Name:           calc
Version:        %{calc_version}
Release:        1
License:        GPL

Requires: java-1.8.0-openjdk

%description

%prep

%build

%install
sudo rm -rf $RPM_BUILD_ROOT
sudo mkdir -p $RPM_BUILD_ROOT/usr/local/taboola/calc/lib
sudo mkdir -p $RPM_BUILD_ROOT/usr/local/bin
sudo mkdir -p $RPM_BUILD_ROOT/tmp
sudo cp -R /usr/local/taboola/calc/* $RPM_BUILD_ROOT/usr/local/taboola/calc/
sudo ln -sf /usr/local/taboola/calc/execute_calc.sh $RPM_BUILD_ROOT/usr/local/bin/calc

%clean
sudo rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir /usr/local/taboola/calc/
%dir /usr/local/taboola/calc/lib
%dir /usr/local/bin
/usr/local/taboola/calc/taboola_test-*.jar
/usr/local/taboola/calc/lib/*
/usr/local/taboola/calc/execute_calc.sh
/usr/local/bin/calc
