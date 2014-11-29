#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib

old_url = 'http://www.baidu.com'  
req = urllib2.Request(old_url)  

try:
    response = urllib2.urlopen(req)    
    print 'Info():'
    print response.info() 
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print 'fine'
 
my_url = 'http://url.cn/DZulrB'  
response = urllib2.urlopen(my_url, timeout=3)  
redirected = response.geturl() == my_url
print response.read()  
print redirected  


cookie = cookielib.CookieJar()  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  
response = opener.open('http://www.baidu.com')  
for item in cookie:  
    print '%s=%s' % (item.name, item.value)


# request = urllib2.Request('url', data={'key':'123'})  
# request.get_method = lambda: 'PUT'  # or 'DELETE'  
# response = urllib2.urlopen(request)  

postdata = urllib.urlencode({  
    'username':'汪小光',
    'password':'why888',
    'continueURI':'http://www.verycd.com/',
    'fk':'',
    'login_submit':'登录'  
})

headers = {  
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    'Referer':'http://www.cnbeta.com/articles'  
}

req = urllib2.Request(
    url='http://secure.verycd.com/signin',
    data=postdata,
    headers=headers
)  
result = urllib2.urlopen(req)  
print result.read()
print result.getcode()
