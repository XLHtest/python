#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import urllib2
import re


def getxiaoshuo():
    html = urllib2.urlopen('http://www.quanshu.net/book/9/9055/').read()
    html = html.decode('gb2312').encode('utf-8')
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    reg = re.compile(reg)
    xs = re.findall(reg, html)
    return xs


def getnr(url):
    html = urllib2.urlopen('http://www.quanshu.net/book/9/9055/' + url).read()
    html = html.decode('gbk').encode('utf-8')
    reg = r'<div class="mainContenr"   id="content"><script type="text/javascript">style5\(\);</script>(.*?)<script type="text/javascript">'.decode('gbk').encode('utf-8')
    reg = re.compile(reg)
    nr = re.findall(reg, html)
    return nr[0].replace('&nbsp;', ' ').replace('<br /><br />', '\n')


if __name__ == '__main__':
    xslist = getxiaoshuo()
    for i in xslist:
        # print i[0]
        text = getnr(i[0])
        print('正在爬取：' + i[1])
        fn = open('1.txt', 'a+')
        fn.write(i[1] + '\n' + getnr(i[0]) + '\n')
        # print text
        # break
    print('小说爬行完成')
