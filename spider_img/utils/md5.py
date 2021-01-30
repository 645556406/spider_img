# -*- coding: utf-8 -*-
# @Time : 2021/1/29 21:49
# @Author : Administrator
# @Email : wangye@payweipan.com
# @File : md5.py.py
# @Project : python_spider
import hashlib

def item_md5(item):
    m = hashlib.md5()
    m.update(item.encode())
    item_md5 = m.hexdigest()
    return item_md5
