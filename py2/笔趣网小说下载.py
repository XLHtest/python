#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import re
import sys
import os


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


def getlist(ID):  # 获取小说章节路径
    html = urllib.urlopen('http://m.qu.la/booklist/' + ID + '.html').read()
    html = html.decode('gbk').encode('utf-8')
    html = GetMiddleStr(html, '<script>shipei_1()</script>',
                        '<script>shipei_2()</script>')
    reg = r'<div class="bgg"><a href=\'(.*?)\'>(.*?)</a></div>'
    reg = re.compile(reg)
    xs = re.findall(reg, html)
    return xs


def getnr(url):  # 将小说内容去出
    html = urllib.urlopen('http://m.qu.la' + url).read()
    html = html.decode('gbk').encode('utf-8')
    html = GetMiddleStr(
        html, '<div id="nr1"><script>shipei_x()</script>', '<div class="nr_page">')
    return html.replace('&nbsp;', ' ').replace('<br /><br />', '\n').replace('</div>', '').replace('<script>dudu3();</script>', '').replace('<script>dudu2();</script>', '').replace('<script>dudu1();</script>', '')


def Download(ID, baocunshuming):  # 下载小说 定义小说名
    xslist = getlist(ID)
    for x in xslist[::-1]:
        print('正在爬取：'.decode('utf-8').encode('gbk') +
              x[1].decode('utf-8').encode('gbk'))
        fn = open(cur_file_dir() + '\\' + baocunshuming + '.txt', 'a+')
        fn.write(x[1] + '\n' + getnr(x[0]) + '\n')
if __name__ == '__main__':
    print u'小说保存路径： ' + cur_file_dir()
    print(u'小说识别代码就是例如：http://m.qu.la/booklist/3361.html中的3361')
    ID = str(raw_input('小说识别代码：'.decode('utf-8').encode('gbk')))
    baocunshuming = str(raw_input('保存书名：'.decode('utf-8').encode('gbk')))
    Download(ID, baocunshuming)