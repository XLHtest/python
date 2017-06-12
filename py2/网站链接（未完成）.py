#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import request
import re
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
url_name = []  # url+名字
a = 1


def cur_file_dir():  # 获取脚本运行路径
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def GetMiddleStr(content, startStr, endStr):  # 取出中间文本
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex:endIndex]


def getlist(lx):
    global a
    # 创建浏览器信息
    hd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    # 定义要访问的网站
    url = 'https://www.susu83.com/htm/movielist' + \
        str(lx) + '/' + str(a) + '.htm'
    # 使用get方式访问网站
    html = requests.get(url, headers=hd).text
    # print html
    # yeshu =  GetMiddleStr(html,'</em>/','</strong>页</div>')
    # 创建正则表达式进行链接和名称的匹配
    url_content = re.compile(
        r'<li><a href="(.*?)" target="_blank"><h3>(.*?)</h3>', re.S)
    url_contents = re.findall(url_content, html)
    print url_contents
    a += 1
    # print yeshu
    for i in url_contents:
        getxiazai(2, i[1])


def getxiazai():
    hd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    url = 'https://www.pu860.com/htm/movie2/1621.htm'
    html = requests.get(url, headers=hd).text
    html1 = urllib.urlopen(url).read()
    print html
    print html1
    # dizi = GetMiddleStr(html,'<SCRIPT>var GvodUrls = codeUrl(movieurl_new_2+"','");</SCRIPT>')
    print dizi
getlist(2)
# getxiazai()
