#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, time
import urllib2    
  
url = 'http://xueqiu.com/stock/quote.json?code=SZ300191&_=%s' % (int(time.time() * 1000))
   
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'    
   
headers = {'User-Agent' : user_agent,
#            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#            'Accept-Encoding':'gzip, deflate, sdch',
#            'Accept-Language':'zh-CN,zh;q=0.8',
           'Cookie':'xq_a_token=JxDkzB0RJmf8aSDaHul92x; xq_r_token=69oXi8d7F1GWLWqFPFyBKP; Hm_lvt_1db88642e346389874251b5a1eded6e3=1421851084; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1421909510; __utma=1.750920091.1421851084.1421905342.1421909445.3; __utmc=1; __utmz=1.1421851084.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
#            Host:xueqiu.com

           
           }    
req = urllib2.Request(url, None, headers)    
response = urllib2.urlopen(req)  
the_page = response.read() 
print response.getcode()
print the_page
