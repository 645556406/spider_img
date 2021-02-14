# -*- coding: utf-8 -*-
import scrapy
import re
from spider_img.items import SpiderGitlab

class Github2Spider(scrapy.Spider):
    name = 'gitlab'
    allowed_domains = ['git.banmamedia.net']
    start_urls = ['http://git.banmamedia.net/users/sign_in']

    def parse(self, response):
        """
        登录gitlab
        :param response:
        :return:
        """
        yield scrapy.FormRequest.from_response(
            response, # 自动从response中寻找form表单
            formdata={
                "user[login]": "wangye",
                "user[password]": "Kxo5qcdUnPaRtwuUxYAR",
                "user[remember_me]": "0"
            },
            callback=self.after_login
        )
    # 登录成功之后操作
    def after_login(self, response):
        user_page_url = "http://git.banmamedia.net/admin/users"
        yield scrapy.Request(
            user_page_url,
            callback=self.get_gitlab_user
        )

    # 获取gitlab所有用户名和邮箱地址
    def get_gitlab_user(self, response):
        item = SpiderGitlab()
        li_list = response.xpath('//*[@id="content-body"]/div/ul/li')
        for li in li_list:
            item["username"] = li.xpath('div[2]/div[1]/a/text()').extract_first()
            item["email"] = li.xpath('div[2]/div[2]/a/text()').extract_first()
            print(item)
        # 翻页
        next_url = response.xpath('//*[@id="content-body"]/div/div[2]/ul/li[8]/@href').extract_first()
        if(next_url):
            next_url = "http://" + self.allowed_domains[0] + next_url
            yield scrapy.Request(
                next_url,
                callback=self.get_gitlab_user
            )
