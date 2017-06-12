#python3
#没有办法匹配出混淆协议
#失败的脚本
from urllib import request
import re

url="https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7"

html = request.urlopen(url).read().decode("utf-8")
reg = r'<p>服务器.*?：(.*?)</p>'
reg = re.compile(reg)
xs = re.findall(reg,html)
for x in xs:
	ls = re.split(r'([^\x00-\xff]+)',x.lstrip())
	a = ls[0]+ls[2]+ls[4]+ls[6]
	fn = open('ss.txt', 'a+')
	fn.write(a + '\n')