# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import requests

#from .spiders.anime import malDict


class ScrapycrawlersPipeline:
    def process_item(self, item, spider):
        self.i = item
        print(self.i)
        return item

    def close_spider(self,spider):
        print(self.i)
        r = requests.get('http://127.0.0.1:8000/list/anime/', data=self.i)
        print(r)
