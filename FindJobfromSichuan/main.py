# encoding: utf-8
"""
@version: 1.0
@author: 
@file: main.py
@time: 2019/10/20 19:57
"""
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

#url_initial = 'http://202.61.89.231/news/morenews.aspx?nId=0&sId=&Id=62&page=1'#省属事业单位
#url_initial = 'http://202.61.89.231/news/morenews.aspx?nId=0&sId=&Id=63&page=1' #市州事业单位
url_initial = 'http://202.61.89.231/news/morenews.aspx?nId=0&sId=&Id=65&page=3' #其他事业单位

dic_excel = {}

def get_docx(url):
    response = requests.get(url)
    bsobj = BeautifulSoup(response.text,'lxml')
    a_tag_herf = bsobj.find('a',style = 'text-decoration: none')
    print(a_tag_herf)

    if a_tag_herf == None:
        return '无可下载文件...'
    else:
        file_name = a_tag_herf.text
        file_type = a_tag_herf['href'].split('.')[-1]
        file_name = file_name.lstrip()
        urlretrieve(a_tag_herf['href'], filename=file_name + '.' + file_type)
        return '文件保存成功...'

if __name__ == "__main__":
    url_eachpage = url_initial[:-1] + str(1)
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    response = requests.get(url_eachpage, headers = head)   #从链接中获取到回复信息
    #print(response.text)
    bsobj = BeautifulSoup(response.text, 'lxml')    #利用bs解析
    #print(bsobj)
    div_class_li = bsobj.find('div',class_ = 'listr')
    Link_href = []
    for li in div_class_li.ul:
        if li == '\n':
            continue
        else:
            link = li.a['href']
            link = 'http://202.61.89.231' + link
            Link_href.append(link)
            print(link)
            get_docx(link)
    print(dic_excel)


