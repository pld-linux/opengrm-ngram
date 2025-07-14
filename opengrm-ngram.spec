#
# Conditional build:
%bcond_without	static_libs	# static libraries
#
Summary:	OpenGrm NGram library - making and modifying n-gram language models
Summary(pl.UTF-8):	Biblioteka OpenGrm NGram - tworzenie i modyfikowanie modeli n-gramowych języków
Name:		opengrm-ngram
Version:	1.3.4
Release:	2
License:	Apache v2.0
Group:		Libraries
#Source0Download: http://www.openfst.org/twiki/bin/view/GRM/NGramDownload
Source0:	http://www.openfst.org/twiki/pub/GRM/NGramDownload/%{name}-%{version}.tar.gz
# Source0-md5:	a158efb18c83c1f64bce5211d635af77
Patch0:		%{name}-link.patch
URL:		http://www.openfst.org/twiki/bin/view/GRM/NGramLibrary
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:1.5
BuildRequires:	openfst-devel >= 1.5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenGrm NGram library is used for making and modifying n-gram
language models encoded as weighted finite-state transducers (FSTs).
It makes use of functionality in the OpenFst library to create, access
and manipulate n-gram models.

%description -l pl.UTF-8
Biblioteka OpenGrm NGram służy do tworzenia i modyfikowania modeli
n-gramowych języków zakodowanych jako automaty skończone z wyjściem
(FST) i wagami. Do tworzenia, dostępu i operowania na modelach
n-gramowych wykorzystuje bibliotekę OpenFst.

%package devel
Summary:	Header files for OpenGrm NGram library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenGrm NGram
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7
Requires:	openfst-devel >= 1.5.2

%description devel
Header files for OpenGrm NGram library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenGrm NGram.

%package static
Summary:	Static OpenGrm NGram library
Summary(pl.UTF-8):	Statyczna biblioteka OpenGrm NGram
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenGrm NGram library.

%description static -l pl.UTF-8
Statyczna biblioteka OpenGrm NGram.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened module
%{__rm} $RPM_BUILD_ROOT%{_libdir}/hist-arc.la \
	%{?with_static_libs:$RPM_BUILD_ROOT%{_libdir}/hist-arc.a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/ngramapply
%attr(755,root,root) %{_bindir}/ngramcontext
%attr(755,root,root) %{_bindir}/ngramcount
%attr(755,root,root) %{_bindir}/ngramhisttest
%attr(755,root,root) %{_bindir}/ngraminfo
%attr(755,root,root) %{_bindir}/ngrammake
%attr(755,root,root) %{_bindir}/ngrammarginalize
%attr(755,root,root) %{_bindir}/ngrammerge
%attr(755,root,root) %{_bindir}/ngramperplexity
%attr(755,root,root) %{_bindir}/ngramprint
%attr(755,root,root) %{_bindir}/ngramrandgen
%attr(755,root,root) %{_bindir}/ngramrandtest
%attr(755,root,root) %{_bindir}/ngramread
%attr(755,root,root) %{_bindir}/ngramshrink
%attr(755,root,root) %{_bindir}/ngramsort
%attr(755,root,root) %{_bindir}/ngramsplit
%attr(755,root,root) %{_bindir}/ngramsymbols
%attr(755,root,root) %{_bindir}/ngramtransfer
%attr(755,root,root) %{_libdir}/libngram.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libngram.so.134
%attr(755,root,root) %{_libdir}/libngramhist.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libngramhist.so.134
# dlopened module
%attr(755,root,root) %{_libdir}/hist-arc.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libngram.so
%attr(755,root,root) %{_libdir}/libngramhist.so
%{_libdir}/libngram.la
%{_libdir}/libngramhist.la
%{_includedir}/ngram

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libngram.a
%{_libdir}/libngramhist.a
%endif
