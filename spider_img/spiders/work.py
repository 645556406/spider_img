import json

import scrapy


class WorkSpider(scrapy.Spider):
    name = 'work'
    allowed_domains = ['work.17doubao.com/user-login.html']
    start_urls = ['http://work.17doubao.com/user-login.html/']

    def parse(self, response):
        login_url = "http://git.banmamedia.net/users/sign_in"
        formdata = {
            "utf8": "✓",
            "authenticity_token": "tJ9v2LaKhyNdrzNcDCLy4OTNmFN3qa3hTPBVI0sz24RM5o4fUEHwq+BhvrmICCr2k/YV4WdAoShpEc8ScRSX6g==",
            "user[login]": "root",
            "user[password]": "!=banma.com2014git",
            "user[remember_me]": 0
        }
        yield scrapy.FormRequest(login_url, formdata=formdata, callback=self.parse_login)

    def parse_login(self, response):
        login_result = dict(json.load(response.body.decode()))
        print(login_result)
        # 登录成功后访问的目标地址
        member_url="http://git.banmamedia.net/admin/users"
        yield scrapy.Request(member_url, callback=self.parse_memeber)

    def parse_memeber(self, response):
        with open("work_renwu.html", 'wb') as f:
            f.write(response.body)
