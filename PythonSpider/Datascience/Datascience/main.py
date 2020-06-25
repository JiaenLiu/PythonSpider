from scrapy import cmdline
import GetIPAddress_Version2
from GetIPAddress_Version2 import GetIpThread
if __name__ == '__main__':
    # 这里填写无忧代理IP提供的API订单号（请到用户中心获取）
    order = "ef614ed49a51483d859fa80a0d0a08e8"
    # 获取IP的API接口
    apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=" + order
    # 要抓取的目标网站地址
    targetUrl = "http://pv.sohu.com/cityjson?ie=utf-8"
    # 获取IP时间间隔，建议为5秒
    fetchSecond = 5
    # 开始自动获取IP
    GetIpThread(apiUrl,fetchSecond).start()
    cmdline.execute('scrapy crawl Taobao'.split())
    
    