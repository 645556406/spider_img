# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import scrapy
from itemadapter import ItemAdapter
class SpiderImgPipeline:

    def __init__(self):
        """
        初始化mongdb
        """
        self.client = pymongo.MongoClient('49.233.214.123')
        self.db = self.client['spider_img']
        self.table = self.db['img']

    def process_item(self, item, spider):
        """数据落地到mongodb"""
        if self.table.find({"MD5": item["MD5"]}).count() == 0:
            self.table.insert(dict(item))
            return item
