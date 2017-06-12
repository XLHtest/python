#python3
from urllib import request
import re
import sys
import os
import threading
htmlurl ="http://www.zxcs8.com/map.html"

def GetMiddleStr(content, startStr, endStr):  # 取出中间文本
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
        endIndex = content.index(endStr)
    return content[startIndex:endIndex]
        
def GetTheDownloadDirectory(): #获取网站地图中的日期归档
    html=request.urlopen(htmlurl).read().decode('utf-8')
    reg = r'<li><a href="([a-zA-z]+://[^\s]*)">.*?</a></li>'
    reg = re.compile(reg)
    xs = re.findall(reg, html)
    # print(xs)
    return xs

def GetDirectory(url):#获取小说链接写到写到文本
    html = request.urlopen(url).read().decode('utf-8')
    if url != "http://www.zxcs8.com/record/201702":
        html = GetMiddleStr(html, '<div id="pagenavi"> <span>1</span>','</a></div>')
        reg = r"-?[1-9]\d*"
        reg = re.compile(reg)
        xs = re.findall(reg, html)
        html=xs[-1]
    else:
        html = "1";
    for x in range(int(html[-1])):
         links = GetLink(url+'/page/%s' %(x+1))
         for a in links:
            fn = open('小说网页目录.txt', 'a+')
            fn.write(a + '\n')

def GetLink(url): #获取日期归档中小说列表
    html = request.urlopen(url).read().decode('utf-8')
    reg = r'<dt><a href="([a-zA-z]+://[^\s]*)">.*?</a></dt>'
    reg = re.compile(reg)
    xs = re.findall(reg, html)
    return xs

def DownloadNovel():#下载小说
    links= GetTheDownloadDirectory()
    for x in links:
        GetDirectory(x) 
    with open("小说网页目录.txt",'rt') as f:
        for x in f:
            shuming,url = GetIinksAndTitles(x)
            request.urlretrieve(url, shuming+".rar", callbackfunc)

def GetIinksAndTitles(url):
    html = request.urlopen(url).read().decode('utf-8')
    Title = GetMiddleStr(html,"<h1>","</h1>")
    reg = r'<a title="TXT下载" href="(.*?)" target="_blank" rel="nofollow">'
    reg = re.compile(reg)
    xs = re.findall(reg, html)
    return Title,xs[0]

def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    global url
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    downsize=blocknum * blocksize
    if downsize >= totalsize:
        downsize=totalsize
    s ="%.2f%%"%(percent)+"====>"+"%.2f"%(downsize/1024/1024)+"M/"+"%.2f"%(totalsize/1024/1024)+"M \r"
    sys.stdout.write(s)
    sys.stdout.flush()
if __name__ == '__main__':
    threading.Thread(target=DownloadNovel,args=('')).start()