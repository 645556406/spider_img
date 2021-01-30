# -*- coding: utf-8 -*-
# @Time : 2021/1/28 13:52
# @Author : Administrator
# @Email : wangye@payweipan.com
# @File : mongdb.py.py
# @Project : python_spider

import pymongo

class MongoModel:
    def __init__(self):
        self.client = pymongo.MongoClient('49.233.214.123')
        self.db = self.client['spider_img']
        self.table = self.db['img']

    def process_item(self, item, spider):
        self.table.insert(dict(item))
        return item
