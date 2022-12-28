#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, mesontools, cmaketools, pisitools, get

j = ''.join([
    ' -DENABLE_EXAMPLES=ON',
    ' -DENABLE_MILTER=OFF',
    ' -DENABLE_SYSTEMD=OFF',
    ' -DAPP_CONFIG_DIRECTORY=/etc/clamav',
    ' -DDATABASE_DIRECTORY=/var/lib/clamav',
    ' -G Ninja',
    ' -B_build -L '
    ])

def setup():
    cmaketools.configure(j)

def build():
    mesontools.build("-C _build")

def check():
    #pass
    mesontools.build("-C _build test")

def install():
    mesontools.install("-C _build install")

    #pisitools.dodir("/run/clamav")
    pisitools.dodir("/var/lib/clamav")
    #pisitools.dodir("/var/log/clamav")

    shelltools.system("find %s/etc/clamav -type f | sed -e 'p;s:.sample::' | xargs -n2 mv" % get.installDIR())
