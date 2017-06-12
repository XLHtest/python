#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Tkinter import *
from ScrolledText import ScrolledText
import urllib
import requests
import re
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url_name = []  # url+名字
a = 1  # 定义
id = 1


def get():  # 写浏览器信息
    global a  # 定义全局
    hd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    url = 'http://www.budejie.com/' + str(a)
    html = requests.get(url, headers=hd).text  # 发送get请求
    url_content = re.compile(
        r'<div class="j-r-list-c">.*?</div>.*?</div>', re.S)
    url_contents = re.findall(url_content, html)
    a += 1
    # print url_contents
    for i in url_contents:
        url_reg = r'data-mp4="(.*?)">'  # 视频正则匹配
        url_items = re.findall(url_reg, i)
        # print url_items#视频链接
        if url_items:  # 判断地址的链接是否存在
            name_reg = re.compile(
                r'<a href="/detail-.{8}?.html">(.*?)</\w', re.S)
            name_items = re.findall(name_reg, i)
            # print name_items
            for i, k in zip(name_items, url_contents):
                url_name.append([i, k])
                # print i,k
    return url_name


def write():
    global id
    while id < 10:
        url_name = get()  # 调用地址+名字
        for i in url_name:
            urllib.urlretrieve(i[1], 'video\\$s.mp4' %
                               (i[0].decode('utf-8').encode('gbk')))  # 下载
            text.insert(END, str(id) + '.' + i[1] + '\n' + i[0] + '\n')
            url_name.pop(0)  # 删除已有的
            id += 1
        var1.set('爬取完成')


def start():
    th = threading.Thread(target=write)
    th.start()

# 创建窗口
root = Tk()  # 创建窗口

root.title('视频下载')  # 设置窗口名称
root.geometry('+300+100')  # 设置+坐标（位置），大小
text = ScrolledText(root, font=('微软雅黑', 10))  # 文本滚动条
text.grid()  # 布局方法
button = Button(root, text='开始爬取', font=('微软雅黑', 10), command=start)  # 按钮
button.grid()
var1 = StringVar()  # 定义一个变量
label = Label(root, font=('微软雅黑', 10), fg='red', textvariable=var1)
label.grid()
var1.set('准备就绪...')
root.mainloop()
