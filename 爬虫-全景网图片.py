#coding:utf-8

import requests
import json
import os
for i in range(1,2):
    url='https://quanjing.com/Handler/SearchUrl.ashx'
    params={
        't': '816',
        'callback': 'searchresult',
        'q': '春天',
        'stype': '1',
        'pagesize': '100',
        'pagenum': i,
        'imageType': '2',
        'fr': '1',
        'sortFlag': '1',
        '_': '1614755168058',
    }
    headers={
    'Cookie': 'BIGipServerPools_Web_ssl=1531750592.47873.0000; Hm_lvt_c01558ab05fd344e898880e9fc1b65c4=1614754262; Hm_lpvt_c01558ab05fd344e898880e9fc1b65c4=1614754272; qimo_seosource_578c8dc0-6fab-11e8-ab7a-fda8d0606763=%E7%BB%94%E6%AC%8F%E5%94%B4; qimo_seokeywords_578c8dc0-6fab-11e8-ab7a-fda8d0606763=; accessId=578c8dc0-6fab-11e8-ab7a-fda8d0606763; pageViewNum=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Referer': 'https://quanjing.com/search.aspx?q=%E6%98%A5%E5%A4%A9'
    }
    html=requests.get(url,params=params,headers=headers).text
    print (html)
    start=html.find('{"pageindex"')
    end=html.find('}]}')+len('}]}')
    result=json.loads(html[start:end])['imglist']
    # for n in result:
    #     print(n['pic_id'],n['imgurl'])
    #     if not os.path.exists('quanjing'):
    #         os.mkdir('quanjing')
    #     with open('quanjing/{}.jpg'.format(n['pic_id']),'wb') as f:
    #         f.write(requests.get(n['imgurl']).content)
