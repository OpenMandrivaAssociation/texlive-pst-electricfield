# revision 21864
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-electricfield
# catalog-date 2011-03-28 22:21:58 +0200
# catalog-license lppl
# catalog-version 0.14
Name:		texlive-pst-electricfield
Version:	0.14
Release:	1
Summary:	Draw electric field and equipotential lines with PStricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-electricfield
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-electricfield.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-electricfield.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-electricfield.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides macros to plot electric field and
equipotential lines using PStricks. There may be any number of
charges which can be placed in a cartesian coordinate system by
(x,y) values.

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
%{_texmfdistdir}/dvips/pst-electricfield/pst-electricfield.pro
%{_texmfdistdir}/tex/generic/pst-electricfield/pst-electricfield.tex
%{_texmfdistdir}/tex/latex/pst-electricfield/pst-electricfield.sty
%doc %{_texmfdistdir}/doc/generic/pst-electricfield/Changes
%doc %{_texmfdistdir}/doc/generic/pst-electricfield/README
%doc %{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-docDE.pdf
%doc %{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-docDE.tex
%doc %{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-docEN.pdf
%doc %{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-docEN.tex
%doc %{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-docFR.pdf
%doc %{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-docFR.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-electricfield/Makefile
%doc %{_texmfdistdir}/source/generic/pst-electricfield/Makefile.latex
%doc %{_texmfdistdir}/source/generic/pst-electricfield/Makefile.pst2pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
