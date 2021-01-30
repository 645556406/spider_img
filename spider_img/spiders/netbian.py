import scrapy

from spider_img.utils.md5 import item_md5


class NetbianSpider(scrapy.Spider):
    name = 'netbian'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/4kmeinv']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="clearfix"]/li')
        for li in li_list:
            item = {}
            item["img"] = "http://pic.netbian.com" + li.xpath('a/img/@src').extract_first()
            # MD5加密图片链接地址作为下次爬取重复
            item_md5(item["img"])
            item["MD5"] = item_md5(item["img"])
            yield item
        # 翻页
        next_url = response.xpath('//*[@id="main"]/div[4]/a[5]/@href').extract_first()
        if(next_url):
            next_url = "http://pic.netbian.com" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )