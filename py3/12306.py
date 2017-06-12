from urllib import request
import ssl
from cs import *
import json

city = {}

for i in city_name.split('@'):
    if i:
        city[i.split('|')[1]] = i.split('|')[2]

ssl._create_default_https_context = ssl._create_unverified_context


train_date = '2017-05-30'
from_city = '南昌'
to_city = '深圳'
from_station = city[from_city]
to_station = city[to_city]

hs = {
    'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
}


def getlist():
    url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT" % (
        train_date, from_station, to_station)
    req = request.Request(url, headers=hs)
    html = request.urlopen(req).read()
    html = html.decode('utf-8')
    dict = json.loads(html)
    return dict
for i in getlist()['data']['result']:
    n = i.split('|')[28]
    if n == '*' or n == '--':
        continue
    if n == u'有' or int(n) > 0:
        print('有余票可以下单')
