%global debug_package %{nil}
%global rust_flags -Ccodegen-units=1 -Cstrip=debuginfo

Name:           atac
Version:        0.14.0
Release:        1%{?dist}
Summary:        Arguably a Terminal API Client

License:        MIT
URL:            https://github.com/Julien-cpsn/ATAC
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires: gcc-c++
%if 0%{?el8} || 0%{?el9}
%else
BuildRequires: cargo
BuildRequires: rust
%endif

%description
Arguably a Terminal API Client. Feature-full, free, open-source, offline and account-less.

%prep
%autosetup -n ATAC-%{version}
%if 0%{?el8} || 0%{?el9}
curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
%endif

%install
export RUSTFLAGS="%{rust_flags}"
%if 0%{?el8} || 0%{?el9}
$HOME/.cargo/bin/cargo install --locked --root=%{buildroot}%{_prefix} --path=.
%else
cargo install --locked --root=%{buildroot}%{_prefix} --path=.
%endif

rm -f %{buildroot}%{_prefix}/.crates.toml \
    %{buildroot}%{_prefix}/.crates2.json
strip --strip-all %{buildroot}%{_bindir}/*

%files
%license LICENSE
%doc README.md
%{_bindir}/atac

%changelog
* Apr 18 2024 julien-cpsn <julien.caposiena@gmail.com> - v0.13.0
- Update to 0.13.0

* Apr 23 2024 julien-cpsn <julien.caposiena@gmail.com> - v0.14.0
- Update to 0.14.0
