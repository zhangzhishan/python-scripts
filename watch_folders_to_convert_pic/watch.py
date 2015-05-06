#!/usr/bin/env python
# coding=utf-8
# author=huhuhushan

import re
import pyinotify
import pic
import Image
import os
import time
wm = pyinotify.WatchManager()
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MOVED_TO
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        self.rebuild(event)
        self.picchange(event.pathname)
    def process_IN_MODIFY(self, event):
        self.rebuild(event)
        self.picchange(event.pathname)
    def process_IN_MOVE_SELF(self, event):
        self.rebuild(event)
        self.picchange(event.pathname)
    def process_IN_MOVED_TO(self, event):
        self.rebuild(event)
        self.picchange(event.pathname)
    def process_IN_MOVED_FROM(self, event):
        self.rebuild(event)
        self.picchange(event.pathname)
    def process_IN_DELETE(self, event):
        self.rebuild(event)
    def process_IN_CLOSE_WRITE(self, event):
        self.rebuild(event)
        self.picchange(event.pathname)
    def rebuild(self, event):
        chang_name=re.compile(".+\.swp$|.+\.swx$|.+\.swpx$")
        if not chang_name.match(event.pathname):
            print event.pathname
    def picchange(self, pathname):
        large_path = '/data/www/imgs/large/'
        small_path = '/data/www/imgs/small/'
        filename = os.path.basename(pathname)
        original_path = pathname
        time.sleep(1)
        print filename
        print pathname
        filename = os.path.splitext(filename)[0]
        file_extension = '.png'
        im = Image.open(original_path)
        print im
        new_im = pic.large(im)
        new_im.save(large_path + filename + file_extension)
        print '[*] large,ok! ' + filename
        new_im = pic.small(im)
        new_im.save(small_path + filename + file_extension)
        print '[*] small,ok ' + filename

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/data/www/imgs/original/', mask, rec=True,auto_add=True )
notifier.loop()
