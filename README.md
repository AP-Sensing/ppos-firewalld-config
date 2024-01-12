# ppos-firewalld-config

RPM containing the [PhotonPonyOS](https://github.com/AP-Sensing/PhotonPonyOS) [firewalld](https://firewalld.org) configuration.

## Requirements

```bash
sudo dnf install rpmdevtools
```

## Building

```bash
# Optionally run `rm -rf ~/rpmbuild/` to ensure we have a clean working directory. 
rpmdev-setuptree

cp -r SPECS/* ~/rpmbuild/SPECS/
cp -r SOURCES/* ~/rpmbuild/SOURCES/

rpmbuild -bs ~/rpmbuild/SPECS/ppos-firewalld-config.spec
rpmbuild -bb ~/rpmbuild/SPECS/ppos-firewalld-config.spec
```

The resulting rpm files are the located inside `~/rpmbuild/SRPMS/` and `~/rpmbuild/RPMS/`.

```bash
ls -l ~/rpmbuild/SRPMS/
ls -l ~/rpmbuild/RPMS/
```

## Signing

Follow these steps for signing the build rpm packages.

### Requirements

```bash
sudo dnf install rpm-sign
```

Follow these instructions for setting up a signing gpg key: https://access.redhat.com/articles/3359321
Then run the following commands for signing all (source-)rpms.
```bash
rpm --addsign ~/rpmbuild/SRPMS/**.rpm
rpm --addsign ~/rpmbuild/RPMS/**/*.rpm
```
