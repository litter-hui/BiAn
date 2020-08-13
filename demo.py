#@Authar:Litter_hui
#@time:2020/8/13  20:50
#@name:PyCharm
#---------coding:utf-8--------

from bs4 import BeautifulSoup
import re
import urllib.request
import xlwt
import os
import shutil

def main():


    print("ok!!!")


#正则表达式标准
#findhref=re.compile(r'<a href=".*?"')
findhref=re.compile(r'/tupian/\d*.html')
findImg=re.compile(r'src="(/uploads/allimg/.*.jpg)"')
finfTitle=re.compile(r'title="(.*)"/>')
def getDate():

    print("data over")


def askURL(url):
    #模拟浏览器head
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/78.0.3904.108 Safari/537.36"}
    request=urllib.request.Request(url,headers=head)

    html=""
    try:
        response=urllib.request.urlopen(request)
        #html = response.read().decode("utf-8")
        html=response.read().decode("gbk")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html

if __name__ == '__main__':
    main()
    print("所长在等你")