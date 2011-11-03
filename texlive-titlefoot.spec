# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/titlefoot
# catalog-date 2007-01-17 00:08:13 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-titlefoot
Version:	20070117
Release:	1
Summary:	Add special material to footer of title page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/titlefoot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlefoot.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Provides the capability of adding keywords (with a \keywords
command), a running title (\runningtitle), AMS subject
classifications (\amssubj), and an 'author's footnote' as
footnotes to the title or first page of a document. Works with
any class for which the \thanks macro works (e.g., article).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/titlefoot/titlefoot.sty
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
