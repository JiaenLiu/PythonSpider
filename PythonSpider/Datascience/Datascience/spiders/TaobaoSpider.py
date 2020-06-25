#TaobaoSpider.py
# import requests_html
from urllib import parse
# from lxml import etree
import json
import time
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

class TaobaoSpider(scrapy.Spider):
    name = 'Taobao'
    allowed_domains = [
        'taobao.com',
        's.taobao.com',
        'tmall.com'
    ]

    base_url = 'https://s.taobao.com/search?q=%s&sort=sale-desc&s=%s'

    def start_requests(self):
        cookie1 = {'UM_distinctid': '1720bca5544332-0cd2cfadbd793f-d373666-144000-1720bca5545728', ' enc': 'jib3kmOY9a2FmhKC9XOmvOE3KhsHLKapY5VJVk6gZ7a4pdP1dT9eAl8sCofUzgsBWxdUFSQ7GZTNPtiw7vu%2Fxg%3D%3D', ' _fbp': 'fb.1.1590743287656.21116350', ' hng': 'CN%7Czh-CN%7CCNY%7C156', ' thw': 'cn', ' _uab_collina': '159235982430406268484295', ' t': '8d1c8eea4b497af13dd510ad8e0d4349', ' cna': 'UE3aFtB3ewICAXWyAKJ4C5QN', ' sgcookie': 'EbjupdeEuxI47XBiRdtcv', ' uc3': 'vt3=F8dBxGGVrSxzNNIOtpw%3D&lg2=UtASsssmOIJ0bQ%3D%3D&nk2=F6k3HSxu%2FKdVgbpSveOkWJYUCPk%3D&id2=UUBfQgCha4B6WA%3D%3D', ' lgc': 't_1503220599924_0966', ' uc4': 'nk4=0%40FbMocxnJc8ITUsbZOz6T0v4sr3tBiPh7bYZ8ZR6jVw%3D%3D&id4=0%40U2LNbWjUVpw12yAN6EP5BDvvBywo', ' tracknick': 't_1503220599924_0966', ' _cc_': 'V32FPkk%2Fhw%3D%3D', ' tfstk': 'cOwGBN6hN5lsqdh3NOM_mIj7ZWfRZjCZ5-yULR9weHQrIj2Fihdea1tOxVUgHI1..', ' mt': 'ci=91_1', ' cookie2': '17cf4a978b672711776465cc39fd0937', ' _tb_token_': '76e1e3eee80d8', ' v': '0', ' alitrackid': 'www.taobao.com', ' lastalitrackid': 'www.taobao.com', ' _m_h5_tk': 'e20a6042b45c563f03e1c6a133c69752_1592708310251', ' _m_h5_tk_enc': '61ab9e244965e0046c0d967468fcc6b0', ' x5sec': '7b227365617263686170703b32223a226430646437316131313233613632623836623330316139623036386166623137434b376d7576634645497971684f32682b2b377176414561444449344e7a41774d7a4d324d4459374d773d3d227d', ' uc1': 'cookie14=UoTV7gbqm%2Fn0Xg%3D%3D', ' JSESSIONID': 'EB2A3043E2A4F540EA1DAC01705B910E', ' l': 'eBPo2UwmQldQqbzBBOfZnurza77OSIRxjuPzaNbMiOCPOu5p5mHhWZxUUEY9C3GNhs_6R3lil4laBeYBqIv4n5U62j-la_kmn', ' isg': 'BPb2HDbStK8EtUAextJN9XSDRyz4FzpR-mFLXGDf4ll0o5Y9yKeKYVxRu3fPODJp'}
        # ua = UserAgent()
        key_words = self.settings['KEY_WORDS'] # '电脑'
        key_words = parse.quote(key_words,' ').replace(' ','+')
        page_num = self.settings['PAGE_NUM']
        one_page_count = self.settings['ONE_PAGE_COUNT']
        for i in range(0,page_num):
            # header = {
            #     "User-Agent":ua.random
            # }
            url = self.base_url % (key_words,i*one_page_count)
            yield scrapy.Request(url,callback=self.parse)
    

    def parse(self, response):
        p = 'g_page_config = ({.*?});'
        g_page_config = response.selector.re(p)[0]
        g_page_config = json.loads(g_page_config)
        # ua = UserAgent()
        
        auctions = g_page_config['mods']['itemlist']['data']['auctions']
        for auction in auctions:
            # ua = UserAgent()
            '''header = {
                "User-Agent":ua.random,
                'authority': 's.taobao.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'zh-HK,zh;q=0.9,en-HK;q=0.8,en;q=0.7,zh-TW;q=0.6,en-US;q=0.5,zh-CN;q=0.4',
                'cookie': 'UM_distinctid=1720bca5544332-0cd2cfadbd793f-d373666-144000-1720bca5545728; enc=jib3kmOY9a2FmhKC9XOmvOE3KhsHLKapY5VJVk6gZ7a4pdP1dT9eAl8sCofUzgsBWxdUFSQ7GZTNPtiw7vu%2Fxg%3D%3D; _fbp=fb.1.1590743287656.21116350; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; cna=UE3aFtB3ewICAXWyAKJ4C5QN; sgcookie=Esu5XFgQPmMTEd1uuAa98; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&id2=UUBfQgCha4B6WA%3D%3D&nk2=F6k3HSxu%2FKdVgbpSveOkWJYUCPk%3D&vt3=F8dBxGDXKYO97m%2B8IwY%3D; lgc=t_1503220599924_0966; uc4=id4=0%40U2LNbWjUVpw12yAN6EP5AOC%2FCrLt&nk4=0%40FbMocxnJc8ITUsbZOz6T0v4sr3tBiPh7bYJG0iQxPQ%3D%3D; tracknick=t_1503220599924_0966; _cc_=UIHiLt3xSw%3D%3D; mt=ci=-1_1; tfstk=cLIlB7Z05a85UMLc5ut5K83gHaZOZGayNMSV0gNQpTfwsHSVip3q7zM8nQClv21..; miid=542627401040427552; _uab_collina=159235982430406268484295; cookie2=145822996ecccdf31aafcb5fd92046eb; t=7f259ea1df9a544530ff27f25b5ae90f; _tb_token_=feb58bb411831; v=0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _samesite_flag_=true; _m_h5_tk=34cb25c1112f5b66539b29fd13c538ee_1592555808906; _m_h5_tk_enc=7c5ccca10a985e8108eab4bfe5bc27a1; uc1=cookie14=UoTV7gQbOk%2FZNg%3D%3D; JSESSIONID=7E2111F9A68B536302E5386BD811CDE5; l=eBPo2UwmQldQqeiEBOfZourza77TSIRxnuPzaNbMiOCP_-fpJhHOWZxdBeL9CnGNh6rBR3lil4lwBeYBqnY4n5U62j-la1kmn; isg=BLu7T5AAYS7NJV3NyzXY1hGsSp8lEM8Svx62L614mrrBDNvuNeIGY_1OIqRCHicK',
            }'''
            item = DatascienceItem()
            item['name'] = auction['raw_title']
            # description = Get_description('https:' + auction['detail_url'])
            item['types'] = self.settings['TYPE']
            item['price'] = int(float(auction['view_price']))
            if len(auction['view_sales']) > 7 :
                if '万+' in auction['view_sales']:
                    sales = re.findall(r'\d+',auction['view_sales'])
                    sales = int(sales[0])*10000
                elif '+' in auction['view_sales']:
                    sales = re.findall(r'\d+',auction['view_sales'])
                    sales = int(sales[0])
            elif len(auction['view_sales']) <= 7:
                sales = re.findall(r'\d+',auction['view_sales'])
                sales = int(sales[0])
            item['sales'] = sales
            item['url'] = 'https:'+auction['detail_url']
            item['salers'] = auction['nick']
            # item['loc'] = auction['item_loc']

            # 
            if "tmall" in item['url']:
                try:
                    # item['description'] = parse_TMall_description(item['url'])
                    # yield item
                    cookie2 = {'UM_distinctid': '1720bca5544332-0cd2cfadbd793f-d373666-144000-1720bca5545728', ' _fbp': 'fb.1.1590743287656.21116350', ' hng': 'CN%7Czh-CN%7CCNY%7C156', ' thw': 'cn', ' _uab_collina': '159235982430406268484295', ' t': '8d1c8eea4b497af13dd510ad8e0d4349', ' cna': 'UE3aFtB3ewICAXWyAKJ4C5QN', ' mt': 'ci=91_1', ' cookie2': '17cf4a978b672711776465cc39fd0937', ' _tb_token_': '76e1e3eee80d8', ' v': '0', ' alitrackid': 'www.taobao.com', ' lastalitrackid': 'www.taobao.com', ' _m_h5_tk': 'e20a6042b45c563f03e1c6a133c69752_1592708310251', ' _m_h5_tk_enc': '61ab9e244965e0046c0d967468fcc6b0', ' x5sec': '7b227365617263686170703b32223a226430646437316131313233613632623836623330316139623036386166623137434b376d7576634645497971684f32682b2b377176414561444449344e7a41774d7a4d324d4459374d773d3d227d', ' _samesite_flag_': 'true', ' sgcookie': 'Ejwf1rGs79AjdCCrIBKPJ', ' unb': '1732072239', ' uc3': 'vt3=F8dBxGGVoWGTJJ4pR4k%3D&nk2=rpw2T3kdsl6NqyspWhk%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&id2=UoYdXzNbaaJOug%3D%3D', ' csg': '75695e10', ' lgc': '%5Cu5F80%5Cu4E8B%5Cu968F%5Cu98CE741229', ' cookie17': 'UoYdXzNbaaJOug%3D%3D', ' dnk': '%5Cu5F80%5Cu4E8B%5Cu968F%5Cu98CE741229', ' skt': '4bccba6f46940c80', ' existShop': 'MTU5MjcwMzM0Mg%3D%3D', ' uc4': 'nk4=0%40rMYjj0o7sVO6CE0AZjBgY56tgHbOiYtbdw%3D%3D&id4=0%40UO6U%2BcKIhhPIJ42J8cyr0qqPp%2FtX', ' tracknick': '%5Cu5F80%5Cu4E8B%5Cu968F%5Cu98CE741229', ' _cc_': 'VT5L2FSpdA%3D%3D', ' _l_g_': 'Ug%3D%3D', ' sg': '996', ' _nk_': '%5Cu5F80%5Cu4E8B%5Cu968F%5Cu98CE741229', ' cookie1': 'UNlhx%2FmXGtHmTIi2KSVsiHC3Yjxuiu0rpGvAOmp7VFs%3D', ' tfstk': 'cvT5B-OJs82SbJoUzQGVYOfhAW7FZ0Hfi06JNnjtvt4-YNO5iz4NCsPkx-4AXs1..', ' uc1': 'existShop=false&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&pas=0&cookie14=UoTV7gbqm%2FqhoA%3D%3D&cookie21=Vq8l%2BKCLjhS4UhJVbhgU', ' enc': 'SdXUE9%2B%2Fq7I%2FEMrLA0%2BUNxRJfLiuC81fLcuS3iWTfaMlupngpiWkII2zZ%2BKsEpIr5%2BYevVW4nGGjBp47xTVMCQ%3D%3D', ' JSESSIONID': 'D15180D2054C956A0A3FC8885F0574C1', ' l': 'eBPo2UwmQldQqqBkBOfwourza77tsIRjjuPzaNbMiOCPOQ5p5NxVWZxUEU89CnGNHspDR3lil4lwBfThpydq0-Y3L3k_J_Dr3dC..', ' isg': 'BGtrPyL4sVxQv-3dm4Vo5iE8-o9VgH8Cj65mX93oQqoBfIreZVF5UnPe0rQS79f6'}
                    item['source'] = 'Tmail'
                    yield scrapy.Request(url=item['url'],meta={'item':item},callback=self.parse_TMall_description)
                except Exception as ex:
                    print(ex)
            elif "taobao" in item['url']:
                try:
                    # item['description'] = parse_Taobao_description(item['url'])
                    # yield item
                    cookie1 = {'UM_distinctid': '1720bca5544332-0cd2cfadbd793f-d373666-144000-1720bca5545728', ' enc': 'jib3kmOY9a2FmhKC9XOmvOE3KhsHLKapY5VJVk6gZ7a4pdP1dT9eAl8sCofUzgsBWxdUFSQ7GZTNPtiw7vu%2Fxg%3D%3D', ' _fbp': 'fb.1.1590743287656.21116350', ' hng': 'CN%7Czh-CN%7CCNY%7C156', ' thw': 'cn', ' _uab_collina': '159235982430406268484295', ' t': '8d1c8eea4b497af13dd510ad8e0d4349', ' cna': 'UE3aFtB3ewICAXWyAKJ4C5QN', ' sgcookie': 'EbjupdeEuxI47XBiRdtcv', ' uc3': 'vt3=F8dBxGGVrSxzNNIOtpw%3D&lg2=UtASsssmOIJ0bQ%3D%3D&nk2=F6k3HSxu%2FKdVgbpSveOkWJYUCPk%3D&id2=UUBfQgCha4B6WA%3D%3D', ' lgc': 't_1503220599924_0966', ' uc4': 'nk4=0%40FbMocxnJc8ITUsbZOz6T0v4sr3tBiPh7bYZ8ZR6jVw%3D%3D&id4=0%40U2LNbWjUVpw12yAN6EP5BDvvBywo', ' tracknick': 't_1503220599924_0966', ' _cc_': 'V32FPkk%2Fhw%3D%3D', ' tfstk': 'cOwGBN6hN5lsqdh3NOM_mIj7ZWfRZjCZ5-yULR9weHQrIj2Fihdea1tOxVUgHI1..', ' mt': 'ci=91_1', ' cookie2': '17cf4a978b672711776465cc39fd0937', ' _tb_token_': '76e1e3eee80d8', ' v': '0', ' alitrackid': 'www.taobao.com', ' lastalitrackid': 'www.taobao.com', ' _m_h5_tk': 'e20a6042b45c563f03e1c6a133c69752_1592708310251', ' _m_h5_tk_enc': '61ab9e244965e0046c0d967468fcc6b0', ' x5sec': '7b227365617263686170703b32223a226430646437316131313233613632623836623330316139623036386166623137434b376d7576634645497971684f32682b2b377176414561444449344e7a41774d7a4d324d4459374d773d3d227d', ' uc1': 'cookie14=UoTV7gbqm%2Fn0Xg%3D%3D', ' JSESSIONID': 'EB2A3043E2A4F540EA1DAC01705B910E', ' l': 'eBPo2UwmQldQqbzBBOfZnurza77OSIRxjuPzaNbMiOCPOu5p5mHhWZxUUEY9C3GNhs_6R3lil4laBeYBqIv4n5U62j-la_kmn', ' isg': 'BPb2HDbStK8EtUAextJN9XSDRyz4FzpR-mFLXGDf4ll0o5Y9yKeKYVxRu3fPODJp'}
                    item['source'] = 'Taobao'
                    yield scrapy.Request(url=item['url'],meta={'item':item},callback=self.parse_Taobao_description)
                except Exception as ex:
                    print(ex)
            # yield item

    def parse_TMall_description(self,response):
        item = response.meta['item']
        item['description'] = ''
        description_data_sets = response.selector.xpath('//*[@id = "J_AttrUL"]/li/text()').get()
        for data in description_data_sets:
            item['description'] = item['description'] + data
        # print("Successful")
        yield item

    def parse_Taobao_description(self,response):
        item = response.meta['item']
        p = 'g_config.spuStandardInfo = ({.*?});'
        g_config = response.selector.xpath('//script[1]/text()').get()
        # print(g_config)
        g_config = re.findall(p,g_config)[0]
        # print(g_config)
        g_config = json.loads(g_config)
        # print(g_config)
        description_data_list = g_config['spuGroupInTab']
        # data_detail = g_config['g_config.spuStandardInfo']['spuGroupInTab']['spuStandardInfoUnits']
        # data_name = g_config['g_config.spuStandardInfo']['spuGroupInTab']['name']
        item['description'] = ''
        for data in description_data_list:
            if 'iconUrl' in data.keys():
                del data['iconUrl']   
            for i in data.values():
                if isinstance(i,str):
                    # print(i)
                    item['description'] = item['description'] + i
            else:
                for n in i:
                    for a in n.values():
                        item['description'] = item['description'] + a
        # print(item['description'])
            # return item['description']
        yield item
        


    # Test PIPELINES Spider
    # def start_requests(self):

    #     ua = UserAgent()
    #     key_words = self.settings['KEY_WORDS']
    #     key_words = parse.quote(key_words,' ').replace(' ','+')
    #     page_num = self.settings['PAGE_NUM']
    #     one_page_count = self.settings['ONE_PAGE_COUNT']
    #     for i in range(0,page_num):
    #         header = {
    #         "User-Agent": ua.random
    #         }
    #         url = self.base_url % (key_words,i*one_page_count)
    #         yield scrapy.Request(url,callback=self.parse,headers=header)
    #         # time.sleep(random.randint(10,15))
    #     #return super().start_requests()

    # def parse(self, response):
    #     p = 'g_page_config = ({.*?});'
    #     g_page_config = response.selector.re(p)[0]
    #     g_page_config = json.loads(g_page_config)
    #     auctions = g_page_config['mods']['itemlist']['data']['auctions']

    #     for auction in auctions:
    #         item = DatascienceItem()
    #         item['name'] = auction['raw_title']
    #         item['description'] = auction['raw_title']
    #         item['types'] = 'Phone'
    #         item['price'] = int(float(auction['view_price']))
    #         if len(auction['view_sales']) > 7 :
    #             if '万+' in auction['view_sales']:
    #                 sales = int(float(auction['view_sales'][0:3]))*10000
    #             elif '+' in auction['view_sales']:
    #                 sales = int(float(auction['view_sales'][0:4]))
    #         elif len(auction['view_price']) <= 7:
    #             sales = int(float(auction['view_sales'][0:4]))
    #         item['sales'] = sales
    #         item['source'] = 'Taobao'
    #         item['url'] = auction['detail_url']
    #         item['salers'] = auction['nick']
    #         item['loc'] = auction['item_loc']

    #         yield item
        # return super().parse(response)
    