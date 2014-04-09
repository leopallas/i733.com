#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'xw'
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value) in attrs:
                    if variable == "href":
                        self.links.append(value)

if __name__ == "__main__":
    fileHandle = open('template/index.html')
    html_code = fileHandle.read()
    fileHandle.close()

    hp = MyHTMLParser()
    hp.feed(html_code)
    hp.close()
    print(hp.links)