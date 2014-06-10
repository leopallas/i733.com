#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-06-05 16:44
# Copyright 2014 LEO

from tornado.web import authenticated
from blog.handler.basic import BaseHandler
#from ckfinder_sae import CkFinder
from ckfinder import CkFinder


class FileListHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render("filemanager/index.html")


class DirListHandler(BaseHandler):
    @authenticated
    def post(self):
        ckfinder = CkFinder()
        self.write(ckfinder.dirlist(self.request))


class GetInfoHandler(BaseHandler):
    @authenticated
    def post(self):
        ckfinder = CkFinder()
        upload_path = self.get_argument("currentpath", "")
        file = self.request.files["newfile"]
        self.write(ckfinder.upload(upload_path, file))

    @authenticated
    def get(self):
        ckfinder = CkFinder()
        action = self.get_argument("mode", "")
        if "getinfo" == action:
            info = ckfinder.get_info(self.get_argument("path", ""))
            self.write(info)

        elif "getfolder" == action:
            self.write(ckfinder.get_dir_file(self.get_argument("path", "")))

        elif "rename" == action:
            old_name = self.get_argument("old", "")
            new_name = self.get_argument("new", "")
            self.write(ckfinder.rename(old_name, new_name))

        elif "delete" == action:
            path = self.get_argument("path", "")
            self.write(ckfinder.delete(path))

        elif "addfolder" == action:
            path = self.get_argument("path", "")
            name = self.get_argument("name", "")
            self.write(ckfinder.addfolder(path, name))

        else:
            self.write("fail")

