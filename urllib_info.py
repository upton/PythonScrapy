#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib2 import Request, urlopen, URLError, HTTPError  
  
old_url = 'http://www.baidu.com'  
req = Request(old_url)  

try:
    response = urlopen(req)    
    print 'Info():'
    print response.info() 
except HTTPError, e:
    print e.code
except URLError, e:
    print e.reason
else:
    print 'fine'
 
