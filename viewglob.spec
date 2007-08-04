Summary:	Filesystem visualization for Bash and Zsh
Summary(pl.UTF-8):	Wizualizacja systemu plików dla Basha i Zsh
Name:		viewglob
Version:	2.0.4
Release:	0.2
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
  of vgseer processes (local or remote) and a Viewglob display.
- vgmini and vgclassic, graphical displays: List the contents of
  directories relevant to the currently active shell, highlighting file
  selections and potential name completions.

A convenience script "viewglob" is provided as a startup shortcut.

%description -l pl.UTF-8
Viewglob to dodatek wizualizujący system plików dla Basha i Zsh.
Śledzi linię poleceń i środowisko dowolnej liczby interaktywnych
powłok (lokalnych i zdalnych). Graficzny wyświetlacz podąża za
aktualnie aktywnym terminalem, wyświetlając zawartość katalogów
odpowiednich dla tej powłoki i podświetlając dynamicznie wybory plików
oraz potencjalne dopełnienia nazw.

Ten pakiet ma trzy komunikujące się części:
- klient vgseer - nadzoruje powłokę interaktywną i śledzi zmiany linii
  poleceń oraz środowiska
- demon serwera vgd - pośredniczy wymianie danych między dowolną liczbą
  (lokalnych lub zdalnych) procesów vgseer i wyświetlaczem Viewgloba
- graficzne wyświetlacze vgmini i vgclassic - wyświetlają zawartości
  katalogów odpowiadające aktualnie aktywnym powłokom, podświetlając
  wybory plików i potencjalne dopełnienia nazw.

Jako ułatwienie uruchamiania dołączony jest skrypt "viewglob".

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
%attr(755,root,root) %{_bindir}/vgd
%attr(755,root,root) %{_bindir}/vgseer
%attr(755,root,root) %{_bindir}/viewglob
%dir %{_libdir}/viewglob
%{_libdir}/viewglob/.zshrc
%{_libdir}/viewglob/init-viewglob.bashrc
%attr(755,root,root) %{_libdir}/viewglob/conf-to-args.sh
%attr(755,root,root) %{_libdir}/viewglob/getopt.sh
%attr(755,root,root) %{_libdir}/viewglob/vgclassic
%attr(755,root,root) %{_libdir}/viewglob/vgexpand
%attr(755,root,root) %{_libdir}/viewglob/vgmini
%attr(755,root,root) %{_libdir}/viewglob/vgping
%{_mandir}/man?/*
