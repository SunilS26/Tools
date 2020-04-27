#rpmdev-setuptree,  rpmbuild --target noarch -bb  tracerRpm.spec
Version:    1.0.0
Release:    1
Summary:    Most simple RPM package
License:    GPL
BUILDROOT:~/rpmbuild/

%description
This is my first RPM package, which does nothing.

%prep
# we have no source, so nothing here
echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp /root/sunil/rpmbuild/scripts/tracer.py $RPM_BUILD_ROOT/usr/bin
exit

%build
%post
%postun


%files
/usr/bin/*

%changelog
# let skip this for now
