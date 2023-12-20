Name:		texlive-truthtable
Version:	68300
Release:	1
Summary:	Automatically generate truth tables for given variables and statements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/truthtable
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/truthtable.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/truthtable.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LuaLaTeX package permits to automatically generate truth
tables given a table header. It supports a number of logical
operations which can be combined as needed. It is built upon
the luacode package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/truthtable
%doc %{_texmfdistdir}/doc/lualatex/truthtable

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
