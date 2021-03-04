#coding:utf-8

import requests
import json
import os,re

hash_re=re.compile('"Hash":"(.*?)"',re.S|re.I)
album_re=re.compile('"album_id":(\d+)',re.S|re.I)
hash_url='https://www.kugou.com/yy/rank/home/1-6666.html?from=homepage'
hash_html=requests.get(hash_url)
hashs=hash_re.findall(hash_html.text)
album_id=album_re.findall(hash_html.text)
print (hashs)
print(album_id)

for ha,id in zip(hashs,album_id):

    url='https://wwwapi.kugou.com/yy/index.php'
    params={
        'r': 'play/getdata',
        'callback': 'jQuery1910056522945376197065_1614846984264',
        'hash': str(ha),
        'dfid': '0PVFDZ3qVwt23cY1C93BuBR1',
        'mid': 'c16afe0890ad8c2a00901214f815242a',
        'platid': '4',
        'album_id': id,
        '_': '1614846984266'
    }
    html=requests.get(url,params=params).text
    #print(html)
    start=html.find('{"status"')
    end=html.find('}}')+len('}}')
    result=json.loads(html[start:end])['data']
    song_name=result['audio_name']
    song_url=result['play_url']
    print('正在下载',song_name)
    with open('E:\个人文件\音乐\{}.mp3'.format(song_name),'wb') as f:
        f.write(requests.get(song_url).content)