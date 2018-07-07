# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

from qunarspider.items import QunarspiderItem


class QunarspiderPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(host=settings['MONGODB_HOST'],
                                         port=settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collections = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        if isinstance(item, QunarspiderItem):
            self.collections.update({'id': item['id']},
                                    {'$set': item},
                                    True)
        return item
