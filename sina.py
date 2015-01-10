#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2


my_url = 'http://money.finance.sina.com.cn/q/view/newFLJK.php?param=industry'  
response = urllib2.urlopen(my_url)  
print response.read().decode('gb2312')  
