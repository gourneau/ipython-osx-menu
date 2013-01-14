#!/usr/bin/python

"""
A little script to run iPython notebook from the OS X system menu
"""

import objc
from Foundation import *
from AppKit import *
from PyObjCTools import AppHelper
import multiprocessing
import subprocess
import time
import sys
import webbrowser
import os

proc = False

class MyApp(NSApplication):
        
    def finishLaunching(self):      
        # Make statusbar item
        statusbar = NSStatusBar.systemStatusBar()
        self.statusitem = statusbar.statusItemWithLength_(NSVariableStatusItemLength)
        self.icon = NSImage.alloc().initByReferencingFile_(os.path.join(os.path.abspath(os.path.dirname(__file__)),'beaker.png'))
        self.icon.setScalesWhenResized_(True)
        self.icon.setSize_((20, 20))
        self.statusitem.setImage_(self.icon)
        # Let it highlight upon clicking
        self.statusitem.setHighlightMode_(1)
        
        #make the menu
        self.menubarMenu = NSMenu.alloc().init()

        self.browser = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Open in browser', 'browser:', '')
        self.menubarMenu.addItem_(self.browser)
        
        self.quit = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Quit', 'close:', '')
        self.menubarMenu.addItem_(self.quit)

        #add menu to statusitem
        self.statusitem.setMenu_(self.menubarMenu)
        self.statusitem.setToolTip_('My App')
        

    def clicked_(self, notification):
        print 'poll =', proc.poll(), '("None" means process not terminated yet)'


    def close_(self, notification):
        global proc
        if proc:
            subprocess.call(["kill", "-9", "%d" % proc.pid])
            proc.wait()
        NSApp.terminate_(None)

    def browser_(self,notification):
        webbrowser.open_new_tab("http://localhost:8888")

def startNotebook():
    global proc
    if not proc:
        #print "starting"
        proc = subprocess.Popen(["/usr/bin/python", "/usr/local/bin/ipython", "notebook", "--pylab", "inline", "--no-browser"], shell=False)


if __name__ == "__main__":
    startNotebook()
    app = MyApp.sharedApplication()
    AppHelper.runEventLoop()
