Summary:	Filesystem visualization for Bash and Zsh
Summary(pl.UTF-8):	Wizualizacja systemu plików dla Basha i Zsh
Name:		viewglob
Version:	2.0.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/viewglob/%{name}-%{version}.tar.gz
# Source0-md5:	7956a2e922a716bd0da30488e4ffb486
URL:		http://viewglob.sourceforge.net/
BuildRequires:	glib2-devel >= 1:2.2
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Viewglob is a filesystem visualization add-on for Bash and Zsh. It
tracks the command line and environment of any number of interactive
shells (local and remote). A graphical display follows the currently
active terminal, listing the contents of directories relevant to its
shell and highlighting file selections and potential name completions
dynamically.

The package has three communicating parts:
- vgseer, client: Supervises an interactive shell and keeps track of
  command line and environment changes.
- vgd, server daemon: Mediates information exchange between any number
  of vgseer pro- cesses (local or remote) and a Viewglob display.
- vgmini and vgclassic, graphical displays: List the contents of
  directories relevant to the currently active shell, highlighting file
  selections and potential name completions.

A convenience script "viewglob" is provided as a startup shortcut.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/viewglob
%{_mandir}/man?/*
