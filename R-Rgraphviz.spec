%global packname  Rgraphviz
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.32.0
Release:          1
Summary:          Provides plotting capabilities for R graph objects
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-methods R-utils R-graph R-grid 
Requires:         R-graph R-graphics R-grDevices R-grid R-methods R-utils 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-utils R-graph R-grid
BuildRequires:    R-graph R-graphics R-grDevices R-grid R-methods R-utils 
BuildRequires:    blas-devel
BuildRequires:    graphviz-devel
BuildRequires:    lapack-devel

%description
Interfaces R with the AT and T graphviz library for plotting R graph
objects from the graph package. Users on all platforms must install
graphviz; see the README file, available in the source distribution of
this file, for details.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME blocks
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/usecases
