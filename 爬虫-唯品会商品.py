#coding=utf-8
import requests
import json

for i in range(0,120,120):
    url='https://mapi.vip.com/vips-mobile/rest/shopping/pc/search/product/rank?callback=getMerchandiseIds&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=103107101&client=pc&mobile_platform=1&province_id=103107&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1613685844591_0610a409c5d025bd593cf23cf7df50aa&wap_consumer=a&standby_id=nature&keyword=%E6%8A%A4%E8%82%A4%E5%A5%97%E8%A3%85&lv3CatIds=&lv2CatIds=&lv1CatIds=&brandStoreSns=&props=&priceMin=&priceMax=&vipService=&sort=0&pageOffset={}&channelId=1&gPlatform=PC&batchSize=120&_=1613686543376'.format(i)
    headers={
        'cookie': 'cps=adp%3Ag1o71nr0%3A%3A%3A%3A; vip_first_visitor=1; vip_address=%257B%2522pid%2522%253A%2522103107%2522%252C%2522cid%2522%253A%2522103107101%2522%252C%2522pname%2522%253A%2522%255Cu5c71%255Cu4e1c%255Cu7701%2522%252C%2522cname%2522%253A%2522%255Cu6d4e%255Cu5357%255Cu5e02%2522%257D; vip_province=103107; vip_province_name=%E5%B1%B1%E4%B8%9C%E7%9C%81; vip_city_name=%E6%B5%8E%E5%8D%97%E5%B8%82; vip_city_code=103107101; vip_wh=VIP_BJ; vip_ipver=31; user_class=a; mars_sid=4f4e4d44e7e0e438a9064b3c460a6e45; PHPSESSID=mkro7rb2c8dngtvr2reqigblh0; mars_pid=0; visit_id=9D98B95441AF3888A799478DCFBE9EC0; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3105; vip_tracker_source_from=; pg_session_no=5; mars_cid=1613685844591_0610a409c5d025bd593cf23cf7df50aa'
,'referer': 'https://category.vip.com/'
,'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
        }
    html=requests.get(url,headers=headers).text
    #print(html)
    start=html.find('{"code"')
    end=html.find('："}}')+len('："}}')
    result=json.loads(html[start:end])['data']['products']
    for pid in result:
        pro_id = pid['pid']
        v2url='https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2?callback=getMerchandiseDroplets1&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=103107101&client=pc&mobile_platform=1&province_id=103107&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1613685844591_0610a409c5d025bd593cf23cf7df50aa&wap_consumer=a&productIds={}&scene=search&standby_id=nature&extParams=%7B%22stdSizeVids%22%3A%22%22%2C%22preheatTipsVer%22%3A%223%22%2C%22couponVer%22%3A%22v2%22%2C%22exclusivePrice%22%3A%221%22%2C%22iconSpec%22%3A%222x%22%7D&context=&_=1613774548752'.format(pid['pid'])
        v2html=requests.get(v2url,headers=headers).text
        start = v2html.find('{"code"')
        end = v2html.find('"}}') + len('"}}')
        result = json.loads(v2html[start:end])['data']['products'][0]
        print(result['productId'])
        print(result['brandShowName'])
        print(result['title'])
        print(result['price']['salePrice'])