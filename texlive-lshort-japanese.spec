Name:		texlive-lshort-japanese
Version:	36207
Release:	2
Summary:	Japanese version of A Short Introduction to LaTeX2e 
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/japanese
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-japanese.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-japanese.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive lshort-japanese package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-japanese/00README
%doc %{_texmfdistdir}/doc/latex/lshort-japanese/CHANGES.jp
%doc %{_texmfdistdir}/doc/latex/lshort-japanese/READ.ME
%doc %{_texmfdistdir}/doc/latex/lshort-japanese/jlshort-1.00.src.tar.gz
%doc %{_texmfdistdir}/doc/latex/lshort-japanese/jlshort.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
