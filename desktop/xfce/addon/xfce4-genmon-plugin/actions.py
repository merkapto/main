#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	# fix build failure w/ xfce4-panel-4.15.0
#	pisitools.dosed("panel-plugin/main.c", "<libxfce4panel/xfce-panel-plugin.h>", "<libxfce4panel/libxfce4panel.h>")
#	pisitools.dosed("panel-plugin/config_gui.c", "<libxfce4panel/xfce-panel-plugin.h>", "<libxfce4panel/libxfce4panel.h>")
#	pisitools.dosed("panel-plugin/config_gui.h", "<libxfce4panel/xfce-panel-plugin.h>", "<libxfce4panel/libxfce4panel.h>")
	autotools.configure()

	pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README")

