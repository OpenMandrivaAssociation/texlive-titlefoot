# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/titlefoot
# catalog-date 2007-01-17 00:08:13 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-titlefoot
Version:	20170414
Release:	1
Summary:	Add special material to footer of title page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/titlefoot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlefoot.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070117-2
+ Revision: 756920
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070117-1
+ Revision: 719753
- texlive-titlefoot
- texlive-titlefoot
- texlive-titlefoot

