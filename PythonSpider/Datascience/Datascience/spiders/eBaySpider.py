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

class eBaySpider(scrapy.Spider):
    name = 'eBay'
    allowed_domains = [
        'ebay.com'
    ]

    # def __init__(self):
    #     self.bro = ''

    base_url = 'https://www.ebay.com/sch/i.html?_nkw={key_words}&_sacat=0&_sop=10&_pgn={page_num}&_ipg=200'

    def start_requests(self):
        key_words = self.settings['KEY_WORDS']
        page_nums = self.settings['PAGE_NUM']
        ua = UserAgent()
        for key_word in key_words:
            for i in range(1,page_nums):
                header = {
                    'User-Agent':ua.random
                }
                url = self.base_url.format(key_words=key_word,page_num=str(i))
                yield scrapy.Request(url,callback=self.parse,headers=header)

    def parse(self,response):
        # //*[@id="srp-river-results"]/ul/li/div/div[2]/div[4]/div[1]/span
        # price_list = response.selector.xpath('//span[@class="s-item__price"][1]/text()').extract()
        # print(price_list)
        splah_args = {
        "lua_source": """
        function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(8))

          splash.images_enabled = false
          return {
            html = splash:html(),
          }
        end
        """
        }
        name_list = response.selector.xpath('//h3[@class="s-item__title"]/text()').extract()
        # print(name_list)
        url_list = response.selector.css('a.s-item__link::attr(href)').extract()
        # print(url_list)
        ua = UserAgent()
        header = {
                'User-Agnet':ua.random
        }

        for i in range(0,199):
            item = DatascienceItem()
            # print(i)
            item['name'] = name_list[i]
            # print(item['name'])
            # item['types'] = self.settings['TYPE']
            
            # print(item['price']) //*[@id="vi-VR-brumb-lnkLst"]/table/tbody/tr/td/ul/li[3]/a/span
            item['url'] = url_list[i]
            item['source'] = 'eBay'
            # print(item['url'])
            yield SplashRequest(url=item['url'],meta={'item':item},callback=self.parse_detail,args=splah_args,headers=header)

    def parse_detail(self,response):
        print('Executed!')
        item = response.meta['item']
        item['types'] = response.xpath('//*[@id="vi-VR-brumb-lnkLst"]/table/tbody/tr/td/ul/li[3]/a/span/text()').get()
        print(item['types'])
        price = response.xpath('//*[@id="convbidPrice"]/text()').get()
        print(price)
        if 'RMB' in price:
            if len(price) > 11:
                    price = re.findall(r'\d+\,?\d+',price)[0]
                    if ',' in price:
                        price = price.replace(',','')
                        price = int(price)
            else:
                price = re.findall(r'\d+',price)[0]
                if ',' in price:
                    price = price.replace(',','')
                price = int(price)
        elif '元' in price:
            if len(price) > 8:
                    price = re.findall(r'\d+\,?\d+',price)[0]
                    if ',' in price:
                        price = price.replace(',','')
                        price = int(price)
            else:
                price = re.findall(r'\d+',price)[0]
                if ',' in price:
                    price = price.replace(',','')
                price = int(price)
        item['price'] = price
        # item['price'] = response.xpath('//span[@class="convbinPrice"]/text()').extract()//*[@id="viTabs_0_is"]/div/table[2] //*[@id="viTabs_0_is"]/div/table[2]/tbody/tr[1]/td[1]
        item['salers'] = response.xpath('//span[@class="mbg-nw"]/text()').extract()[0]
        # //*[@id="viTabs_0_is"] //*[@id="viTabs_0_is"]/div //*[@id="viTabs_0_is"]/div //*[@id="viTabs_0_is"]/div/table
        description_list = response.xpath('//*[@id="viTabs_0_is"]/div/table/tbody/tr/td//text()').extract()
        # print(description_list)
        item['description'] = ''
        for description in description_list:
            description = description.replace('\n','')
            description = description.replace('\t','')
            item['description'] = item['description']+ description
        print(item['description'])
        item['sales'] = ''
        salesInfo = response.xpath('//*[@id="why2buy"]/div//text()').get()
        print(salesInfo)
        if salesInfo is None:
            item['sales'] = -1
        else:
            for Info in salesInfo:
                # print(Info)
                if 'sold' in Info:
                    try:
                        sales = re.findall(r'\d+',Info)[0]
                        # print(sales)
                        item['sales'] = int(sales)
                        print(int(sales))
                        break
                    except Exception as e:
                        print(e)
                else:
                    item['sales'] = -1
        yield item
        # print(item)
            
        
        

