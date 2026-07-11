%global tl_name titlefoot
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Add special material to footer of title page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/titlefoot
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/titlefoot.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides the capability of adding keywords (with a \keywords command), a
running title (\runningtitle), AMS subject classifications (\amssubj),
and an 'author's footnote' as footnotes to the title or first page of a
document. Works with any class for which the \thanks macro works (e.g.,
article).

