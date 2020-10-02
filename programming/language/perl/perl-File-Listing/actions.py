#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules


def setup():
    perlmodules.configure()


def build():
    perlmodules.make()


def check():
    perlmodules.make("test")


def install():
    perlmodules.install()
    pisitools.dodoc("README")
    pisitools.remove("/usr/share/man/man3/File::Listing.3pm")
