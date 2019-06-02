import requests  # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
import os  # 导入os模块
import re  # 正则表达式

class elven_beautifulps():

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
        }  # 给请求指定一个请求头来模拟chrome浏览器

    def app_request(self,url_addr):
        req = requests.get(url_addr, self.headers)
        req.encoding = 'utf-8'
        return req

    def get_bk(self,url_addr):
            self.url_prefix='https://www.webank.com'
            req_bk=self.app_request(url_addr)
            str_bk_all=BeautifulSoup(req_bk.text,'lxml')
            str_bk_url=str_bk_all.find_all(href=re.compile('/announcement/*'),text=re.compile(''))
            print(str_bk_all)
            for i in str_bk_url:
              print('https://www.webank.com/'+i['href'],i.string)
              str_bk_url1=self.url_prefix+i['href']
              #pass

ps = elven_beautifulps()
ps.get_bk('https://www.webank.com/announcement/#/1')