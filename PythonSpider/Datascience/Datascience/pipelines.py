# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to ADD your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymysql
from pymysql import cursors

class DatasciencePipeline(object):
    eBay_name = 'datascience'
    taobao_name = 'datascience'
    taobaoInsert = '''INSERT INTO datascience (name,description,types,price,sales,source,url,salers) 
                        VALUES ('{name}','{description}','{types}',{price},{sales},'{source}','{url}','{salers}')'''
    # print("CALLE DATASCIENCEPIPELINE")
    def __init__(self):
        # 这里的database，user，passwd需要改成自己设置。
        self.connect = pymysql.connect(
            host = 'localhost',
            port = 3306,
            database = 'scrapy',
            user = 'jiaenliu',
            passwd = '12345',
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item ,spider):
        sqltext = self.taobaoInsert.format(
            name = item['name'],
            description = item['description'],
            types = item['types'],
            price = item['price'],
            sales = item['sales'],
            source = item['source'],
            url = item['url'],
            salers = item['salers'],
            # loc = item['loc']
        )
        print(sqltext)
        try:
            # print(sqltext)
            self.cursor.execute(sqltext) 
            self.connect.commit()
            print('Successful')
        except Exception as ex:
            print(ex)
        # return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()