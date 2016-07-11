#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cups
Version  : elease
Release  : 6
URL      : https://github.com/apple/cups/archive/release-2.1.4.tar.gz
Source0  : https://github.com/apple/cups/archive/release-2.1.4.tar.gz
Summary  : CUPS
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 Zlib
Requires: cups-bin
Requires: cups-lib
Requires: cups-data
Requires: cups-doc
BuildRequires : Linux-PAM-dev
BuildRequires : dbus-dev
BuildRequires : krb5-dev
BuildRequires : libgcrypt-dev
BuildRequires : llvm-dev
BuildRequires : pkgconfig(com_err)
BuildRequires : pkgconfig(zlib)

%description
CUPS is the standards-based, open source printing system developed by
Apple Inc. for OS X and other UNIXÂ®-like operating systems.

%package bin
Summary: bin components for the cups package.
Group: Binaries
Requires: cups-data

%description bin
bin components for the cups package.


%package data
Summary: data components for the cups package.
Group: Data

%description data
data components for the cups package.


%package dev
Summary: dev components for the cups package.
Group: Development
Requires: cups-lib
Requires: cups-bin
Requires: cups-data
Provides: cups-devel

%description dev
dev components for the cups package.


%package doc
Summary: doc components for the cups package.
Group: Documentation

%description doc
doc components for the cups package.


%package lib
Summary: lib components for the cups package.
Group: Libraries
Requires: cups-data

%description lib
lib components for the cups package.


%prep
%setup -q -n cups-release-2.1.4

%build
export LANG=C
export CC=clang
export CXX=clang++
export LD=ld.gold
export CFLAGS="-g -O3 -feliminate-unused-debug-types  -pipe -Wall -D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wl,--copy-dt-needed-entries -m64 -march=westmere  -mtune=native -fasynchronous-unwind-tables -D_REENTRANT  -Wl,-z -Wl,now -Wl,-z -Wl,relro "
export CXXFLAGS=$CFLAGS
unset LDFLAGS
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/cups/backend/http
/usr/lib/cups/backend/ipp
/usr/lib/cups/backend/lpd
/usr/lib/cups/backend/snmp
/usr/lib/cups/backend/socket
/usr/lib/cups/backend/usb
/usr/lib/cups/cgi-bin/admin.cgi
/usr/lib/cups/cgi-bin/classes.cgi
/usr/lib/cups/cgi-bin/help.cgi
/usr/lib/cups/cgi-bin/jobs.cgi
/usr/lib/cups/cgi-bin/printers.cgi
/usr/lib/cups/daemon/cups-deviced
/usr/lib/cups/daemon/cups-driverd
/usr/lib/cups/daemon/cups-exec
/usr/lib/cups/daemon/cups-lpd
/usr/lib/cups/filter/commandtops
/usr/lib/cups/filter/gziptoany
/usr/lib/cups/filter/pstops
/usr/lib/cups/filter/rastertodymo
/usr/lib/cups/filter/rastertoepson
/usr/lib/cups/filter/rastertohp
/usr/lib/cups/filter/rastertolabel
/usr/lib/cups/filter/rastertopwg
/usr/lib/cups/monitor/bcp
/usr/lib/cups/monitor/tbcp
/usr/lib/cups/notifier/dbus
/usr/lib/cups/notifier/mailto
/usr/lib/cups/notifier/rss

%files bin
%defattr(-,root,root,-)
/usr/bin/accept
/usr/bin/cancel
/usr/bin/cups-config
/usr/bin/cupsaccept
/usr/bin/cupsaddsmb
/usr/bin/cupsctl
/usr/bin/cupsd
/usr/bin/cupsdisable
/usr/bin/cupsenable
/usr/bin/cupsfilter
/usr/bin/cupsreject
/usr/bin/cupstestdsc
/usr/bin/cupstestppd
/usr/bin/ipptool
/usr/bin/lp
/usr/bin/lpadmin
/usr/bin/lpc
/usr/bin/lpinfo
/usr/bin/lpmove
/usr/bin/lpoptions
/usr/bin/lpq
/usr/bin/lpr
/usr/bin/lprm
/usr/bin/lpstat
/usr/bin/ppdc
/usr/bin/ppdhtml
/usr/bin/ppdi
/usr/bin/ppdmerge
/usr/bin/ppdpo
/usr/bin/reject

%files data
%defattr(-,root,root,-)
/usr/share/cups/drv/sample.drv
/usr/share/cups/examples/color.drv
/usr/share/cups/examples/constraint.drv
/usr/share/cups/examples/custom.drv
/usr/share/cups/examples/grouping.drv
/usr/share/cups/examples/laserjet-basic.drv
/usr/share/cups/examples/laserjet-pjl.drv
/usr/share/cups/examples/minimum.drv
/usr/share/cups/examples/postscript.drv
/usr/share/cups/examples/r300-basic.drv
/usr/share/cups/examples/r300-colorman.drv
/usr/share/cups/examples/r300-remote.drv
/usr/share/cups/ipptool/color.jpg
/usr/share/cups/ipptool/create-printer-subscription.test
/usr/share/cups/ipptool/document-a4.pdf
/usr/share/cups/ipptool/document-a4.ps
/usr/share/cups/ipptool/document-letter.pdf
/usr/share/cups/ipptool/document-letter.ps
/usr/share/cups/ipptool/get-completed-jobs.test
/usr/share/cups/ipptool/get-jobs.test
/usr/share/cups/ipptool/get-notifications.test
/usr/share/cups/ipptool/get-printer-attributes.test
/usr/share/cups/ipptool/get-subscriptions.test
/usr/share/cups/ipptool/gray.jpg
/usr/share/cups/ipptool/ipp-1.1.test
/usr/share/cups/ipptool/ipp-2.0.test
/usr/share/cups/ipptool/ipp-2.1.test
/usr/share/cups/ipptool/ipp-2.2.test
/usr/share/cups/ipptool/ipp-everywhere.test
/usr/share/cups/ipptool/onepage-a4.pdf
/usr/share/cups/ipptool/onepage-a4.ps
/usr/share/cups/ipptool/onepage-letter.pdf
/usr/share/cups/ipptool/onepage-letter.ps
/usr/share/cups/ipptool/print-job-deflate.test
/usr/share/cups/ipptool/print-job-gzip.test
/usr/share/cups/ipptool/print-job.test
/usr/share/cups/ipptool/testfile.jpg
/usr/share/cups/ipptool/testfile.pcl
/usr/share/cups/ipptool/testfile.pdf
/usr/share/cups/ipptool/testfile.ps
/usr/share/cups/ipptool/testfile.txt
/usr/share/cups/ipptool/validate-job.test
/usr/share/cups/mime/mime.convs
/usr/share/cups/mime/mime.types
/usr/share/cups/ppdc/epson.h
/usr/share/cups/ppdc/font.defs
/usr/share/cups/ppdc/hp.h
/usr/share/cups/ppdc/label.h
/usr/share/cups/ppdc/media.defs
/usr/share/cups/ppdc/raster.defs
/usr/share/cups/templates/add-class.tmpl
/usr/share/cups/templates/add-printer.tmpl
/usr/share/cups/templates/add-rss-subscription.tmpl
/usr/share/cups/templates/admin.tmpl
/usr/share/cups/templates/choose-device.tmpl
/usr/share/cups/templates/choose-make.tmpl
/usr/share/cups/templates/choose-model.tmpl
/usr/share/cups/templates/choose-serial.tmpl
/usr/share/cups/templates/choose-uri.tmpl
/usr/share/cups/templates/class-added.tmpl
/usr/share/cups/templates/class-confirm.tmpl
/usr/share/cups/templates/class-deleted.tmpl
/usr/share/cups/templates/class-jobs-header.tmpl
/usr/share/cups/templates/class-modified.tmpl
/usr/share/cups/templates/class.tmpl
/usr/share/cups/templates/classes-header.tmpl
/usr/share/cups/templates/classes.tmpl
/usr/share/cups/templates/command.tmpl
/usr/share/cups/templates/de/add-class.tmpl
/usr/share/cups/templates/de/add-printer.tmpl
/usr/share/cups/templates/de/add-rss-subscription.tmpl
/usr/share/cups/templates/de/admin.tmpl
/usr/share/cups/templates/de/choose-device.tmpl
/usr/share/cups/templates/de/choose-make.tmpl
/usr/share/cups/templates/de/choose-model.tmpl
/usr/share/cups/templates/de/choose-serial.tmpl
/usr/share/cups/templates/de/choose-uri.tmpl
/usr/share/cups/templates/de/class-added.tmpl
/usr/share/cups/templates/de/class-confirm.tmpl
/usr/share/cups/templates/de/class-deleted.tmpl
/usr/share/cups/templates/de/class-jobs-header.tmpl
/usr/share/cups/templates/de/class-modified.tmpl
/usr/share/cups/templates/de/class.tmpl
/usr/share/cups/templates/de/classes-header.tmpl
/usr/share/cups/templates/de/classes.tmpl
/usr/share/cups/templates/de/command.tmpl
/usr/share/cups/templates/de/edit-config.tmpl
/usr/share/cups/templates/de/error-op.tmpl
/usr/share/cups/templates/de/error.tmpl
/usr/share/cups/templates/de/header.tmpl
/usr/share/cups/templates/de/help-header.tmpl
/usr/share/cups/templates/de/help-printable.tmpl
/usr/share/cups/templates/de/help-trailer.tmpl
/usr/share/cups/templates/de/job-cancel.tmpl
/usr/share/cups/templates/de/job-hold.tmpl
/usr/share/cups/templates/de/job-move.tmpl
/usr/share/cups/templates/de/job-moved.tmpl
/usr/share/cups/templates/de/job-release.tmpl
/usr/share/cups/templates/de/job-restart.tmpl
/usr/share/cups/templates/de/jobs-header.tmpl
/usr/share/cups/templates/de/jobs.tmpl
/usr/share/cups/templates/de/list-available-printers.tmpl
/usr/share/cups/templates/de/modify-class.tmpl
/usr/share/cups/templates/de/modify-printer.tmpl
/usr/share/cups/templates/de/norestart.tmpl
/usr/share/cups/templates/de/option-boolean.tmpl
/usr/share/cups/templates/de/option-conflict.tmpl
/usr/share/cups/templates/de/option-header.tmpl
/usr/share/cups/templates/de/option-pickmany.tmpl
/usr/share/cups/templates/de/option-pickone.tmpl
/usr/share/cups/templates/de/option-trailer.tmpl
/usr/share/cups/templates/de/pager.tmpl
/usr/share/cups/templates/de/printer-accept.tmpl
/usr/share/cups/templates/de/printer-added.tmpl
/usr/share/cups/templates/de/printer-cancel-jobs.tmpl
/usr/share/cups/templates/de/printer-configured.tmpl
/usr/share/cups/templates/de/printer-confirm.tmpl
/usr/share/cups/templates/de/printer-default.tmpl
/usr/share/cups/templates/de/printer-deleted.tmpl
/usr/share/cups/templates/de/printer-jobs-header.tmpl
/usr/share/cups/templates/de/printer-modified.tmpl
/usr/share/cups/templates/de/printer-reject.tmpl
/usr/share/cups/templates/de/printer-start.tmpl
/usr/share/cups/templates/de/printer-stop.tmpl
/usr/share/cups/templates/de/printer.tmpl
/usr/share/cups/templates/de/printers-header.tmpl
/usr/share/cups/templates/de/printers.tmpl
/usr/share/cups/templates/de/restart.tmpl
/usr/share/cups/templates/de/samba-export.tmpl
/usr/share/cups/templates/de/samba-exported.tmpl
/usr/share/cups/templates/de/search.tmpl
/usr/share/cups/templates/de/set-printer-options-header.tmpl
/usr/share/cups/templates/de/set-printer-options-trailer.tmpl
/usr/share/cups/templates/de/subscription-added.tmpl
/usr/share/cups/templates/de/subscription-canceled.tmpl
/usr/share/cups/templates/de/test-page.tmpl
/usr/share/cups/templates/de/trailer.tmpl
/usr/share/cups/templates/de/users.tmpl
/usr/share/cups/templates/edit-config.tmpl
/usr/share/cups/templates/error-op.tmpl
/usr/share/cups/templates/error.tmpl
/usr/share/cups/templates/es/add-class.tmpl
/usr/share/cups/templates/es/add-printer.tmpl
/usr/share/cups/templates/es/add-rss-subscription.tmpl
/usr/share/cups/templates/es/admin.tmpl
/usr/share/cups/templates/es/choose-device.tmpl
/usr/share/cups/templates/es/choose-make.tmpl
/usr/share/cups/templates/es/choose-model.tmpl
/usr/share/cups/templates/es/choose-serial.tmpl
/usr/share/cups/templates/es/choose-uri.tmpl
/usr/share/cups/templates/es/class-added.tmpl
/usr/share/cups/templates/es/class-confirm.tmpl
/usr/share/cups/templates/es/class-deleted.tmpl
/usr/share/cups/templates/es/class-jobs-header.tmpl
/usr/share/cups/templates/es/class-modified.tmpl
/usr/share/cups/templates/es/class.tmpl
/usr/share/cups/templates/es/classes-header.tmpl
/usr/share/cups/templates/es/classes.tmpl
/usr/share/cups/templates/es/command.tmpl
/usr/share/cups/templates/es/edit-config.tmpl
/usr/share/cups/templates/es/error-op.tmpl
/usr/share/cups/templates/es/error.tmpl
/usr/share/cups/templates/es/header.tmpl
/usr/share/cups/templates/es/help-header.tmpl
/usr/share/cups/templates/es/help-printable.tmpl
/usr/share/cups/templates/es/help-trailer.tmpl
/usr/share/cups/templates/es/job-cancel.tmpl
/usr/share/cups/templates/es/job-hold.tmpl
/usr/share/cups/templates/es/job-move.tmpl
/usr/share/cups/templates/es/job-moved.tmpl
/usr/share/cups/templates/es/job-release.tmpl
/usr/share/cups/templates/es/job-restart.tmpl
/usr/share/cups/templates/es/jobs-header.tmpl
/usr/share/cups/templates/es/jobs.tmpl
/usr/share/cups/templates/es/list-available-printers.tmpl
/usr/share/cups/templates/es/modify-class.tmpl
/usr/share/cups/templates/es/modify-printer.tmpl
/usr/share/cups/templates/es/norestart.tmpl
/usr/share/cups/templates/es/option-boolean.tmpl
/usr/share/cups/templates/es/option-conflict.tmpl
/usr/share/cups/templates/es/option-header.tmpl
/usr/share/cups/templates/es/option-pickmany.tmpl
/usr/share/cups/templates/es/option-pickone.tmpl
/usr/share/cups/templates/es/option-trailer.tmpl
/usr/share/cups/templates/es/pager.tmpl
/usr/share/cups/templates/es/printer-accept.tmpl
/usr/share/cups/templates/es/printer-added.tmpl
/usr/share/cups/templates/es/printer-cancel-jobs.tmpl
/usr/share/cups/templates/es/printer-configured.tmpl
/usr/share/cups/templates/es/printer-confirm.tmpl
/usr/share/cups/templates/es/printer-default.tmpl
/usr/share/cups/templates/es/printer-deleted.tmpl
/usr/share/cups/templates/es/printer-jobs-header.tmpl
/usr/share/cups/templates/es/printer-modified.tmpl
/usr/share/cups/templates/es/printer-reject.tmpl
/usr/share/cups/templates/es/printer-start.tmpl
/usr/share/cups/templates/es/printer-stop.tmpl
/usr/share/cups/templates/es/printer.tmpl
/usr/share/cups/templates/es/printers-header.tmpl
/usr/share/cups/templates/es/printers.tmpl
/usr/share/cups/templates/es/restart.tmpl
/usr/share/cups/templates/es/samba-export.tmpl
/usr/share/cups/templates/es/samba-exported.tmpl
/usr/share/cups/templates/es/search.tmpl
/usr/share/cups/templates/es/set-printer-options-header.tmpl
/usr/share/cups/templates/es/set-printer-options-trailer.tmpl
/usr/share/cups/templates/es/subscription-added.tmpl
/usr/share/cups/templates/es/subscription-canceled.tmpl
/usr/share/cups/templates/es/test-page.tmpl
/usr/share/cups/templates/es/trailer.tmpl
/usr/share/cups/templates/es/users.tmpl
/usr/share/cups/templates/header.tmpl
/usr/share/cups/templates/help-header.tmpl
/usr/share/cups/templates/help-printable.tmpl
/usr/share/cups/templates/help-trailer.tmpl
/usr/share/cups/templates/ja/add-class.tmpl
/usr/share/cups/templates/ja/add-printer.tmpl
/usr/share/cups/templates/ja/add-rss-subscription.tmpl
/usr/share/cups/templates/ja/admin.tmpl
/usr/share/cups/templates/ja/choose-device.tmpl
/usr/share/cups/templates/ja/choose-make.tmpl
/usr/share/cups/templates/ja/choose-model.tmpl
/usr/share/cups/templates/ja/choose-serial.tmpl
/usr/share/cups/templates/ja/choose-uri.tmpl
/usr/share/cups/templates/ja/class-added.tmpl
/usr/share/cups/templates/ja/class-confirm.tmpl
/usr/share/cups/templates/ja/class-deleted.tmpl
/usr/share/cups/templates/ja/class-jobs-header.tmpl
/usr/share/cups/templates/ja/class-modified.tmpl
/usr/share/cups/templates/ja/class.tmpl
/usr/share/cups/templates/ja/classes-header.tmpl
/usr/share/cups/templates/ja/classes.tmpl
/usr/share/cups/templates/ja/command.tmpl
/usr/share/cups/templates/ja/edit-config.tmpl
/usr/share/cups/templates/ja/error-op.tmpl
/usr/share/cups/templates/ja/error.tmpl
/usr/share/cups/templates/ja/header.tmpl
/usr/share/cups/templates/ja/help-header.tmpl
/usr/share/cups/templates/ja/help-printable.tmpl
/usr/share/cups/templates/ja/help-trailer.tmpl
/usr/share/cups/templates/ja/job-cancel.tmpl
/usr/share/cups/templates/ja/job-hold.tmpl
/usr/share/cups/templates/ja/job-move.tmpl
/usr/share/cups/templates/ja/job-moved.tmpl
/usr/share/cups/templates/ja/job-release.tmpl
/usr/share/cups/templates/ja/job-restart.tmpl
/usr/share/cups/templates/ja/jobs-header.tmpl
/usr/share/cups/templates/ja/jobs.tmpl
/usr/share/cups/templates/ja/list-available-printers.tmpl
/usr/share/cups/templates/ja/modify-class.tmpl
/usr/share/cups/templates/ja/modify-printer.tmpl
/usr/share/cups/templates/ja/norestart.tmpl
/usr/share/cups/templates/ja/option-boolean.tmpl
/usr/share/cups/templates/ja/option-conflict.tmpl
/usr/share/cups/templates/ja/option-header.tmpl
/usr/share/cups/templates/ja/option-pickmany.tmpl
/usr/share/cups/templates/ja/option-pickone.tmpl
/usr/share/cups/templates/ja/option-trailer.tmpl
/usr/share/cups/templates/ja/pager.tmpl
/usr/share/cups/templates/ja/printer-accept.tmpl
/usr/share/cups/templates/ja/printer-added.tmpl
/usr/share/cups/templates/ja/printer-cancel-jobs.tmpl
/usr/share/cups/templates/ja/printer-configured.tmpl
/usr/share/cups/templates/ja/printer-confirm.tmpl
/usr/share/cups/templates/ja/printer-default.tmpl
/usr/share/cups/templates/ja/printer-deleted.tmpl
/usr/share/cups/templates/ja/printer-jobs-header.tmpl
/usr/share/cups/templates/ja/printer-modified.tmpl
/usr/share/cups/templates/ja/printer-reject.tmpl
/usr/share/cups/templates/ja/printer-start.tmpl
/usr/share/cups/templates/ja/printer-stop.tmpl
/usr/share/cups/templates/ja/printer.tmpl
/usr/share/cups/templates/ja/printers-header.tmpl
/usr/share/cups/templates/ja/printers.tmpl
/usr/share/cups/templates/ja/restart.tmpl
/usr/share/cups/templates/ja/samba-export.tmpl
/usr/share/cups/templates/ja/samba-exported.tmpl
/usr/share/cups/templates/ja/search.tmpl
/usr/share/cups/templates/ja/set-printer-options-header.tmpl
/usr/share/cups/templates/ja/set-printer-options-trailer.tmpl
/usr/share/cups/templates/ja/subscription-added.tmpl
/usr/share/cups/templates/ja/subscription-canceled.tmpl
/usr/share/cups/templates/ja/test-page.tmpl
/usr/share/cups/templates/ja/trailer.tmpl
/usr/share/cups/templates/ja/users.tmpl
/usr/share/cups/templates/job-cancel.tmpl
/usr/share/cups/templates/job-hold.tmpl
/usr/share/cups/templates/job-move.tmpl
/usr/share/cups/templates/job-moved.tmpl
/usr/share/cups/templates/job-release.tmpl
/usr/share/cups/templates/job-restart.tmpl
/usr/share/cups/templates/jobs-header.tmpl
/usr/share/cups/templates/jobs.tmpl
/usr/share/cups/templates/list-available-printers.tmpl
/usr/share/cups/templates/modify-class.tmpl
/usr/share/cups/templates/modify-printer.tmpl
/usr/share/cups/templates/norestart.tmpl
/usr/share/cups/templates/option-boolean.tmpl
/usr/share/cups/templates/option-conflict.tmpl
/usr/share/cups/templates/option-header.tmpl
/usr/share/cups/templates/option-pickmany.tmpl
/usr/share/cups/templates/option-pickone.tmpl
/usr/share/cups/templates/option-trailer.tmpl
/usr/share/cups/templates/pager.tmpl
/usr/share/cups/templates/printer-accept.tmpl
/usr/share/cups/templates/printer-added.tmpl
/usr/share/cups/templates/printer-cancel-jobs.tmpl
/usr/share/cups/templates/printer-configured.tmpl
/usr/share/cups/templates/printer-confirm.tmpl
/usr/share/cups/templates/printer-default.tmpl
/usr/share/cups/templates/printer-deleted.tmpl
/usr/share/cups/templates/printer-jobs-header.tmpl
/usr/share/cups/templates/printer-modified.tmpl
/usr/share/cups/templates/printer-reject.tmpl
/usr/share/cups/templates/printer-start.tmpl
/usr/share/cups/templates/printer-stop.tmpl
/usr/share/cups/templates/printer.tmpl
/usr/share/cups/templates/printers-header.tmpl
/usr/share/cups/templates/printers.tmpl
/usr/share/cups/templates/pt_BR/add-class.tmpl
/usr/share/cups/templates/pt_BR/add-printer.tmpl
/usr/share/cups/templates/pt_BR/add-rss-subscription.tmpl
/usr/share/cups/templates/pt_BR/admin.tmpl
/usr/share/cups/templates/pt_BR/choose-device.tmpl
/usr/share/cups/templates/pt_BR/choose-make.tmpl
/usr/share/cups/templates/pt_BR/choose-model.tmpl
/usr/share/cups/templates/pt_BR/choose-serial.tmpl
/usr/share/cups/templates/pt_BR/choose-uri.tmpl
/usr/share/cups/templates/pt_BR/class-added.tmpl
/usr/share/cups/templates/pt_BR/class-confirm.tmpl
/usr/share/cups/templates/pt_BR/class-deleted.tmpl
/usr/share/cups/templates/pt_BR/class-jobs-header.tmpl
/usr/share/cups/templates/pt_BR/class-modified.tmpl
/usr/share/cups/templates/pt_BR/class.tmpl
/usr/share/cups/templates/pt_BR/classes-header.tmpl
/usr/share/cups/templates/pt_BR/classes.tmpl
/usr/share/cups/templates/pt_BR/command.tmpl
/usr/share/cups/templates/pt_BR/edit-config.tmpl
/usr/share/cups/templates/pt_BR/error-op.tmpl
/usr/share/cups/templates/pt_BR/error.tmpl
/usr/share/cups/templates/pt_BR/header.tmpl
/usr/share/cups/templates/pt_BR/help-header.tmpl
/usr/share/cups/templates/pt_BR/job-cancel.tmpl
/usr/share/cups/templates/pt_BR/job-hold.tmpl
/usr/share/cups/templates/pt_BR/job-move.tmpl
/usr/share/cups/templates/pt_BR/job-moved.tmpl
/usr/share/cups/templates/pt_BR/job-release.tmpl
/usr/share/cups/templates/pt_BR/job-restart.tmpl
/usr/share/cups/templates/pt_BR/jobs-header.tmpl
/usr/share/cups/templates/pt_BR/jobs.tmpl
/usr/share/cups/templates/pt_BR/list-available-printers.tmpl
/usr/share/cups/templates/pt_BR/modify-class.tmpl
/usr/share/cups/templates/pt_BR/modify-printer.tmpl
/usr/share/cups/templates/pt_BR/norestart.tmpl
/usr/share/cups/templates/pt_BR/option-boolean.tmpl
/usr/share/cups/templates/pt_BR/option-conflict.tmpl
/usr/share/cups/templates/pt_BR/option-header.tmpl
/usr/share/cups/templates/pt_BR/option-pickmany.tmpl
/usr/share/cups/templates/pt_BR/option-pickone.tmpl
/usr/share/cups/templates/pt_BR/option-trailer.tmpl
/usr/share/cups/templates/pt_BR/pager.tmpl
/usr/share/cups/templates/pt_BR/printer-accept.tmpl
/usr/share/cups/templates/pt_BR/printer-added.tmpl
/usr/share/cups/templates/pt_BR/printer-configured.tmpl
/usr/share/cups/templates/pt_BR/printer-confirm.tmpl
/usr/share/cups/templates/pt_BR/printer-default.tmpl
/usr/share/cups/templates/pt_BR/printer-deleted.tmpl
/usr/share/cups/templates/pt_BR/printer-jobs-header.tmpl
/usr/share/cups/templates/pt_BR/printer-modified.tmpl
/usr/share/cups/templates/pt_BR/printer-reject.tmpl
/usr/share/cups/templates/pt_BR/printer-start.tmpl
/usr/share/cups/templates/pt_BR/printer-stop.tmpl
/usr/share/cups/templates/pt_BR/printer.tmpl
/usr/share/cups/templates/pt_BR/printers-header.tmpl
/usr/share/cups/templates/pt_BR/printers.tmpl
/usr/share/cups/templates/pt_BR/restart.tmpl
/usr/share/cups/templates/pt_BR/samba-export.tmpl
/usr/share/cups/templates/pt_BR/samba-exported.tmpl
/usr/share/cups/templates/pt_BR/search.tmpl
/usr/share/cups/templates/pt_BR/set-printer-options-header.tmpl
/usr/share/cups/templates/pt_BR/set-printer-options-trailer.tmpl
/usr/share/cups/templates/pt_BR/subscription-added.tmpl
/usr/share/cups/templates/pt_BR/subscription-canceled.tmpl
/usr/share/cups/templates/pt_BR/test-page.tmpl
/usr/share/cups/templates/pt_BR/trailer.tmpl
/usr/share/cups/templates/pt_BR/users.tmpl
/usr/share/cups/templates/restart.tmpl
/usr/share/cups/templates/ru/add-class.tmpl
/usr/share/cups/templates/ru/add-printer.tmpl
/usr/share/cups/templates/ru/add-rss-subscription.tmpl
/usr/share/cups/templates/ru/admin.tmpl
/usr/share/cups/templates/ru/choose-device.tmpl
/usr/share/cups/templates/ru/choose-make.tmpl
/usr/share/cups/templates/ru/choose-model.tmpl
/usr/share/cups/templates/ru/choose-serial.tmpl
/usr/share/cups/templates/ru/choose-uri.tmpl
/usr/share/cups/templates/ru/class-added.tmpl
/usr/share/cups/templates/ru/class-confirm.tmpl
/usr/share/cups/templates/ru/class-deleted.tmpl
/usr/share/cups/templates/ru/class-jobs-header.tmpl
/usr/share/cups/templates/ru/class-modified.tmpl
/usr/share/cups/templates/ru/class.tmpl
/usr/share/cups/templates/ru/classes-header.tmpl
/usr/share/cups/templates/ru/classes.tmpl
/usr/share/cups/templates/ru/command.tmpl
/usr/share/cups/templates/ru/edit-config.tmpl
/usr/share/cups/templates/ru/error-op.tmpl
/usr/share/cups/templates/ru/error.tmpl
/usr/share/cups/templates/ru/header.tmpl
/usr/share/cups/templates/ru/help-header.tmpl
/usr/share/cups/templates/ru/help-printable.tmpl
/usr/share/cups/templates/ru/help-trailer.tmpl
/usr/share/cups/templates/ru/job-cancel.tmpl
/usr/share/cups/templates/ru/job-hold.tmpl
/usr/share/cups/templates/ru/job-move.tmpl
/usr/share/cups/templates/ru/job-moved.tmpl
/usr/share/cups/templates/ru/job-release.tmpl
/usr/share/cups/templates/ru/job-restart.tmpl
/usr/share/cups/templates/ru/jobs-header.tmpl
/usr/share/cups/templates/ru/jobs.tmpl
/usr/share/cups/templates/ru/list-available-printers.tmpl
/usr/share/cups/templates/ru/modify-class.tmpl
/usr/share/cups/templates/ru/modify-printer.tmpl
/usr/share/cups/templates/ru/norestart.tmpl
/usr/share/cups/templates/ru/option-boolean.tmpl
/usr/share/cups/templates/ru/option-conflict.tmpl
/usr/share/cups/templates/ru/option-header.tmpl
/usr/share/cups/templates/ru/option-pickmany.tmpl
/usr/share/cups/templates/ru/option-pickone.tmpl
/usr/share/cups/templates/ru/option-trailer.tmpl
/usr/share/cups/templates/ru/pager.tmpl
/usr/share/cups/templates/ru/printer-accept.tmpl
/usr/share/cups/templates/ru/printer-added.tmpl
/usr/share/cups/templates/ru/printer-cancel-jobs.tmpl
/usr/share/cups/templates/ru/printer-configured.tmpl
/usr/share/cups/templates/ru/printer-confirm.tmpl
/usr/share/cups/templates/ru/printer-default.tmpl
/usr/share/cups/templates/ru/printer-deleted.tmpl
/usr/share/cups/templates/ru/printer-jobs-header.tmpl
/usr/share/cups/templates/ru/printer-modified.tmpl
/usr/share/cups/templates/ru/printer-reject.tmpl
/usr/share/cups/templates/ru/printer-start.tmpl
/usr/share/cups/templates/ru/printer-stop.tmpl
/usr/share/cups/templates/ru/printer.tmpl
/usr/share/cups/templates/ru/printers-header.tmpl
/usr/share/cups/templates/ru/printers.tmpl
/usr/share/cups/templates/ru/restart.tmpl
/usr/share/cups/templates/ru/samba-export.tmpl
/usr/share/cups/templates/ru/samba-exported.tmpl
/usr/share/cups/templates/ru/search.tmpl
/usr/share/cups/templates/ru/set-printer-options-header.tmpl
/usr/share/cups/templates/ru/set-printer-options-trailer.tmpl
/usr/share/cups/templates/ru/subscription-added.tmpl
/usr/share/cups/templates/ru/subscription-canceled.tmpl
/usr/share/cups/templates/ru/test-page.tmpl
/usr/share/cups/templates/ru/trailer.tmpl
/usr/share/cups/templates/ru/users.tmpl
/usr/share/cups/templates/samba-export.tmpl
/usr/share/cups/templates/samba-exported.tmpl
/usr/share/cups/templates/search.tmpl
/usr/share/cups/templates/set-printer-options-header.tmpl
/usr/share/cups/templates/set-printer-options-trailer.tmpl
/usr/share/cups/templates/subscription-added.tmpl
/usr/share/cups/templates/subscription-canceled.tmpl
/usr/share/cups/templates/test-page.tmpl
/usr/share/cups/templates/trailer.tmpl
/usr/share/cups/templates/users.tmpl
/usr/share/locale/ca/cups_ca.po
/usr/share/locale/cs/cups_cs.po
/usr/share/locale/de/cups_de.po
/usr/share/locale/es/cups_es.po
/usr/share/locale/fr/cups_fr.po
/usr/share/locale/it/cups_it.po
/usr/share/locale/ja/cups_ja.po
/usr/share/locale/pt_BR/cups_pt_BR.po
/usr/share/locale/ru/cups_ru.po

%files dev
%defattr(-,root,root,-)
/usr/include/cups/adminutil.h
/usr/include/cups/array.h
/usr/include/cups/backend.h
/usr/include/cups/cgi.h
/usr/include/cups/cups.h
/usr/include/cups/dir.h
/usr/include/cups/file.h
/usr/include/cups/help-index.h
/usr/include/cups/http.h
/usr/include/cups/ipp.h
/usr/include/cups/language.h
/usr/include/cups/mime.h
/usr/include/cups/ppd.h
/usr/include/cups/ppdc.h
/usr/include/cups/pwg.h
/usr/include/cups/raster.h
/usr/include/cups/sidechannel.h
/usr/include/cups/transcode.h
/usr/include/cups/versioning.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/cups/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
