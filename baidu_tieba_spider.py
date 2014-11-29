#!/usr/bin/env python
# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：百度贴吧爬虫
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。
#   功能：下载对应页码内的所有页面并存储为html文件。
#---------------------------------------

import urllib2, string, os

def tieba(url, start, end):
    for i in range(start, end + 1):
        fileName = os.path.join('tmp', string.zfill(i, 5) + '.html')
        print '正在保存文件%s' % fileName
        
        content = urllib2.urlopen(url + str(i)).read()
        
        with open(fileName, 'wb') as f:
            f.write(content)

url = 'http://tieba.baidu.com/p/1946603449?pn='
tieba(url, 2, 6)
