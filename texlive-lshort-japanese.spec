# revision 15878
# category Package
# catalog-ctan /info/lshort/japanese
# catalog-date 2006-12-28 00:06:45 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-lshort-japanese
Version:	20190822
Release:	1
Summary:	Japanese version of A Short Introduction to LaTeX2e 
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/japanese
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-japanese.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-japanese.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


