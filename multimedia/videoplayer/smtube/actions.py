#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import qt5
from pisi.actionsapi import pisitools

def setup():
    #pisitools.dosed("Makefile", "^DOC_PATH=.*$", "DOC_PATH=$(PREFIX)/share/doc/smplayer")
    pisitools.dosed("Makefile", "PREFIX=/usr/local", "PREFIX=/usr")

def build():
    qt5.make()
    #autotools.make("PREFIX=/usr QMAKE=/usr/bin/qmake LRELEASE=/usr/bin/lrelease")

def install():
    qt5.install()
    #autotools.rawInstall("PREFIX=/usr DESTDIR=%s DOC_PATH=/usr/share/doc/%s" % (get.installDIR(),get.srcNAME()))
    pisitools.dodoc("Readme.txt","Release_notes.md","README.md","Copying.txt")
    
    pisitools.dosed("%s/usr/share/applications/smtube.desktop" % get.installDIR(), "Icon=smtube", "Icon=smtube.png")
