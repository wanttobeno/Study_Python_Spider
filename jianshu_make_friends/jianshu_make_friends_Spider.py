#-*- encoding:utf-8 -*-
import sys   #reload()之前必须要引入模块
reload(sys)
sys.setdefaultencoding('utf-8')

#===================================================================
import requests
from lxml import etree
import time
import os
import re
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

def get_url(url):
    res = requests.get(url,headers=headers)
    html = etree.HTML(res.text)
    infos = html.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        root = 'https://www.jianshu.com'
        #获取文章链接
        url_path = root + info.xpath('div/a/@href')[0]
        #print(url_path)
        get_img(url_path)
    time.sleep(3)

def get_img(url):
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    title = html.xpath('//div[@class="article"]/h1/text()')[0].strip('|').split('，')[0]
    # 去除非法符号
    title =validateTitle(title)
    name = html.xpath('//div[@class="author"]/div/span/a/text()')[0].strip('|')
    # 去除非法符号
    name = validateTitle(name)
    # 
    #print(title + ' ' + name)
    # 文章中的贴图
    infos = html.xpath('//div[@class = "image-package"]')
    i = 1
    for info in infos:
        path = 'row_img/' + title + '+' + name + '+' + str(i) + '.jpg'
        # 避免重复下载
        if os.path.exists(path) :
            continue
        #print(path)
        try:
            img_url = info.xpath('div[1]/div[2]/img/@data-original-src')[0]
            print(img_url)
            data = requests.get('http:' + img_url,headers=headers)
            try:
                fp = open(path,'wb')
                fp.write(data.content)
                fp.close()
            except OSError:
                fp = open('row_img/' + name + '+' + str(i) + '.jpg', 'wb')
                fp.write(data.content)
                fp.close()
        except IndexError:
            print('错误文件' + path)
            pass
        i = i + 1

if __name__ == '__main__':
    urls = ['https://www.jianshu.com/c/bd38bd199ec6?order_by=added_at&page={}'.format(str(i)) for i in range(1,201)]
    for url in urls:
        print(url)
        time.sleep(1)
        get_url(url)