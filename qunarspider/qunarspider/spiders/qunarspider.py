from scrapy import Selector, Request
from scrapy.spiders import Spider

from qunarspider.items import QunarspiderItem

"""
爬取去哪儿网的精华游记
"""


class QuNarSpider(Spider):

    name = 'qunar'
    start_url = 'http://travel.qunar.com/travelbook/list.htm?page=%s'

    def start_requests(self):
        for i in range(1, 201):
            yield Request(url=self.start_url % i, callback=self.parse)

    def parse(self, response):
        item = QunarspiderItem()
        sel = Selector(response)
        lis = sel.xpath('/html/body/div[2]/div/div[2]/ul/li')

        for li in lis:
            # 游记id
            item['id'] = li.xpath('./@data-url').extract()[0].split('/')[-1]
            # 游记链接
            item['link'] = 'http://travel.qunar.com' + li.xpath('./h2/a/@href').extract()[0]
            # 用户头像
            # if li.xpath('./a/img/@src').extract():
            item['icon_src'] = li.xpath('./a/img/@src').extract()[0]
            # 游记标题
            item['title'] = li.xpath('./h2/a/text()').extract()[0]
            # 用户名
            item['user_name'] = li.xpath('.//span[@class="user_name"]/a/text()').extract()[0]
            # 相关简介
            item['intro'] = li.xpath('.//span[@class="intro"]/span/text()').extract()
            # 途径哪些地方
            item['places'] = li.xpath('.//p[@class="places"]/text()').extract()
            # 照片链接
            item['img_src'] = li.xpath('.//img[@alt="攻略图"]/@src').extract()

            yield item

