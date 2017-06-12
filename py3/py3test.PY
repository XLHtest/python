#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib import request
import re
import sys,os
import keyword
# reload(sys)
# sys.setdefaultencoding('utf-8')
# hd = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# url = 'https://www.susu83.com/htm/index.htm'
# html = requests.get(url,headers=hd).text
# url_content = re.compile(r'<li><a href="(.*?)" target="_blank"><h3>(.*?)</h3>',re.S)
# url_contents =re.findall(url_content,html)
# print url_contents
# str = 'Runoob'
# print (str)          # 输出字符串
# print (str[0:-1])    # 输出第一个个到倒数第二个的所有字符
# print (str[0])       # 输出字符串第一个字符
# print (str[2:5])     # 输出从第三个开始到第五个的字符
# print (str[2:])      # 输出从第三个开始的后的所有字符
# print (str * 2)      # 输出字符串两次
# print (str + "TEST") # 连接字符串
a = 0
b = 1
AS = ['1000','1','2','0','9','8','7','6','5','4','3','2','11','12','13','14','15','16','17','18','19']
for x in AS: 
    a+=1    
    if a==10:
        print(x)
        AS.insert(b,"dishiz")
        a = -1
        print(AS)
    b+=1
    