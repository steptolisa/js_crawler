#coding:utf-8
#python3.6

import requests



def download(url,pages):


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
    import pandas as pd
    path = r'D:\download_files'
    writer = pd.ExcelWriter(path + '/' + 'output_final.xlsx')
    for page in range(pages):
        page = page + 1
        paras = {
            'jsoncallback':'jQuery111203831878820422663_1535169834711',
            'lcnK':'f57f50a55dc99564468dba987810aaff',
            'brand':'TAN',
            'page':str(page),
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
        res_dict = json.loads(res_out0)

        print(res_dict)
        print(type(res_dict))



        df = pd.DataFrame(res_dict)
        print(df)



        df.to_excel(writer,str(page))
    writer.save()

pages = 614



url = 'http://k.tanjiaoyi.com:8080/KDataController/datumlist4Embed.do?'

download(url,pages)

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