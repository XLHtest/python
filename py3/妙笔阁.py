#python3
from urllib import request
import re
import threading
# 0_1_0_0_0_1
# 0_ 0全部 1玄幻奇幻 2武侠仙侠 3都市青春 4历史军事 5科幻灵异 6游戏竞技 9女生言情
#0_1_0_11_0_1东方玄幻0_1_0_13_0_1史诗奇幻0_1_0_15_0_1历史神话0_1_0_17_0_1高武世界0_1_0_21_0_1古典仙侠0_1_0_23_0_1现代修真0_1_0_25_0_1传统武侠0_1_0_27_0_1国术武技0_1_0_29_0_1幻想修仙0_1_0_32_0_1官场沉浮0_1_0_34_0_1乡土小说0_1_0_36_0_1现实百态0_1_0_41_0_1架空历史0_1_0_43_0_1秦汉三国0_1_0_45_0_1五代十国0_1_0_47_0_1清史民国0_1_0_49_0_1历史传记0_1_0_411_0_1抗战烽火0_1_0_61_0_1虚拟网游0_1_0_63_0_1体育竞技0_1_0_65_0_1电子竞技0_1_0_51_0_1未来世界0_1_0_53_0_1宇宙练功0_1_0_55_0_1时空穿梭0_1_0_57_0_1末世危机0_1_0_59_0_1恐怖惊悚0_1_0_511_0_1寻墓探险0_1_0_91_0_1豪门总裁0_1_0_93_0_1青春校园0_1_0_95_0_1星际科幻0_1_0_97_0_1灵异推理0_1_0_99_0_1官场沉浮0_1_0_911_0_1穿越架空0_1_0_913_0_1玄幻仙侠0_1_0_915_0_1宫闱宅斗0_1_0_917_0_1豪门恩怨
# urls = "http://www.miaobige.com/shuku/0_1_0_0_0_1"
urls = "http://www.miaobige.com/shuku/5_1_0_0_0_1"
Pages = []
def GetMiddleStr(content, startStr, endStr):  # 取出中间文本
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex:endIndex]
def GetBooksLinks():
    html = request.urlopen(urls).read().decode('gbk')
    ys = GetMiddleStr(html,"</a> <a href=/shuku/",">尾页</a> </div>")
    ys = int(ys[-2]+ys[-1])
    BooksLinks(ys)
    
def BooksLinks(ye):
    global Pages
    for x in range(ye):
        urls ="http://www.miaobige.com/shuku/5_1_0_0_0_"+str(x+1)
        html = request.urlopen(urls).read().decode('gbk')        
        reg = r'<a href="/book/(.*?)/" target="_blank">(.*?)</a>'
        reg = re.compile(reg)
        xs = re.findall(reg, html)
        Pages += xs

def DownloadTheNovel(dz):
    AS = []
    ka = 'http://www.miaobige.com/read/'+dz[0]+'/'
    html = request.urlopen(ka).read().decode('gbk')
    reg = r'<a href="/read/(.*?)" target="_blank">(.*?)</a>'
    reg = re.compile(reg)
    xs = re.findall(reg, html)
    AS +=xs
    a = 0
    b = 1
    for x in AS: 
        a+=1  
        if a==9:
            html2 = request.urlopen('http://www.miaobige.com/read/'+x[0]).read().decode('gbk')
            reg2 = r'标记书签</a> <a href="(.*?)" title="(.*?)">下一章</a>'
            reg2 = re.compile(reg2)
            xs = re.findall(reg2, html2)
            ljdz = (dz[0] + '/' + xs[0][0]),xs[0][1]
            AS.insert(b,ljdz)
            a = -1 
        b+=1
    for s in AS:
        fn = open(dz[1]+'.txt', 'a+')
        fn.write(s[0] + '||' +s[1] + '\n')
if __name__ == '__main__':
    GetBooksLinks()
    for a in Pages:
        DownloadTheNovel(a)
        print("完成%s的链接爬取" %a[0])