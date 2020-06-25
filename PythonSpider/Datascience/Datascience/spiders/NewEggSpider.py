from urllib import parse
# from lxml import etree
import json
import time
import scrapy_splash
from scrapy_splash import SplashRequest
from scrapy.selector import Selector
# import requests
import re
import random
from fake_useragent import UserAgent
from Datascience.items import DatascienceItem
import scrapy
import logging

logging.info("一般信息")
logging.warning("警告信息")
logging.error("错误信息")

# Not Tested

class NewEggSpider(scrapy.Spider):
    name = 'NewEgg'
    allowed_domains = [
        'newegg.com'
    ]

    base_url = 'https://www.newegg.com/p/pl?N=100161551&d={key_word}&page={page_num}'

    def start_requests(self):
        key_words = self.settings['KEY_WORDS']
        page_num = self.settings['PAGE_NUM']
        ua = UserAgent()
        for key_word in key_words:
            # print(key_word)
            for i in range(1,page_num):
                header = {
                    'User-Agent':ua.random
                }
                url = self.base_url.format(key_word=key_word,page_num=str(i))
                yield scrapy.Request(url,callback=self.parse,headers=header)

    def parse(self,response):
        # //*[@id="baBreadcrumbTop"]/li[3]/a
        types = response.xpath('//*[@id="baBreadcrumbTop"]/li[3]/a/text()').get()
        ItemFrame = response.xpath('//div[@class="items-view is-grid"]/div[@class="item-container"]')
        ua = UserAgent()
        for items in ItemFrame:
            print(items)
            item = DatascienceItem()
            # 
            header = {
                    'User-Agent':ua.random
                }
            description_list = response.xpath('//ul[@class="item-features"]//text()').getall()
            item['description'] = ''
            for description in description_list:
                item['description'] = item['description']  + description
            item['name'] = items.xpath('//a[@class="item-title"]/text()').get()
            print(item['name'])
            item['price'] = items.xpath('//a[@class="price-current"]/strong/text()').get()
            print(item['price'])
            item['types'] = types
            item['sales'] = -1
            item['source'] = 'NewEgg'
            item['url'] = items.xpath('//div[@class="item-info"]/a/@href').get()
            print(item['url'])
            yield SplashRequest(url=item['url'],callback=self.parse_detail,meta={'item':item},headers=header,args={'wait':10})
    
    def parse_detail(self,response):
        item = response.meta['item']
        item['salers'] = response.xpath('//div[@class="featured-seller"]/div/strong/text()').get()
        yield item
        print(item)
        





            





