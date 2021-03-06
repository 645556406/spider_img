# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderImgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img = scrapy.Field()
    MD5 = scrapy.Field()
    image_urls = scrapy.Field()

class SpiderGitlab(scrapy.Item):
    username = scrapy.Field()
    email = scrapy.Field()