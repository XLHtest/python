#！/use/bin/python3
import urllib.request
import urllib.parse
import json

# ip= input("请ip：")
ip = "110.188.248.88"
html = "https://api.map.baidu.com/highacciploc/v1?qcip=220.181.38.113&ak=QCIr4l4KI3O8NjqmIHborXnm0XyZt0Dt&extensions=1&coord=bd09ll"
response = urllib.request.urlopen(html)
html = response.read().decode("utf-8")
target = json.loads(html)
print(target)