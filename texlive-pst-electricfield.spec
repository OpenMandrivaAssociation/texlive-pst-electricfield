Name:		texlive-pst-electricfield
Version:	29803
Release:	2
Summary:	Draw electric field and equipotential lines with PStricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-electricfield
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-electricfield.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-electricfield.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-electricfield.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros to plot electric field and
equipotential lines using PStricks. There may be any number of
charges which can be placed in a cartesian coordinate system by
(x,y) values.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
