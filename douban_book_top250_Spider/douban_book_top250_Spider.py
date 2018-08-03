#-*- encoding:utf-8 -*-
import sys   #reload()之前必须要引入模块
reload(sys)
sys.setdefaultencoding('utf-8')

#===================================================================
from lxml import etree    #解析模块
import requests           #请求模块
import time
 
fp = open('douban_book_top250.txt','wb')
for a in range(10):
    url = 'https://book.douban.com/top250?start={}'.format(a*25)   #URL 遍历
    data = requests.get(url).text              #获得目标url 代码
 
    s=etree.HTML(data)     #解析下载的数据data
    #获取元素的Xpath信息  file=s.xpath('元素的xpath信息/text()')
    file=s.xpath('//*[@id="content"]/div/div[1]/div/table')   #shift+ctrl+c     右键 copy copyxpath
    #根据不同的需求 修改一下xpath 去掉数组[]  和  /tbody 标签
        
    #time.sleep(3)   #延迟  防止被检测

    for div in file:
        title = div.xpath("./tr/td[2]/div[1]/a/@title")[0]
        href = div.xpath("./tr/td[2]/div[1]/a/@href")[0]
        score=div.xpath("./tr/td[2]/div[2]/span[2]/text()")[0]
        num=div.xpath("./tr/td[2]/div[2]/span[3]/text()")[0].strip("(").strip().strip(")").strip()
        scrible=div.xpath("./tr/td[2]/p[2]/span/text()")
 
        if len(scrible) > 0:
            #print(u"书名：{}, 目标网址：{}, 评分：{}, 人数：{}, 评语：{}\n".format(title,href,score,num,scrible[0]))
            #data = '书名：' + title + '，目标网址' + href + '，评分：' + score + '，人数：' + num + '，评语：' + scrible[0] + '\n'	
            print('.'),
            data = '书名：%s 目标网址：%s 评分：%s 人数：%s 评语：%s\n' % (title, href, score,num,scrible[0])
            fp.write(data)
        else:
            # 没有评语的
            #print(u"{},{},{},{}\n".format(title,href,score,num))
            print('.'),
            data = '书名：%s 目标网址：%s 评分：%s 人数：%s\n' % (title, href, score,num)
            fp.write(data)
    print('OK !!!')
print('End !!!')
fp.close()