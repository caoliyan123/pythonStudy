#coding:utf-8

import requests
import json

url='https://ke.study.youdao.com/course/live/lessons.json'
params={
    'courseId': '100075459',
    'r': '1614867020074'
}
html=requests.get(url,params=params).text
result=json.loads(html)['data']
print(result[0])
# title=result['title']
# download_url=result['downloadUrl']
# print(title,download_url)

