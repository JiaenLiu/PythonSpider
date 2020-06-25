# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# define the fields for your item here like:
# name = scrapy.Field()
import scrapy


class DatascienceItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    types = scrapy.Field()
    price = scrapy.Field()
    sales = scrapy.Field()
    source = scrapy.Field()
    # way = scrapy.Field()
    url = scrapy.Field()
    salers = scrapy.Field()
    # loc = scrapy.Field()