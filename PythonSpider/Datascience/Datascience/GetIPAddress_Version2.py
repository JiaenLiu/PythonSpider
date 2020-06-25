# -*- coding: UTF-8 -*-

'''
Python 3.x
无忧代理IP Created on 2018年07月11日
描述：本段代码定时从无忧代理API接口获取代理IP，存入IP池中
@author: www.data5u.com
'''
import requests
import time
import threading
from data5u import IPPOOL
from requests.packages import urllib3

# ips = []

# 爬数据的线程类
'''class CrawlThread(threading.Thread):
    def __init__(self,proxyip):
        super(CrawlThread, self).__init__()
        self.proxyip=proxyip
    def run(self):
        # 开始计时
        start = time.time()
        #消除关闭证书验证的警告
        urllib3.disable_warnings()
        #使用代理IP请求网址，注意第三个参数verify=False意思是跳过SSL验证（可以防止报SSL错误）
        html=requests.get(url=targetUrl, proxies={"http" : 'http://' + self.proxyip, "https" : 'https://' + self.proxyip}, verify=False, timeout=15).content.decode()
        # 结束计时
        end = time.time()
        # 输出内容
        print(threading.current_thread().getName() +  "使用代理IP, 耗时 " + str(end - start) + "毫秒 " + self.proxyip + " 获取到如下HTML内容：\n" + html + "\n*************")
'''
# 获取代理IP的线程类
class GetIpThread(threading.Thread):
    def __init__(self,apiUrl,fetchSecond):
        super(GetIpThread, self).__init__()
        self.fetchSecond=fetchSecond
        self.apiUrl = apiUrl
    def run(self):
        # global ips
        while True:
            # 获取IP列表
            res = requests.get(self.apiUrl).content.decode()
            # 按照\n分割获取到的IP
            print(res.split('\n'))
            IPPOOL=(res.split('\n'))
            print(IPPOOL)
            # 休眠
            time.sleep(self.fetchSecond)

