#coding=utf-8
#author:wangfeng
#
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

stockid = "sh6003318"
f = open('stock.txt','w')
#url = "http://hq.sinajs.cn/list=%s"%stockid
url1="http://hq.sinajs.cn/list=sh603318"
result =requests.get(url1)
f.write(result.text)
print result.text
f.close()


