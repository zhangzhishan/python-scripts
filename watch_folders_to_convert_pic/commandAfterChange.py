#!/usr/bin/env python
# coding=utf-8
# author=huhuhushan

import re
import pyinotify
import os
import time
wm = pyinotify.WatchManager()
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MOVED_TO


class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        self.rebuild(event)
        self.executeCommand(event.pathname)

    def process_IN_MODIFY(self, event):
        self.rebuild(event)
        self.executeCommand(event.pathname)

    def process_IN_MOVE_SELF(self, event):
        self.rebuild(event)
        self.executeCommand(event.pathname)

    def process_IN_MOVED_TO(self, event):
        self.rebuild(event)
        self.executeCommand(event.pathname)

    def process_IN_MOVED_FROM(self, event):
        self.rebuild(event)
        self.executeCommand(event.pathname)

    def process_IN_DELETE(self, event):
        self.rebuild(event)

    def process_IN_CLOSE_WRITE(self, event):
        self.rebuild(event)
        self.executeCommand(event.pathname)

    def rebuild(self, event):
        chang_name=re.compile(".+\.swp$|.+\.swx$|.+\.swpx$")
        if not chang_name.match(event.pathname):
            print event.pathname

    def executeCommand(self, pathname):
        large_path = '/data/www/imgs/large/'
        small_path = '/data/www/imgs/small/'
        filename = os.path.basename(pathname)
        original_path = pathname
        time.sleep(10)
        print filename
        print pathname
        os.system("ls")
        filename = os.path.splitext(filename)[0]
        file_extension = '.png'
        k = 0
        while k <= 1000:
            try:
                print '[+] ok!' + filename
                print '[+] small,ok' + filename
                k = 1000
            except Exception:
                k = k + 1
                pass

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('~/code/', mask, rec=True, auto_add=True)
notifier.loop()
