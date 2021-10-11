%global luaver 5.3
%define lua_libdir %{_libdir}/lua/%{luaver}
%define lua_pkgdir %{_datadir}/lua/%{luaver}


Name:           lua-posix
Version:        35.0.1
Release:        1
Summary:        A POSIX library for Lua
License:        MIT
URL:            http://luaforge.net/projects/luaposix/
Source0:        https://github.com/luaposix/luaposix/archive/v%{version}/lua-posix-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  lua
BuildRequires:  pkgconfig(libcrypt)


%description
This is a POSIX library for Lua which provides access to many POSIX features
to Lua programs.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
build-aux/luke CFLAGS="%build_cflags"


%install
build-aux/luke install \
         PREFIX=%{buildroot}%{_prefix} \
         INST_LIBDIR=%{buildroot}%{lua_libdir}


#check
# Tests require specl which is not yet packaged


%files
%license LICENSE
%doc AUTHORS ChangeLog.old NEWS.md README.md
%{lua_libdir}/*
%{lua_pkgdir}/posix/
