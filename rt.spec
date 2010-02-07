#
# Copyright (c) 2005, 2006, 2007, 2008 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# Supported rpmbuild options:
#
# --with gd/--without gd 
#	enable/disable gd support
#	Default: --with (had been default in rt < 3.8.0)
%bcond_without gd 

# --with graphviz/--without graphviz
#	enable/disable graphiz support
#	Default: --without (missing deps)
%bcond_with graphviz

# --with devel_mode/--without devel_mode
#	enable/disable building/installing devel files
#	Default: without (missing deps; TBA in spec)
%bcond_with devel_mode

# --with gpg/--without gpg
#	enable/disable building gpg support
#	Default: without
%bcond_with gpg

# --with tests
#	run testsuite when building the rpm
#	Default: without (doesn't work in chroots.)
%bcond_with tests

%define RT_BINDIR		%{_sbindir}
%define RT_LIBDIR		%{perl_vendorlib}
%define RT_WWWDIR		%{_datadir}/rt/html
%define RT_LOGDIR		/var/log/rt
%define RT_CACHEDIR		/var/cache/rt
%define RT_LOCALSTATEDIR	/var/lib/rt

Summary:	Request tracker 3
Name:		rt
Version:	3.8.1
Release:	%mkrel 5
Group:		System/Servers
License:	GPLv2+
URL:		http://www.bestpractical.com/rt
Source0:	http://www.bestpractical.com/pub/rt/release/rt-%{version}.tar.gz
Source3:	rt.conf.in
Source4:	README.fedora.in
Source5:	rt.logrotate.in
Patch0:		rt-3.8.1-config.diff
Patch1:		rt-3.4.1-I18N.diff
Patch2:		rt-3.8.1-Makefile.diff
Patch3:		rt-3.8.1-test-dependencies.diff
BuildArch:	noarch
# For Debian compatibility
Provides:	request-tracker3 = %{version}-%{release}
# This list is alpha sorted
BuildRequires: perl(Apache::DBI)
BuildRequires: perl(Apache::Session) >= 1.53
BuildRequires: perl(Cache::Simple::TimedExpiry)
BuildRequires: perl(Calendar::Simple)
BuildRequires: perl(CGI::Cookie) >= 1.20
BuildRequires: perl(Class::ReturnValue) >= 0.40
BuildRequires: perl(CPAN)
BuildRequires: perl(CSS::Squish) >= 0.06
BuildRequires: perl(Data::ICal)
BuildRequires: perl(Date::Format)
BuildRequires: perl(DBD::mysql) >= 2.1018
BuildRequires: perl(DBI) >= 1.37
BuildRequires: perl(DBIx::SearchBuilder) >= 1.54
BuildRequires: perl(Devel::StackTrace) >= 1.19
BuildRequires: perl(Digest::base)
BuildRequires: perl(Digest::MD5) >= 2.27
BuildRequires: perl(Email::Address)
BuildRequires: perl(Encode) >= 2.13
BuildRequires: perl(Errno)
%{?with_devel_mode:BuildRequires: perl(File::Find)}
BuildRequires: perl(File::Glob)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Spec) >= 0.8
BuildRequires: perl(File::Temp) >= 0.18
%{?with_gd:BuildRequires: perl(GD)}
%{?with_gd:BuildRequires: perl(GD::Graph)}
%{?with_gd:BuildRequires: perl(GD::Text)}
%{?with_gpg:BuildRequires: perl(GnuPG::Interface)}
%{?with_graphviz:BuildRequires: perl(GraphViz)}
BuildRequires: perl(Getopt::Long) >= 2.24
BuildRequires: perl(HTML::Entities)
%{?with_devel_mode:BuildRequires: perl(HTML::Form)}
BuildRequires: perl(HTML::FormatText)
BuildRequires: perl(HTML::Mason) >= 1.36
BuildRequires: perl(HTML::RewriteAttributes) >= 0.02
BuildRequires: perl(HTML::Scrubber) >= 0.08
BuildRequires: perl(HTML::TreeBuilder)
BuildRequires: perl(HTTP::Request::Common)
BuildRequires: perl(HTTP::Server::Simple) >= 0.34
BuildRequires: perl(HTTP::Server::Simple::Mason) >= 0.09
%{?with_graphviz:BuildRequires: perl(IPC::Run)}
%{?with_devel_mode:BuildRequires: perl(IPC::Run3)}
%{?with_graphviz:BuildRequires: perl(IPC::Run::SafeHandles)}
BuildRequires: perl(Locale::Maketext) >= 1.06
BuildRequires: perl(Locale::Maketext::Fuzzy)
BuildRequires: perl(Locale::Maketext::Lexicon) >= 0.32
BuildRequires: perl(Log::Dispatch) >= 2.0
%{?with_devel_mode:BuildRequires: perl(Log::Dispatch::Perl)}
BuildRequires: perl(LWP)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Mail::Mailer) >= 1.57
BuildRequires: perl(MIME::Entity) >= 5.425
BuildRequires: perl(MIME::Types)
%{?with_devel_mode:BuildRequires: perl(Module::Refresh) >= 0.03}
BuildRequires: perl(Module::Versions::Report) >= 1.05
BuildRequires: perl(Net::Server)
BuildRequires: perl(Net::Server::PreFork)
BuildRequires: perl(Net::SMTP)
%{?with_gpg:BuildRequires: perl(PerlIO::eol)}
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable) >= 2.08
%{?with_devel_mode:BuildRequires: perl(String::ShellQuote)}
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Term::ReadLine)
%{?with_devel_mode:BuildRequires: perl(Test::Builder) >= 0.77}
%{?with_devel_mode:BuildRequires: perl(Test::Deep)}
%{?with_devel_mode:BuildRequires: perl(Test::Expect) >= 0.31}
%{?with_devel_mode:BuildRequires: perl(Test::HTTP::Server::Simple) >= 0.09}
%{?with_devel_mode:BuildRequires: perl(Test::MockTime)}
%{?with_devel_mode:BuildRequires: perl(Test::Warn)}
%{?with_devel_mode:BuildRequires: perl(Test::WWW::Mechanize)}
BuildRequires: perl(Text::ParseWords)
BuildRequires: perl(Text::Quoted) >= 2.02
BuildRequires: perl(Text::Template)
BuildRequires: perl(Text::WikiFormat) >= 0.76
BuildRequires: perl(Text::Wrapper)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Time::ParseDate)
BuildRequires: perl(Tree::Simple) >= 1.04
BuildRequires: perl(UNIVERSAL::require)
%{?with_devel_mode:BuildRequires: perl(WWW::Mechanize)}
BuildRequires: perl(XML::RSS) >= 1.05
%{?with_devel_mode:BuildRequires: perl(XML::Simple)}
BuildRequires:	/usr/bin/pod2man
BuildRequires:	apache-devel
Requires(postun): /bin/rm
# rpm doesn't catch these:
Requires: perl(Apache::Session)
Requires: perl(Calendar::Simple)
%{?with_gd:Requires: perl(GD::Text)}
%{?with_gd:Requires: perl(GD::Graph::bars)}
%{?with_gd:Requires: perl(GD::Graph::pie)}
Requires: perl(HTTP::Server::Simple::Mason)
Requires: perl(I18N::LangTags::List)
Requires: perl(Locale::Maketext::Fuzzy)
Requires: perl(LWP::MediaTypes)
Requires: apache-mod_perl
Requires: perl(Module::Versions::Report)
Requires: perl(Tree::Simple)
Requires: perl(URI::URL)
# rpm fails to add these:
Provides: perl(RT::Shredder::Exceptions)
Provides: perl(RT::Shredder::Record)
Provides: perl(RT::Shredder::Transaction)
Provides: perl(RT::Tickets_Overlay_SQL)
# Split out. Technically, not actually necessary, but ... let's keep it for now.
Requires: rt-mailgate
%if %mdkversion < 201010
Requires(pre): rpm-helper
Requires(postun): rpm-helper
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
RT is an enterprise-grade ticketing system which enables a group of people
to intelligently and efficiently manage tasks, issues, and requests submitted
by a community of users.

%package mailgate
Summary: rt's mailgate utility
Group:   System/Servers
# rpm doesn't catch these:
Requires:	perl(Pod::Usage)
Requires:	perl(HTML::TreeBuilder)
Requires:	perl(HTML::FormatText)

%description mailgate
%{summary}

%prep
%setup -q -n rt-%{version}

sed -e 's,@RT_CACHEDIR@,%{RT_CACHEDIR},' %{SOURCE4} \
  > README.fedora
sed -e 's,@RT_LOGDIR@,%{RT_LOGDIR},' %{SOURCE5} \
  > rt.logrotate

# Fixup the tarball shipping with broken permissions
find . \( -name '*.pm' -o -name '*.pm.in' -o -name '*.po' -o -name '*.pod' \) \
  -exec chmod a-x {} \;
chmod -x UPGRADING README C* aclocal.* config.* *.ac *.in
find etc -type f -exec chmod a-x {} \;

%patch0 -p1
#%patch1 -p1
%patch2 -p1
%patch3 -p1

# Patch backups added by rpm disturb
find -name '*.orig' -exec rm -f {} \;

cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
    sed -e '/^perl(RT)$/d' \
    	-e '/^perl(HTML::Mason/d' \
	-e '/^perl(IO::Handle::CRLF)$/d'
EOF
%define __perl_provides %{_builddir}/rt-%{version}/%{name}-prov
chmod +x %{__perl_provides}

# Filter out a bogus R:perl() rpm adds.
# Keep SpamAssassin optional
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
    sed -e '/^perl()/d' \
	-e '/^perl(Mail::SpamAssassin)$/d'
EOF
%define __perl_requires %{_builddir}/rt-%{version}/%{name}-req
chmod +x %{__perl_requires}

# Propagate rpm's directories to config.layout
cat << \EOF >> config.layout

# Mandriva directory layout.
<Layout Mandriva>
  bindir:		%{RT_BINDIR}
  sysconfdir:		%{_sysconfdir}/rt
  libdir:		%{RT_LIBDIR}
  manualdir:		${datadir}/doc
  localstatedir:	%{RT_LOCALSTATEDIR}
  htmldir:		%{RT_WWWDIR}
  logfiledir:		%{RT_LOGDIR}
  masonstatedir:	%{RT_CACHEDIR}/mason_data
  sessionstatedir:	%{RT_CACHEDIR}/session_data
  customdir:		%{_prefix}/local/lib/rt
  custometcdir:		%{_prefix}/local/etc/rt
  customhtmldir:	${customdir}/html
  customlexdir:		${customdir}/po
  customlibdir:		${customdir}/lib
</Layout>
EOF

# Comment out the Makefile trying to change groups/owners
# Fix DESTDIR support
sed -i \
	-e 's,	chgrp,	: chrgp,g' \
	-e 's,	chown,	: chown,g' \
	-e 's,$(DESTDIR)/,$(DESTDIR),g' \
	-e 's,-o $(BIN_OWNER) -g $(RTGROUP),,g' \
Makefile.in

%build
%configure \
    --with-apachectl=/usr/sbin/apachectl \
    --with-web-user=apache \
    --with-web-group=apache \
    --enable-layout=Mandriva \
    --with-modperl2 \
    --with-web-handler=modperl2 \
    --libdir=%{RT_LIBDIR} \
    %{?with_graphviz:--enable-graphviz}%{!?with_graphviz:--disable-graphviz} \
    %{?with_gd:--enable-gd}%{!?with_gd:--disable-gd} \
    %{?with_gpg:--enable-gpg}%{!?with_gpg:--disable-gpg} \
    %{?with_devel_mode:--enable-devel-mode}%{!?with_devel_mode:--disable-devel-mode}

%make

# Generate man-pages
pod2man bin/rt-mailgate > bin/rt-mailgate.1
pod2man bin/mason_handler.fcgi > bin/mason_handler.fcgi.1

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

# Cleanup the mess rt's configuration leaves behind
rm -f %{buildroot}%{_docdir}/README

# Win32 stuff
rm -f %{buildroot}%{RT_BINDIR}/mason_handler.svc

# We don't want CPAN
rm -f %{buildroot}%{_sbindir}/rt-test-dependencies

# An installed testsuite without infrastructure
rm -rf %{buildroot}%{RT_LIBDIR}/t

# Bogus
rm -f %{buildroot}%{RT_LIBDIR}/RT.pm.in

# Unsupported
rm -f %{buildroot}%{RT_BINDIR}/*.scgi

# Install apache configuration
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
sed -e 's,@RT_WWWDIR@,%{RT_WWWDIR},g' \
  -e 's,@RT_BINDIR@,%{RT_BINDIR},g' \
  %{SOURCE3} > %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/rt.conf

mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 bin/rt-mailgate.1 bin/mason_handler.fcgi.1 \
  %{buildroot}%{_mandir}/man1

if [ "%{_bindir}" != "%{RT_BINDIR}" ]; then
  mkdir -p %{buildroot}%{_bindir}
  mv %{buildroot}%{RT_BINDIR}/rt \
    %{buildroot}%{_bindir}
fi

install -d -m755 %{buildroot}%{_prefix}/local/etc/rt
install -d -m755 %{buildroot}%{_prefix}/local/lib/rt
install -d -m755 %{buildroot}%{_prefix}/local/lib/rt/html
install -d -m755 %{buildroot}%{_prefix}/local/lib/rt/po
install -d -m755 %{buildroot}%{_prefix}/local/lib/rt/lib

install -d -m755 %{buildroot}%{RT_LOGDIR}

# install log rotation stuff
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 rt.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/rt

install -d -m755 %{buildroot}%{RT_LOCALSTATEDIR}

install -d -m755 %{buildroot}%{_sysconfdir}/rt/upgrade
cp -R etc/upgrade/* %{buildroot}%{_sysconfdir}/rt/upgrade
rm -f %{buildroot}%{_sysconfdir}/rt/upgrade/*.in

# Fix permissions
find %{buildroot}%{RT_WWWDIR} \
  -type f -exec chmod a-x {} \;

%check
# The tests don't work:
# - Require to be run as root
# - Require an operational rt system
# - Require packages which are n/a in Fedora
%{?with_tests:make test}

%post
%if %mdkversion < 201010
%_post_webapp
%endif
    
%postun
%if %mdkversion < 201010
%_postun_webapp
%endif
if [ "$1" = "0" ]; then
  /bin/rm -rf %{RT_CACHEDIR}
fi
                    
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README UPGRADING README.fedora
%{_bindir}/*
%{_sbindir}/*
%exclude %{_sbindir}/rt-mailgate
%{_mandir}/man1/*
%exclude %{_mandir}/man1/rt-mailgate*
%{RT_LIBDIR}/*
%exclude %{RT_LIBDIR}/RT/Test*
%attr(0700,apache,apache) %{RT_LOGDIR}

%dir %{_sysconfdir}/rt
%attr(-,root,root)%{_sysconfdir}/rt/upgrade
%attr(-,root,root)%{_sysconfdir}/rt/acl*
%attr(-,root,root)%{_sysconfdir}/rt/schema*
%attr(-,root,root)%{_sysconfdir}/rt/init*
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/rt/RT_*

%config(noreplace) %{_sysconfdir}/logrotate.d/rt

%dir %{_datadir}/rt
%{RT_WWWDIR}
%config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/rt.conf

%dir %{RT_CACHEDIR}
%attr(0770,apache,apache) %{RT_CACHEDIR}/mason_data
%attr(0770,apache,apache) %{RT_CACHEDIR}/session_data

%if "%{RT_LOCALSTATEDIR}" != "%{RT_CACHEDIR}"
%dir %{RT_LOCALSTATEDIR}
%endif

%ghost %{_prefix}/local/lib/rt
%ghost %{_prefix}/local/etc/rt

%files mailgate
%defattr(-,root,root,-)
%{_sbindir}/rt-mailgate
%{_mandir}/man1/rt-mailgate*
