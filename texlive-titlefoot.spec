Name:		texlive-titlefoot
Version:	15878
Release:	2
Summary:	Add special material to footer of title page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/titlefoot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlefoot.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides the capability of adding keywords (with a \keywords
command), a running title (\runningtitle), AMS subject
classifications (\amssubj), and an 'author's footnote' as
footnotes to the title or first page of a document. Works with
any class for which the \thanks macro works (e.g., article).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/titlefoot/titlefoot.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
