#coding:utf-8
#python3.6

import requests




url = 'http://k.tanjiaoyi.com:8080/KDataController/datumlist4Embed.do?'

headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'Hm_lvt_5b7b04c64b5e4f3443ad385ba0ee1d37=1535165401; JSESSIONID=KnkH4WVpYh9Xt4Z3tdQXe+u6.undefined; Hm_lpvt_5b7b04c64b5e4f3443ad385ba0ee1d37=1535169835',
    'Host':'k.tanjiaoyi.com:8080',
    'Referer':'http://k.tanjiaoyi.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

}

paras = {
    'jsoncallback':'jQuery111203831878820422663_1535169834711',
    'lcnK':'f57f50a55dc99564468dba987810aaff',
    'brand':'TAN',
    'page':'1',
    'rows':'20',
    '_':'1535169834713'

}



response = requests.get(url, params=paras, headers = headers,timeout = 60)
response.encoding = 'utf-8'
res = response.text

print(res)
# print(type(res))


import json
import re

#正则匹配所需数据
p1 = '(?<="rows":).+?(?=}, \'ALL\')'
pattern1 = re.compile(p1,re.S)

res_out = re.findall(pattern1,res)
# print(res_out)
print(len(res_out))

res_out0 = res_out[0]
print(res_out0)
# res_out0 = json.dumps(res_out0)
# res_out0 = json.loads(res_out0)
# print(res_out0)

# 用法推荐网址
# https://blog.csdn.net/mr_evanchen/article/details/77879967
# 字符串转字典
res_dict = json.loads(res_out0)

print(res_dict)
print(type(res_dict))

#导入pandas模块，pandas模块用处很大的，可以多查看官网 API  http://pandas.pydata.org/pandas-docs/stable/api.html
import pandas as pd

# 字典转dataframe
df = pd.DataFrame(res_dict)
print(df)

path = r'D:\download_files'
# 创建excel
writer = pd.ExcelWriter(path + '/'+'output1.xlsx')

# 写入到excel 的sheet里
df.to_excel(writer,'Sheet1')
# 保存
writer.save()



# res_out0 =res_out0.replace('[','')
# dict = json.dumps(res_out0)
#
# dict = json.loads(dict)
#
# print(dict)
# #
# print(type(dict))
#
# res_json = json.dumps(res)
# print(res_json)
# print(type(res_json))
#
# js_ = json.loads(res_json)
# print(js_)
#
# print(type(js_))