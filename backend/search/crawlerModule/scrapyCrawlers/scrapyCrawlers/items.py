# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapycrawlersItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    desc = scrapy.Field()
    urlImg =scrapy.Field()
    attractionType = scrapy.Field()
    rating = scrapy.Field()
    genre = scrapy.Field()
    stream = scrapy.Field()
    
