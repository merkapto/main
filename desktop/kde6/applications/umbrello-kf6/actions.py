#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde6
from pisi.actionsapi import get

NoStrip=["/usr/share"]

def setup():
    kde6.configure("-DBUILD_KF5=ON")

def build():
    kde6.make()

def install():
    kde6.install()
    
    pisitools.dodoc("COPYING*", "AUTHORS", "CODING-STYLE", "ChangeLog", "README", "THANKS", "TODO")
