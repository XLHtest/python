# !/usr/bin/python
# -*- coding: utf-8 -*-
from ftplib import FTP
import time
import tarfile
import sys,os
def cur_file_dir():#获取脚本运行路径
     path = sys.path[0]
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp

#从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

#从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == "__main__":
    ftp = ftpconnect("121.42.195.235", "xlh", "qq2402324010...")
    #downloadfile(ftp, "NetSyst96.dll", cur_file_dir()+"test.dll")
    uploadfile(ftp,"12.py",'\\'+"笔趣网小说下载 - 副本.py")
    ftp.quit()