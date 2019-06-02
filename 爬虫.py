import requests  # 导入requests 模块
import requests_ftp  # 导入FTP request模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
import os  # 导入os模块
import re  # 正则表达式
import traceback

requests_ftp.monkeypatch_session()


class BeautifulPicture():

    def __init__(self):  # 类的初始化操作
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'https://www.xiaopian.com/html/gndy/dyzz/20181024/111902.html'  # 要访问的网页地址
        self.folder_path = 'C:\Elven_Code\BeautifulPicture'  # 设置图片要存放的文件目录

    def get_pic(self):
        print('开始网页get请求')
        r = self.request(self.web_url)

        print('开始获取所有a标签')
        all_a = BeautifulSoup(r.text, 'lxml').find_all('head')  # 获取网页中的class为cV68d的所有a标签

        print('开始创建文件夹')
        self.mkdir(self.folder_path)  # 创建文件夹

        print('开始切换文件夹')
        os.chdir(self.folder_path)  # 切换路径至上面创建的文件夹

        for a in all_a:  # 循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
            img_str = a['style']  # a标签中完整的style字符串
            print('a标签的style内容是：', img_str)
            first_pos = img_str.index('"') + 1
            second_pos = img_str.index('"', first_pos)
            img_url = img_str[first_pos: second_pos]  # 使用Python的切片功能截取双引号之间的内容
            # 获取高度和宽度的字符在字符串中的位置
            width_pos = img_url.index('&w=')
            height_pos = img_url.index('&q=')
            width_height_str = img_url[width_pos: height_pos]  # 使用切片功能截取高度和宽度参数，后面用来将该参数替换掉
            print('高度和宽度数据字符串是：', width_height_str)
            img_url_final = img_url.replace(width_height_str, '')  # 把高度和宽度的字符串替换成空字符
            print('截取后的图片的url是：', img_url_final)
            # 截取url中参数前面、网址后面的字符串为图片名
            name_start_pos = img_url.index('photo')
            name_end_pos = img_url.index('?')
            img_name = img_url[name_start_pos: name_end_pos]
            # self.save_img(img_url_final, img_name) #调用save_img方法来保存图片

    def save_img(self, url, name):  ##保存图片
        print('开始请求图片地址，过程会有点长...')
        img = self.request(url)
        file_name = name + '.jpg'
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '图片保存成功！')
        f.close()

    def request(self, url):  # 返回网页的response
        r = requests.get(url, headers=self.headers)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')


class elven_beautifulps():

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
        }  # 给请求指定一个请求头来模拟chrome浏览器
        #self.web_url = 'https://www.xiaopian.com/html/gndy/dyzz/20181024/111902.html'
        self.web_index = 'https://www.xiaopian.com/html/gndy/dyzz/index.html'
        self.web_prefix = 'https://www.xiaopian.com'

    def app_request(self,url_addr):
        req = requests.get(url_addr, self.headers)
        req.encoding = 'utf-8'
        return req

    def get_ps(self, url_addr):
        req1=self.app_request(url_addr)
        str_ps_all=BeautifulSoup(req1.text,'lxml')
        str_ps_url=str_ps_all.find_all(href=re.compile("http://www.win4000.com/mobile_detail_.*.html"),target="_blank")
        for i in str_ps_url:
            print(i["title"])
            print(i["href"])

    def get_moive_list(self):
        #页数定义
        page_num=1
        #获取请求
        req1= self.app_request(self.web_index)
        #解析请求，并爬取index里的每一条链接
        str_ind_all = BeautifulSoup(req1.text, 'lxml').find_all('option')

        #爬取每部电影的真实网页链接
        for i in str_ind_all:

            #只扫第一页首页
            if page_num>1:
                break

            #定义正则表达式
            str_ind1 = re.compile(r'/.*', re.S)
            #获取网址后面部分内容，并和网站名拼接为真实电影链接
            str_ind2 = str_ind1.findall(i['value'])
            if str_ind2:
                page_num = page_num + 1
                #print(self.web_prefix + '.'.join(str_ind2))
                new_url_addr = self.web_prefix + '.'.join(str_ind2)

                #请求电影列表页面链接
                req2 = self.app_request(new_url_addr)
                str_url_all = BeautifulSoup(req2.text, 'lxml').find_all('a',class_='ulink')

                #循环电影列表页面链接
                for i in str_url_all:
                    #print('  '+self.web_prefix+i['href'])
                    new_file_addr = self.web_prefix+i['href']

                    #请求电影页面链接
                    req3 = self.app_request(new_file_addr)
                    try:
                        #解析电影页面链接
                        str_soup=BeautifulSoup(req3.text, 'lxml')
                        #查找到img标签中的src属性的值，也就是图片的真实地址
                        str_ps = str_soup.find('img')['src']
                        #查找table标签中的内容
                        str_table = str_soup.find('table')
                        #获取table标签中子标签a的内容，也就是电影的ftp下载地址
                        str_source=str_table.a.contents
                        #获取下一个table标签中子标签a的内容，也就是电影的bt磁力链接
                        str_bt=str_table.find_next('table').a.contents
                        #获取电影标题名称
                        str_mv =str_soup.find('title')
                        #从下载地址中，截取文件名
                        file_name = re.split('/', '.'.join(str_source))[3]
                        #bt磁力链接转换成字符串
                        bt_src=''.join(str_bt)
                        #ftp下载链接转换成字符串
                        ftp_src = ''.join(str_source)
                        print('================'+''.join(str_mv)+'================')
                        print('    File Url   :' + new_file_addr)
                        print('    File Name  :' + file_name)
                        print('    FTP Source :' + ftp_src)
                        print('    BT Source  :' + bt_src)
                        print('    File Ps    :' + ''.join(str_ps))
                     #   print('    Moive Date :' + str_date)
                    except Exception as e:
                        print('  ----解析失败-----'+str(req1.status_code)+'--')
                        print(self.web_prefix + '.'.join(str_ind2))
                        print('  ' + self.web_prefix + i['href'])
                        traceback.print_exc()

ps = elven_beautifulps()
ps.get_ps('http://www.win4000.com/mobile_2344_0_0_1.html')
