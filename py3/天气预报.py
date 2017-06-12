#http://wthrcdn.etouch.cn/weather_mini?city=查询地址
#python3
from urllib import *
import json


content = input("请输入要查询的地点：")
url = "http://wthrcdn.etouch.cn/weather_mini?city="+content
html = urllib.urlopen(url)
print(html)
target = json.loads(html)
print(target)