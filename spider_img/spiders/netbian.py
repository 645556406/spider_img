import scrapy


class NetbianSpider(scrapy.Spider):
    name = 'netbian'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/']

    def parse(self, response):
        li_list = response.xpath('//*[@class="clearfix"]/li')
        for li in li_list:
            item = {}
            item["img"] =  "http://pic.netbian.com/" + li.xpath('//img/@src').extract_first()
            yield item
        # 翻页
        next_url = response.xpath('///*[@id="main"]/div[4]/a[8]/@href').extract_first()
        if next_url != "javascript:;":
            next_url = "http://pic.netbian.com/" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )