%global tl_name lshort-japanese
%global tl_revision 79461

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Japanese version of A Short Introduction to LaTeX2e
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/japanese
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-japanese.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-japanese.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Japanese version of A Short Introduction to LaTeX2e

