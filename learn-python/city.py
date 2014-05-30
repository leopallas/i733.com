#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-19 11:49
# Copyright 2014 LEO
import xml.dom.minidom
import os


def get_citys():
    city_xml = open(os.path.join(os.path.normpath(os.path.dirname(__file__)),'city.xml'))
    doc = xml.dom.minidom.parse(city_xml)
    citys = []
    provinces = doc.getElementsByTagName('province')
    for item in provinces:
        entry = {'province':'','citys':[]}
        province = item.getAttribute('name')
        entry['province'] = province
        for city in item.getElementsByTagName('city'):
            city = city.getAttribute('name')
            entry['citys'].append(city)
        citys.append(entry)
    return citys

if __name__ == '__main__':
    print get_citys()