# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class LagoumenuPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        sheetname = settings['MONGODB_SHEETNAME']
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.port = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.port.insert(data)
        return item

