# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QunarspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()  # 游记id
    link = scrapy.Field()  # 游记链接
    icon_src = scrapy.Field()  # 用户头像
    title = scrapy.Field()  # 游记标题
    user_name = scrapy.Field()  # 用户名
    intro = scrapy.Field()  # 相关简介
    places = scrapy.Field()  # 途径哪些地方
    img_src = scrapy.Field()  # 照片链接
