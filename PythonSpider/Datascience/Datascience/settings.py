# -*- coding: utf-8 -*-

# Scrapy settings for Datascience project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import datetime

BOT_NAME = 'Datascience'

SPIDER_MODULES = ['Datascience.spiders']
NEWSPIDER_MODULE = 'Datascience.spiders'

LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = 'log-NewEggspider.txt'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Datascience (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    # 'Datascience.middlewares.RandomUserAgentMiddlware': 543, 
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,  
    # 'Datascience.middlewares.DatascienceSpiderMiddleware':125,
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':2,
    # 'Datascience.uamid.Uamid':1,
    # 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None
}

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


UAPOOL= [
	"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0", 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36", 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
]

# MYSQL SETTINGS:

ITEM_PIPELINES = {
    'Datascience.pipelines.DatasciencePipeline':300,
}

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapy'
MYSQL_USER = 'jiaenliu'
MYSQL_PASSWD = '12345'
MYSQL_PORT = 3306

SPLASH_URL = 'http://localhost:8050'

KEY_WORDS = ['Laptop','Computer']

TYPE = "Phone"

PAGE_NUM = 10

ONE_PAGE_COUNT = 44

DOWNLOAD_DELAY = 10

API_ADDRESS = ''


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16




DEFAULT_REQUEST_HEADERS = {
    #Proxy-Authorization要填入由自己的账号密码生成base64加密字符串
    'Proxy-Authorization':'Basic MTIyNzIzNzQ4OUBxcS5jb206RkE3NTV1TlVYakZya2FK',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    # 我刚才找不到这个东西，按照我自己的思路改了一下
    #cookie要填入获得代理那个网页的cookie
    #'cookie':'advanced-frontend=xxxxxxxxxxxxxxxxx',
    'cookie': 'UM_distinctid=1720bca5544332-0cd2cfadbd793f-d373666-144000-1720bca5545728; _fbp=fb.1.1590743287656.21116350; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _uab_collina=159235982430406268484295; t=8d1c8eea4b497af13dd510ad8e0d4349; cna=UE3aFtB3ewICAXWyAKJ4C5QN; mt=ci=91_1; cookie2=17cf4a978b672711776465cc39fd0937; _tb_token_=76e1e3eee80d8; v=0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _m_h5_tk=e20a6042b45c563f03e1c6a133c69752_1592708310251; _m_h5_tk_enc=61ab9e244965e0046c0d967468fcc6b0; _samesite_flag_=true; sgcookie=Ejwf1rGs79AjdCCrIBKPJ; unb=1732072239; uc3=vt3=F8dBxGGVoWGTJJ4pR4k%3D&nk2=rpw2T3kdsl6NqyspWhk%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&id2=UoYdXzNbaaJOug%3D%3D; csg=75695e10; lgc=%5Cu5F80%5Cu4E8B%5Cu968F%5Cu98CE741229; cookie17=UoYdXzNbaaJOug%3D%3D; dnk=%5Cu5F80%5Cu4E8B%5Cu968F%5Cu98CE741229; skt=4bccba6f46940c80; existShop=MTU5MjcwMzM0Mg%3D%3D; uc4=nk4=0%40rMYjj0o7sVO6CE0AZjBgY56tgHbOiYtbdw%3D%3D&id4=0%40UO6U%2BcKIhhPIJ42J8cyr0qqPp%2FtX; tracknick=%5Cu5F80%5Cu4E8B%5Cu968F%5Cu98CE741229; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; sg=996; _nk_=%5Cu5F80%5Cu4E8B%5Cu968F%5Cu98CE741229; cookie1=UNlhx%2FmXGtHmTIi2KSVsiHC3Yjxuiu0rpGvAOmp7VFs%3D; tfstk=cvT5B-OJs82SbJoUzQGVYOfhAW7FZ0Hfi06JNnjtvt4-YNO5iz4NCsPkx-4AXs1..; enc=SdXUE9%2B%2Fq7I%2FEMrLA0%2BUNxRJfLiuC81fLcuS3iWTfaMlupngpiWkII2zZ%2BKsEpIr5%2BYevVW4nGGjBp47xTVMCQ%3D%3D; uc1=cookie14=UoTV7gbqm%2F096Q%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjhS4UhJVbhgU&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&pas=0; JSESSIONID=3CE88F18C01EE7AC78AE6106549D3BC5; isg=BP7-BL4TLEaQiHg2jurFDbwrTxRAP8K5IjlTdKgGQcF9S54lEMrmyd5qxx-HwLrR; l=eBPo2UwmQldQqUapBO5Clurza77TVIOb4cVzaNbMiInca6LF9n3buNQDxF4yWdtj_tCUTetrsqgr_dLHR3fRwxDDB3h2q_oIFxvO.',
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
}

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
'''DEFAULT_REQUEST_HEADERS = {
    'authority': 's.taobao.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.taobao.com/',
    'accept-language': 'zh-HK,zh;q=0.9,en-HK;q=0.8,en;q=0.7,zh-TW;q=0.6,en-US;q=0.5,zh-CN;q=0.4',
    'cookie': 'UM_distinctid=1720bca5544332-0cd2cfadbd793f-d373666-144000-1720bca5545728; enc=jib3kmOY9a2FmhKC9XOmvOE3KhsHLKapY5VJVk6gZ7a4pdP1dT9eAl8sCofUzgsBWxdUFSQ7GZTNPtiw7vu%2Fxg%3D%3D; _fbp=fb.1.1590743287656.21116350; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; cna=UE3aFtB3ewICAXWyAKJ4C5QN; sgcookie=Esu5XFgQPmMTEd1uuAa98; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&id2=UUBfQgCha4B6WA%3D%3D&nk2=F6k3HSxu%2FKdVgbpSveOkWJYUCPk%3D&vt3=F8dBxGDXKYO97m%2B8IwY%3D; lgc=t_1503220599924_0966; uc4=id4=0%40U2LNbWjUVpw12yAN6EP5AOC%2FCrLt&nk4=0%40FbMocxnJc8ITUsbZOz6T0v4sr3tBiPh7bYJG0iQxPQ%3D%3D; tracknick=t_1503220599924_0966; _cc_=UIHiLt3xSw%3D%3D; mt=ci=-1_1; tfstk=cLIlB7Z05a85UMLc5ut5K83gHaZOZGayNMSV0gNQpTfwsHSVip3q7zM8nQClv21..; miid=542627401040427552; _uab_collina=159235982430406268484295; _m_h5_tk=4901525a98740dbfcb9aacca003232fb_1592621298078; _m_h5_tk_enc=9791a8d4dac8c692b5b9a2da9b9afd4f; uc1=cookie14=UoTV7gdcNuAbcg%3D%3D; t=8d1c8eea4b497af13dd510ad8e0d4349; cookie2=13862f752aa981a3c048e04fbcd7f9fa; v=0; _tb_token_=53b77bbeb5553; JSESSIONID=66FC4E19261DD9F32373EC641D7AEA42; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; l=eBPo2UwmQldQqxCsBOfwnurza77tIIRxnuPzaNbMiOCP_W1p5K2GWZxCiMY9CnGNh6oDR3lil4lwBeYBqIv4n5U62j-lasHmn; isg=BKmphXRQ0zUZOO_X7dPK_O9SuFUDdp2ocVDk1UueIhDPEskkk8dYeA0A0L4kuDXg',
}'''

# RANDOM_UA_TYPE = 'random' # Random Chrome



# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    # 'Datascience.middlewares.DatascienceSpiderMiddleware': 543,
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Datascience.middlewares.DatascienceDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Datascience.pipelines.DatasciencePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
