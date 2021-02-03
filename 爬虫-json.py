import json
import requests
from bs4 import BeautifulSoup

# url = 'https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=antip&srv_id=pc&offset=0&limit=20&strategy=1&ext={%22pool%22:[%22high%22,%22top%22],%22is_filter%22:10,%22check_type%22:true}'
# html = requests.get(url)
# for i in html.json():
#     print(i['cms_id'])

headers = {
'Cookie': 'PSTM=1583116647; BIDUPSID=FDBCED1967561446FEFE46083559F85F; BAIDUID=E2D7FD8EF652F7FBE20F4C4D83C7DB8F:SL=0:NR=10:FG=1; BD_UPN=12314753; sug=3; ORIGIN=0; bdime=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=GlIclhJbnZ0MS1vSmlBeXp6eHU4NERhZm5qdmdFcWd3RnJrRVlVM3JndFhmejlnRVFBQUFBJCQAAAAAAAAAAAEAAABO6QUb0-q8vtGpx6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFfyF2BX8hdga; BDUSS_BFESS=GlIclhJbnZ0MS1vSmlBeXp6eHU4NERhZm5qdmdFcWd3RnJrRVlVM3JndFhmejlnRVFBQUFBJCQAAAAAAAAAAAEAAABO6QUb0-q8vtGpx6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFfyF2BX8hdga; H_PS_PSSID=33425_33507_33403_33257_33272_31660_33584_26350_33544; delPer=0; BD_CK_SAM=1; PSINO=2; sugstore=1; COOKIE_SESSION=1526_0_4_1_45_4_0_1_2_3_0_0_7584088_0_0_0_1612391442_0_1612392965%7C9%230_1_1582873836%7C1; H_PS_645EC=a5f065Sww9naGZfmeQEgdqH6%2BDS7FgidY0IM1GzrtsrTmz2LyUe1Nc2c%2B00; BA_HECTOR=a1a0a1812k0ka0a58u1g1mag60q'
,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

html = requests.get('https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=python',headers=headers)
html.encoding=html.apparent_encoding
soup = BeautifulSoup(html.text,'lxml')
title = soup.select('div.result.c-container h3')
for i in title:
    print(i.text)
