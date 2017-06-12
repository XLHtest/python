#python3
from urllib import request
import os,re

url ="https://www.doutula.com/article/detail/"
def Download(dteail):
	html = request.urlopen(url+dteail).read().decode('utf-8')
	reg = r'<img src=\"(.*?)\" alt=\"(.*?)\" onerror=.*?>'
	reg =re.compile(reg)
	xs = re.findall(reg, html)
	for x in xs:
	    request.urlretrieve("https:"+x[0], x[1]+".jpg")
if __name__ == '__main__':
	dteail = input("请输入dteail：")
	Download(dteail)