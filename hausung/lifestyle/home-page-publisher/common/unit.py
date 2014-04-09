#!/usr/local/bin/python
#coding=utf-8

__author__ = 'xw'
LIFE_THUMB_SMALL_NAME = "life-thumb-small"
LIFE_THUMB_MEDIUM_NAME = "life-thumb-medium"
LIFE_THUMB_LARGE_NAME = "life-thumb-large"
THUMB_SMALL_NAME = "thumb-small"


class FileUrl(object):
    def __init__(self):
        """
        获取图片的url地址
        """
        import sys
        self.__sys = sys

    def __md5_id(self, content):
        from hashlib import md5
        md5 = md5()
        md5.update(content)
        return md5.hexdigest()

    def __get_dir_list(self, dir_id):
        dir_list = []
        dir_hash = self.__md5_id(dir_id)
        for i in range(0, 6, 2):
            dir_list.append(dir_hash[i:i + 2])
        return dir_list

    def get_file_url(self, **kwargs):
        if 'domain' in kwargs:
            domain = kwargs['domain']
        else:
            print "\033[31;1m[Error]===> domain参数未指定\033[0m"
            return

        if 'file' in kwargs:
            file = kwargs['file']
        else:
            print "\033[31;1m[Error]===> domain参数未指定\033[0m"
            return

        file_id = file['id']
        if file_id is None:
            return

        if file['parentId'] is not None:
            dir_list = self.__get_dir_list(file['parentId'])
        else:
            dir_list = self.__get_dir_list(file_id)

        dir_list.append(file_id)

        file_name = "%s_%s%s" % (file_id, file['dimension'], file['type'])
        dir_list.append(file_name)

        uri = "/".join(dir_list)

        return "http://%s/%s" % (domain, uri)


class HtmlGenerator(object):
    def __init__(self, work_path, domain, db_conn, no_img_uri):
        """
        生成HTML片段
        """
        self.__work_path = work_path
        self.__domain = domain
        self.__conn = db_conn
        self.__no_img_uri = no_img_uri

    def __read_template_html(self, name):
        import os
        file = os.path.join(self.__work_path, name)
        fileHandle = open(file)
        templateHTML = fileHandle.read()
        fileHandle.close()
        return templateHTML

    def couponHTML(self, sql):
        templateHTML = self.__read_template_html('template/coupon.html')
        coupon_list = self.__conn.getAll(sql)
        couponHTML = ''
        url = FileUrl()
        for coupon in coupon_list:
            if coupon['ATTACHMENT_ID'] is None:
                coupon['URL'] = self.__no_img_uri
            else:
                img_file = {
                    'parentId': None,
                    'id': coupon['ATTACHMENT_ID'],
                    'type': coupon['EXTENSION_NAME'],
                    'dimension': LIFE_THUMB_MEDIUM_NAME,
                }
                coupon['URL'] = url.get_file_url(domain=self.__domain, file=img_file)
            couponHTML += templateHTML % coupon
        return couponHTML

    def houseHTML(self, sql):
        templateHTML = self.__read_template_html('template/house.html')

        house_list = self.__conn.getAll(sql)
        houseHTML = ''
        url = FileUrl()
        for house in house_list:
            if house['ATTACHMENT_ID'] is None:
                house['URL'] = self.__no_img_uri
            else:
                img_file = {
                    'parentId': None,
                    'id': house['ATTACHMENT_ID'],
                    'type': house['EXTENSION_NAME'],
                    'dimension': LIFE_THUMB_MEDIUM_NAME,
                }
                house['URL'] = url.get_file_url(domain=self.__domain, file=img_file)
            houseHTML += templateHTML % house
        return houseHTML

    def shopHTML(self, sql):
        templateHTML = self.__read_template_html('template/shop.html')

        shop_list = self.__conn.getAll(sql)
        shopHTML = ''
        url = FileUrl()
        for shop in shop_list:
            if shop['ATTACHMENT_ID'] is None:
                shop['URL'] = self.__no_img_uri
            else:
                img_file = {
                    'parentId': None,
                    'id': shop['ATTACHMENT_ID'],
                    'type': shop['EXTENSION_NAME'],
                    'dimension': LIFE_THUMB_MEDIUM_NAME,
                }
                shop['URL'] = url.get_file_url(domain=self.__domain, file=img_file)
            shopHTML += templateHTML % shop
        return shopHTML

    def secondhandHTML(self, sql):
        templateHTML = self.__read_template_html('template/second_hand.html')

        secondhand_list = self.__conn.getAll(sql)
        secondhandHTML = ''
        url = FileUrl()
        for secondhand in secondhand_list:
            if secondhand['ATTACHMENT_ID'] is None:
                secondhand['URL'] = self.__no_img_uri
            else:
                img_file = {
                    'parentId': None,
                    'id': secondhand['ATTACHMENT_ID'],
                    'type': secondhand['EXTENSION_NAME'],
                    'dimension': LIFE_THUMB_MEDIUM_NAME,
                }
                secondhand['URL'] = url.get_file_url(domain=self.__domain, file=img_file)
            secondhandHTML += templateHTML % secondhand
        return secondhandHTML


if __name__ == '__main__':
    task_id = '52390baae4b07f22a540c23c'
    attach_id = '52390baae4b07f22a540c23c'

    domain = "i.wjia.com.cn"

    IMG_FILE = {
        'parentId': None,
        'id': attach_id,
        'type': '.jpg',
        'dimension': THUMB_SMALL_NAME,
    }
    print FileUrl().get_file_url(domain=domain, file=IMG_FILE)