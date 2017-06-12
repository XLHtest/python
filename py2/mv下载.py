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


def getlist():
    url = 'http://www.68mtv.com/hot.html'
    html = urllib.urlopen(url).read()
    # print html
    reg = re.compile(
        r'<a target="_blank" title="(.*?)" href="/music/(.*?).html"><div class="image">'
    )
    nr = re.findall(reg, html)
    return nr


if __name__ == '__main__':
    dz = getlist()
    for x in dz:
        fn = open(cur_file_dir() + '\\' + 'mv下载链接.txt', 'a+')
        fn.write(x[0] + ':' + 'http://www.68mtv.com/index/down/id/' + x[1] + '\n')
