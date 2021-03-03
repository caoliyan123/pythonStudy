#coding:utf-8

import requests
import os,re,json

# re_hash=re.compile('"hash":"(.*?)"',re.S|re.I)
# url=''
hash_url='https://searchrecommend.kugou.com/get/complex'
params={
    'callback': 'jQuery1124011578388853206789_1614761739771',
    'word': '周杰伦',
    '_': '1614761739773'
}
hash_html=requests.get(hash_url, params=params).text
start=hash_html.find('{"data"')
end=hash_html.find('"info":""}')+len('"info":""}')
result=json.loads(hash_html[start:end])['data']['song']
for lis in result:
    song_name=lis['songname']
    songer_name=lis['singername']
    hash=lis['hash']

    url='https://wwwapi.kugou.com/yy/index.php'
    params={
        'r': 'play/getdata',
        'callback': 'jQuery19104341443083221761_1614761024893',
        'hash': str(hash),
        'dfid': '0PVFDZ3qVwt23cY1C93BuBR1',
        'mid': 'c16afe0890ad8c2a00901214f815242a',
        'platid': '4',
        'album_id': '966846',
        '_': '1614761024895'
    }
    html=requests.get(url,params=params).text
    print(json.loads(html))


    # s_start=html.find('{"status"')
    # s_end=html.find('}}')+len('}}')-1
    # s_result=json.loads(html[start:end])['data']
    # print(s_result)
