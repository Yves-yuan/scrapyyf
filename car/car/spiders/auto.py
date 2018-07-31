# coding=utf-8
import scrapy


class AutoSpider(scrapy.spiders.Spider):
    name = 'auto'
    allowedDomain = ['autohome.com']
    start_urls = ['https://www.autohome.com.cn/chengdu/']

    def parse(self, response):
        # print(response, type(response))
        # from scrapy.http.response.html import HtmlResponse
        # print(response.body_as_unicode())

        current_url = response.url  # 爬取时请求的url
        body = response.body  # 返回的html
        unicode_body = response.body_as_unicode()  # 返回的html unicode编码
        print(current_url)
        print(body)
        print(unicode_body)
