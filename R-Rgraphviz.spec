%global packname  Rgraphviz
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.4.1
Release:          1
Summary:          Provides plotting capabilities for R graph objects
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/Rgraphviz_2.4.1.tar.gz
Requires:         R-methods R-utils R-graph R-grid
Requires:         R-graphics R-grDevices R-grid R-methods R-utils
Requires:         graphviz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-methods R-utils R-graph R-grid
BuildRequires:    R-graphics R-grDevices R-grid R-methods R-utils
BuildRequires:    blas-devel
BuildRequires:    graphviz-devel
BuildRequires:    lapack-devel
BuildRequires:    x11-server-xvfb

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

# FIXME blocks (apparently due to calling malloc, with bogus value, from
# signal handler that apparently triggered the signal due to out of memory)
#(gdb) bt
#0  __lll_lock_wait_private () at ../nptl/sysdeps/unix/sysv/linux/x86_64/lowlevellock.S:96
#1  0x00000034de680ce5 in _L_lock_9980 () from /lib64/libc.so.6
#2  0x00000034de67ea62 in __GI___libc_malloc (bytes=227072984864) at malloc.c:2925
#3  0x00007f1f8b006268 in ?? () from /usr/lib64/R/lib/libR.so
#4  0x00007f1f8af7fbee in ?? () from /usr/lib64/R/lib/libR.so
#5  0x00007f1f8af81417 in ?? () from /usr/lib64/R/lib/libR.so
#6  0x00007f1f8af8248e in ?? () from /usr/lib64/R/lib/libR.so
#7  0x00007f1f8afb21b5 in R_GetTraceback () from /usr/lib64/R/lib/libR.so
#8  0x00007f1f8affad61 in ?? () from /usr/lib64/R/lib/libR.so
#9  <signal handler called>
#10 malloc_consolidate (av=0x34de9ac720) at malloc.c:4252
#11 0x00000034de67bff8 in malloc_consolidate (av=0x34de9ac720) at malloc.c:4227
#12 _int_malloc (av=0x34de9ac720, bytes=<optimized out>) at malloc.c:3538
#13 0x00000034de67ea70 in __GI___libc_malloc (bytes=2008) at malloc.c:2928
%if 0
%check
xvfb-run %{_bindir}/R CMD check %{packname}
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

