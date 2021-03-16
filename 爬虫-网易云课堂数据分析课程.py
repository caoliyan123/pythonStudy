#coding:utf-8

import requests
import json
import re,os

lesson_re=re.compile('"id":(\d+)',re.S|re.I)
lesson_url='https://ke.study.163.com/course/detail/100075459'
html=requests.get(lesson_url).text
less_id=lesson_re.findall(html)
for id in less_id:

    url='https://ke.study.163.com/course/video.json'
    params={
        'lessonId': id,
        'r': '1614907554570'
    }
    headers={
        'cookie': '_ntes_nnid=30845a8dd378dbcd37a70fd19d07cbbd,1610089449371; UM_distinctid=176e0cf4afc15f-031662222b1225-c791039-100200-176e0cf4afd47a; OUTFOX_SEARCH_USER_ID_NCOO=84543307.09987459; EDUWEBDEVICE=2f388dcd855d43a2be447f5998ce89b0; __utmz=129633230.1611044340.1.1.utmcsr=live.study.163.com|utmccn=(referral)|utmcmd=referral|utmcct=/; EDU-YKT-MODULE_GLOBAL_PRIVACY_DIALOG=true; P_INFO=15553116753|1611044365|1|study|00&99|shd&1611018876&yanxuan#shd&370100#10#0#0|&0|null|15553116753; xuetangvendor=iPhone; keoutvendor=; ke_inLoc=; hb_MA-BFF5-63705950A31C_source=study.163.com; ke_Pdt=ydkWeb; visitorUserId=visitora4954c205af844af8d05fd7fa203e64f; NTES_STUDY_YUNXIN_ACCID=s-1433894591; NTES_STUDY_YUNXIN_TOKEN=1b1a61e07e33b2639ce5913ca4213fdc; STUDY_NOT_SHOW_PROMOTION_DIALOG=true; sideBarPost=1247; NTESSTUDYSI=ca9aa8e9f3b744478838703ea2d8ba39; utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9saXZlLnN0dWR5LjE2My5jb20v; STUDY_INFO="yd.c4cb545e542b4e40b@163.com|8|1433894591|1614907184711"; STUDY_SESS="U0Mq3MQa/yAYZVgfO2oVyiN5r1TTVU8SM5/w7GJIf9PxkRVG8F1CQOBFXHRrOb2XHdEUClw+LjYFdW2Q1ESuNgqnHhWLHYmMrPlsQtpEcZG/QK4lkp3oOVKFAQRfe4wgIwM3TvIX5VqbTSWYpaYYiyr3qHVAchG+fOiIXxNG1fYLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="ow0L2SsbK9ykUacL1njX8VNQhWbDHurrOaquqUsxRwUtWoLs5kwglUuBjnlgiBNPZ3Hh/JWyTTiddmTQ7Y9BPfiZtr5HkBFfT6MGW1Dkb2tw6omQQfkGMzZaIXMtPPnVDeJdaGh/VzS84btmnWiTMtRb50qTg6oG9dcpGOO+gWKMcy+4vpwzcJ9+2BzcEQu4EiHkke8Ohp14KsIl3MaKPlyp6+IPziAIW3py1yG5f1/ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; DICT_SESS=v2|yi57zjWNQVYfnLgLnLTLROY64TuOLkY0TunH6uRLTz0lW0MpFOfYf06FRHz5O4eyROG64U5h4JL0Of6LQBRMYl0UW0fJyPLT4R; DICT_LOGIN=1||1614907184769; NETEASE_WDA_UID=1433894591#|#1585552573713; __utma=129633230.1928301253.1611044340.1614843183.1614907187.18; __utmc=129633230; __utmb=129633230.6.8.1614907361514; CNZZDATA1253417976=230845453-1611042202-https%253A%252F%252Fstudy.163.com%252F%7C1614904160; Hm_lvt_e46790f6d676f71878ebef1153dda3e2=1612490499,1614754217,1614843198,1614907370; Hm_lpvt_e46790f6d676f71878ebef1153dda3e2=1614907370; mp_MA-BFF5-63705950A31C_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fke.study.163.com%2Fcourse%2Fdetail%2F100075459%22%2C%22updatedTime%22%3A%201614907393202%2C%22sessionStartTime%22%3A%201614907370244%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%207%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%22beb6f363-55d4-4a36-bc54-77fc62886515%22%2C%22persistedTime%22%3A%201614907370240%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%2271f4d97d16585d67e09334c08daf465301f5671a%22%2C%22time%22%3A%201614907393203%7D%2C%22sessionUuid%22%3A%20%220688aa39-828b-4af6-a421-e0f5c0956044%22%7D',
        'origin': 'https://live.study.163.com',
        'referer': 'https://live.study.163.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    html=requests.get(url,params=params,headers=headers).text
    if html.find('"code":404')!=1:
        html_dic=json.loads(html)['result']
        lesson_title=html_dic['lessonTitle']
        video_url=html_dic['videoUrl']
        print('正在下载：',lesson_title)
        if not os.path.exists('E:\\学习\\video'):
            os.mkdir('E:\\学习\\video')
        with open('E:\\学习\\video\\{}.mp4'.format(lesson_title),'wb') as f:
            f.write(requests.get(video_url).content)

