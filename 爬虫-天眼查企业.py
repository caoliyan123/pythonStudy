import requests
from bs4 import BeautifulSoup
from urllib.parse import quote



headers={
    'Cookie': 'aliyungf_tc=44204f411e110a256a919feeb519d89701db6a079fb6f275538278b756bdcc5d; acw_tc=76b20f8a16124285553981412e2fbe0a7acd65021e1bcc1c671691b3eab9c5; csrfToken=ACJq1ZwYhItXkrZdfOImWH_o; jsid=SEM-BAIDU-PZ-SY-2021112-JRGW; TYCID=dc4a281066c511eb9f269d7dd6b96686; ssuid=1622506620; sajssdk_2015_cross_new_user=1; bannerFlag=true; _ga=GA1.2.1776532874.1612428559; _gid=GA1.2.2081418380.1612428559; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22237743532%22%2C%22first_id%22%3A%221776c3b3f0540f-0c04cdc4ac10d1-c791039-1049088-1776c3b3f06412%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E5%A4%A9%E7%9C%BC%E6%9F%A5%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%7D%2C%22%24device_id%22%3A%221776c3b3f0540f-0c04cdc4ac10d1-c791039-1049088-1776c3b3f06412%22%7D; tyc-user-info={%22claimEditPoint%22:%220%22%2C%22vipToMonth%22:%22false%22%2C%22explainPoint%22:%220%22%2C%22personalClaimType%22:%22none%22%2C%22integrity%22:%2210%25%22%2C%22state%22:%220%22%2C%22score%22:%220%22%2C%22announcementPoint%22:%220%22%2C%22messageShowRedPoint%22:%220%22%2C%22bidSubscribe%22:%22-1%22%2C%22vipManager%22:%220%22%2C%22monitorUnreadCount%22:%220%22%2C%22discussCommendCount%22:%220%22%2C%22onum%22:%220%22%2C%22showPost%22:null%2C%22messageBubbleCount%22:%220%22%2C%22claimPoint%22:%220%22%2C%22token%22:%22eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTU1MzExNjc1MyIsImlhdCI6MTYxMjQyOTI1NSwiZXhwIjoxNjQzOTY1MjU1fQ.Nn3HOywW6zVFA5R5bc8QmRyBMrG1caMwuZaBBRcWWzlL0WlaB31G94cNJA2qXh8n76McZBDqvP4MiOAvniV6NA%22%2C%22schoolAuthStatus%22:%222%22%2C%22userId%22:%22237743532%22%2C%22scoreUnit%22:%22%22%2C%22redPoint%22:%220%22%2C%22myTidings%22:%220%22%2C%22companyAuthStatus%22:%222%22%2C%22originalScore%22:%220%22%2C%22myAnswerCount%22:%220%22%2C%22myQuestionCount%22:%220%22%2C%22signUp%22:%221%22%2C%22privateMessagePointWeb%22:%220%22%2C%22nickname%22:%22%E5%B0%91%E7%9A%9E%22%2C%22privateMessagePoint%22:%220%22%2C%22bossStatus%22:%222%22%2C%22isClaim%22:%220%22%2C%22yellowDiamondEndTime%22:%220%22%2C%22new%22:%221%22%2C%22yellowDiamondStatus%22:%22-1%22%2C%22pleaseAnswerCount%22:%220%22%2C%22bizCardUnread%22:%220%22%2C%22vnum%22:%220%22%2C%22mobile%22:%2215553116753%22%2C%22riskManagement%22:{%22servicePhone%22:null%2C%22mobile%22:15553116753%2C%22title%22:null%2C%22currentStatus%22:null%2C%22lastStatus%22:null%2C%22quickReturn%22:false%2C%22oldVersionMessage%22:null%2C%22riskMessage%22:null}}; tyc-user-info-save-time=1612429256667; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTU1MzExNjc1MyIsImlhdCI6MTYxMjQyOTI1NSwiZXhwIjoxNjQzOTY1MjU1fQ.Nn3HOywW6zVFA5R5bc8QmRyBMrG1caMwuZaBBRcWWzlL0WlaB31G94cNJA2qXh8n76McZBDqvP4MiOAvniV6NA; tyc-user-phone=%255B%252215553116753%2522%255D; searchSessionId=1612429297.38232322; relatedHumanSearchGraphId=23402373; relatedHumanSearchGraphId.sig=xQxyUIDqVdMkulWk5m_htP28Pzw8_eM8tUMIyK4_qqs; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1612428559,1612429604; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1612429626; RTYCID=e517fb1a353e4f37ba487a71fdd756ff; CT_TYCID=f9ab2b7acdab46b984b0b90783b6085e; cloud_token=cc816e8cb7cd4db6a0f4b76f8cf24dba; cloud_utm=3c96386797d34eeea70e2078a78417ec'
,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

lst=['华为','小米','鼎兴达','百度']
for com in lst:
    url = 'https://www.tianyancha.com/search?key='+quote(com)
    html = requests.get(url,headers=headers)
    html.encoding=html.apparent_encoding
    soup=BeautifulSoup(html.text,'lxml')

    innerUrl=soup.select_one('a.name')['href']
    innerHtml=requests.get(innerUrl,headers=headers)
    soup=BeautifulSoup(innerHtml.text,'lxml')
    divs=soup.select('.table.-striped-col tbody tr td ')
    for i in divs:
        with open('company.txt','a',encoding='utf-8')as f:
            f.write(i.text)
    with open('company.txt','a',encoding='utf-8')as f:
        f.write('\n')


