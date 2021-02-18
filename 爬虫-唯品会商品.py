#coding=utf-8
import requests

for i in range(0,500,120):
    url='https://mapi.vip.com/vips-mobile/rest/shopping/pc/search/product/rank?callback=getMerchandiseIds&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=103107101&client=pc&mobile_platform=1&province_id=103107&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1612492176417_4a8975a3508b3c07e5e52711cb87a04c&wap_consumer=a&standby_id=nature&keyword=护肤套装&lv3CatIds=&lv2CatIds=&lv1CatIds=&brandStoreSns=&props=&priceMin=&priceMax=&vipService=&sort=0&pageOffset={}&channelId=1&gPlatform=PC&batchSize=120&_=1613636273022'.format(i)
    headers={
        'cookie': 'vip_cps_cuid=CU1612490862651f08678e0d86548392; vip_cps_cid=1612490862654_f269c5410c2794e3929ff6a3239445c9; vip_wh=VIP_NH; PAPVisitorId=c94b8d4ebef70e7233f995717f027bab; vip_new_old_user=1; mars_pid=0; _jzqco=%7C%7C%7C%7C%7C1.436013481.1612491528912.1612491528912.1612491528912.1612491528912.1612491528912.0.0.0.1.1; VipRUID=177860578; VipUID=3b2e501f78e448ef5ad8ffa8148983f5; VipRNAME=155*****753; cps_share=cps_share; cps=adp%3AC01V4m9vjc9h6b5c%3A%40_%401613636385195%3Amig_code%3ADL001%3Aac010cnh1nbgfx9u4f1w846ta697h0de; vip_address=%257B%2522pname%2522%253A%2522%255Cu5e7f%255Cu4e1c%255Cu7701%2522%252C%2522pid%2522%253A%2522104104%2522%252C%2522cname%2522%253A%2522%255Cu5e7f%255Cu5dde%255Cu5e02%2522%252C%2522cid%2522%253A%2522104104101%2522%257D; vip_province=104104; vip_province_name=%E5%B9%BF%E4%B8%9C%E7%9C%81; vip_city_name=%E5%B9%BF%E5%B7%9E%E5%B8%82; vip_city_code=104104101; user_class=c; VipUINFO=luc%3Ac%7Csuc%3Ac%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3102; mars_sid=de59fce838b0d10689882c893c09748c; PHPSESSID=6q79aarsjp89470b9j55spdgq5; visit_id=FBE324A0974D7C13A576B1FF43B1478A; pg_session_no=4; vip_tracker_source_from=; mars_cid=1612490865911_4da099c564802c81ad3a13b7097d3880',
        'referer': 'https: // category.vip.com /',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    html=requests.get(url,headers=headers)
    print (html.text)
