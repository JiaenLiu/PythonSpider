# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import base64
from twisted.internet.defer import DeferredLock
import scrapy
import time
import json
import requests
import urllib.request
from scrapy.utils.project import get_project_settings
from Datascience.settings import UAPOOL,DEFAULT_REQUEST_HEADERS
from Datascience.try_to_getProxy import ProxyModel
# from fake_useragent import UserAgent
from scrapy import signals
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# import random

class RandomProxy(object):

    def __init__(self):
        self.current_proxy = None
        self.lock = DeferredLock()

    def process_request(self, request, spider):
        user_agent = random.choice(UAPOOL)
        request.headers['User-Agent'] = user_agent

        if 'proxy' not in request.meta or self.current_proxy.is_expiring:
            #请求代理
            self.update_proxy()
            request.meta['proxy'] = self.current_proxy.proxy

    def process_response(self, request, response, spider):
        # 如果对方重定向（302）去验证码的网页，换掉代理IP
        # 'captcha' in response.url 指的是有时候验证码的网页返回的状态码是200，所以用这个作为辨识的标志
        if response.status != 200 or 'captcha' in response.url:
            # 如果来到这里，说明这个请求已经被boss直聘识别为爬虫了
            # 所以这个请求就相当于什么都没有获取到
            # 所以要重新返回request，让这个请求重新加入到调度中
            # 下次再发送
            if not self.current_proxy.blacked:
                self.current_proxy.blacked = True
            self.update_proxy()
            print('%s代理失效' % self.current_proxy.proxy)
            request.meta['proxy'] = self.current_proxy.proxy
            return request

        # 如果是正常的话，记得最后要返回response
        # 如果不返回，这个response就不会被传到爬虫那里去
        # 也就得不到解析
        return response

    def update_proxy(self):
        #lock是属于多线程中的一个概念，因为这里scrapy是采用异步的，可以直接看成多线程
        #所以有可能出现这样的情况，爬虫在爬取一个网页的时候，忽然被对方封了，这时候就会来到这里
        #获取新的IP，但是同时会有多条线程来这里请求，那么就会出现浪费代理IP的请求，所以这这里加上了锁
        #锁的作用是在同一时间段，所有线程只能有一条线程可以访问锁内的代码，这个时候一条线程获得新的代理IP
        #而这个代理IP是可以用在所有线程的，这样子别的线程就可以继续运行了，减少了代理IP（钱）的浪费
        self.lock.acquire()
        # 判断换线程的条件
        # 1.目前没有使用代理IP
        # 2.到线程过期的时间了
        # 3.目前IP已经被对方封了
        # 满足以上其中一种情况就可以换代理IP了

        # Verify Function

        if not self.current_proxy or self.current_proxy.is_expiring or self.current_proxy.blacked:
            url = r'http://api.wandoudl.com/api/ip?app_key=c282518965f3b0ecc95c1044d1399210&pack=0&num=5&xy=1&type=2&lb=\r\n&mr=1&' # % random.randint(0, 10)
            response = requests.get(url=url, headers=DEFAULT_REQUEST_HEADERS)
            text = json.loads(response.text)
            print(text)
            data = text['data'][0]
            proxy_model = ProxyModel(data)
            print('重新获取了一个代理：%s' % proxy_model.proxy)
            self.current_proxy = proxy_model
            # return proxy_model
        self.lock.release()







# Get Random User-Agent
# class RandomUserAgentMiddlware(object):
#     def __init__(self,crawler):
#         super(RandomUserAgentMiddlware,self).__init__()
#         self.ua = UserAgent()
#         self.ua_type = crawler.settings.get('RANDOM_UA_TYPE','random')

#     @classmethod
#     def from_crawler(cls,crawler):
#         return cls(crawler)

#     def process_request(self,request,spider):
#         def get_ua():
#             return getattr(self.ua,self.ua_type)
#         request.headers.setdefault('User-Agent',get_ua)
#         pass

# Get Random Proxy
'''
class RandomProxy(object):
    def __init__(self, settings):
        self.PROXY_URL = settings.get('PROXY_URL')
        self.chosen_proxy = ''


        if self.PROXY_URL is None:
                raise KeyError('需要先设置获取代理ip接口的地址')
        #从地址获取一个ip
        self.chosen_proxy =self.getProxy()


    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def getProxy(self):
        log.msg('get proxy')
        proxy_addr=json.loads(requests.get(self.PROXY_URL).text)['ip']
        log.msg("[+]---get proxy ip is:" + proxy_addr)
        return proxy_addr

    def delip(self, proxy):
        log.msg("要删除的ip:" + proxy)
        sql = 'delete from ip where data =%s' % '\'' + proxy + '\''
        sta = cursor.execute(sql)
        log.msg(sql)
        log.msg(sta)
        if sta > 0:
            log.msg("del band ip from databases")
            db.connection.commit()
        else:
            log.msg('del ip faile')

    def process_request(self, request, spider):
        if 'proxy' in request.meta:
            if request.meta["exception"] is False:
                return
        request.meta["exception"] = False
        request.meta['proxy'] ="http://" + self.chosen_proxy

    def process_response(self, request, response, spider):

        if response.status in [403, 400,302] and 'proxy' in request.meta:
            log.msg('Response status: {0} using proxy {1} retrying request to {2}'.format(response.status, \
                                                                                          request.meta['proxy'],
                                                                                          request.url))
            proxy = request.meta['proxy']
            del request.meta['proxy']
            proxyip = proxy.split("//")[1]
            try:
                #删除数据库里的ip
                self.delip(proxyip)
                log.msg('deleted banned proxy , proxy %s' % proxyip)
            except KeyError:
                pass
            self.chosen_proxy = self.getProxy()#这个代理被403,302了 重新获取
            return request
        return response

    def process_exception(self, request, exception, spider):
        if 'proxy' not in request.meta:
            log.msg("没代理错了,需要检查")
            return
        else:
            log.msg("有代理也错了，把数据库的ip删掉")
            proxy = request.meta['proxy']
            proxyip = proxy.split("//")[1]
            try:
                # 删除数据库里的ip
                self.delip(proxyip)
            except KeyError:
                pass
            request.meta["exception"] = True
            log.msg("重新获取ip")
            self.chosen_proxy=self.getProxy()
            return  request

'''
# class IPPOOlS(HttpProxyMiddleware):
#     # Initialization
#     def __init__(self,ip=''):
#         self.ip = ip
    
#     def process_request(self,request,spider):
#         this_ip = random.choice(IPPOOL)
#         print("This ip is:" + this_ip)
#         request.meta["proxy"] = "http://" + this_ip



# class ProxyMiddleWare(object):
#     """docstring for ProxyMiddleWare"""  
#     def process_request(self,request, spider):  
#         '''对request对象加上proxy'''  
#         proxy = self.get_random_proxy()  
#         print("this is request ip:"+proxy)  
#         request.meta['proxy'] = proxy   

#     def process_response(self, request, response, spider):  
#         '''对返回的response处理'''  
#         # 如果返回的response状态不是200，重新生成当前request对象  
#         if response.status != 200:  
#             proxy = self.get_random_proxy()  
#             print("this is response ip:"+proxy)  
#             # 对当前reque加上代理  
#             request.meta['proxy'] = proxy   
#             return request  
#         return response  

#     def get_random_proxy(self):  
#         '''随机从文件中读取proxy'''  
#         while 1:  
#             with open('proxies.txt', 'r') as f:  
#                 proxies = f.readlines()  
#                 if proxies:  
#                     break  
#                 else:  
#                     time.sleep(1)  
#         proxy = random.choice(proxies).strip()
#         return proxy  

    # Version 1
    # def process_request(self,request,spider):
    #     '''Add proxy to request object'''
    #     proxy = self.get_random_proxy()
    #     print("This is request ip:"+proxy)
    #     request.meta['proxy'] = proxy

    # def process_response(self,request,response,spider):
    #     '''Process the request'''
    #     # if response's status is not 200, make request again
    #     if response.status != 200:
    #         proxy = self.get_random_proxy()
    #         print("This is request ip:"+proxy)
    #         # 对当前request加上代理
    #         request.meta['proxy'] = proxy
    #         return request
    #     return response

    



class DatascienceSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    def process_request(self, request, spider):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        # 指定谷歌浏览器路
        base_url_list = ['https://www.ebay.com/sch/i.html?_nkw=Phone&_sacat=0&_sop=10&_pgn=1&_ipg=200','https://www.ebay.com/sch/i.html?_nkw=Phone&_sacat=0&_sop=10&_pgn=2&_ipg=200','https://www.ebay.com/sch/i.html?_nkw=Phone&_sacat=0&_sop=10&_pgn=3&_ipg=200','https://www.ebay.com/sch/i.html?_nkw=Phone&_sacat=0&_sop=10&_pgn=4&_ipg=200','https://www.ebay.com/sch/i.html?_nkw=Phone&_sacat=0&_sop=10&_pgn=5&_ipg=200','https://www.ebay.com/sch/i.html?_nkw=Phone&_sacat=0&_sop=10&_pgn=6&_ipg=200'
        ,'https://www.ebay.com/sch/i.html?_nkw=Phone&_sacat=0&_sop=10&_pgn=7&_ipg=200','https://www.ebay.com/sch/i.html?_nkw=Phone&_sacat=0&_sop=10&_pgn=8&_ipg=200','https://www.ebay.com/sch/i.html?_nkw=Phone&_sacat=0&_sop=10&_pgn=9&_ipg=200','https://www.ebay.com/sch/i.html?_nkw=Phone&_sacat=0&_sop=10&_pgn=10&_ipg=200']
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='/mnt/c/DRIVERS/chromedriver.exe')
        # if request.url not in  base_url_list:
        self.driver.get(request.url)
        time.sleep(4)
        html = self.driver.page_source
        self.driver.quit()
        return scrapy.http.HtmlResponse(url=request.url, body=html.encode('utf-8'), encoding='utf-8',request=request)


    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DatascienceDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    # def __init__(self):
    #     settings = get_project_settings()
    #     ApiAddress = settings.get('API_ADDRESS')
    #     res = requests.get(ApiAddress)

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
