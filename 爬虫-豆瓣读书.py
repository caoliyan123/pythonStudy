#coding:utf-8

import requests
from bs4 import BeautifulSoup

for i in range(0,40,20):
    url='https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T'.format(i)
    headers={'Cookie': 'gadsTest=test; ll="118220"; bid=T8AZ6oYFJnk; __utma=30149280.1177391123.1612391368.1612391368.1614693284.2; __utmc=30149280; __utmz=30149280.1614693284.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ap_v=0,6.0; gr_user_id=cf9745f3-2560-4377-b29c-cf53a373b978; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=08d7a8b4-7499-425f-88e9-6c01161a5524; gr_cs1_08d7a8b4-7499-425f-88e9-6c01161a5524=user_id%3A0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1614693288%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.3ac3=*; __utmt_douban=1; __utma=81379588.2032780805.1614693288.1614693288.1614693288.1; __utmc=81379588; __utmz=81379588.1614693288.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_08d7a8b4-7499-425f-88e9-6c01161a5524=true; __yadk_uid=HumTWW4xj4BmXJJOvTzGQHuIwZbhs56k; _vwo_uuid_v2=DE51977D76CA66001CB770D5D69915861|32b30710004243a8470eb694d0efb2aa; __gads=ID=898d25e209de87ab-2253e9df34c6000d:T=1614693292:RT=1614693292:S=ALNI_MZ_hDHjtB5aNQwoqWhNp2DTEPBR_w; __utmb=30149280.5.10.1614693284; __utmb=81379588.4.10.1614693288; _pk_id.100001.3ac3=4be81b1abfd84e16.1614693288.1.1614693315.1614693288.',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
    html=requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    lis=soup.select('.subject-item')
    for n in lis:
        img=n.select('.pic a img')
        title=n.select('.info a')
        price=n.select('.info .pub')
        mark=n.select('.info p')
        print('图书标题：',title[0]['title'])
        print ('图片链接：',img[0]['src'])
        print ('图书作者、出版社、出版年份、价格：',price[0].text.strip().replace(' ','').replace('\n',''))
        print('图书简介：',mark[0].text.strip().replace(' ','').replace('\n',''))



