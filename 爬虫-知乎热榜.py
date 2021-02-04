import requests
import re
from bs4 import BeautifulSoup
import os

headers={
'cookie': '_zap=ce8af1c4-4adf-43cd-9224-1c8c06db489b; _xsrf=mSmyQnh2uy6IinMR31RvPoEnGQlyWg1B; d_c0="AIAWr25CaxKPTruVspOusUk_22jW7RC6XBk=|1609215708"; z_c0="2|1:0|10:1609215734|4:z_c0|92:Mi4xNUZwN0F3QUFBQUFBZ0JhdmJrSnJFaVlBQUFCZ0FsVk45dnpYWUFER0ljcmtYLUdVS0NTSGtjQS01d1hmMjlfSGV3|4cdf8e9583d7fc880b4aedcf34fdda206fba9e57ed7f96f9e917bf94309375e9"; q_c1=4936a75b469e4ff9b90e708e6571047e|1610011799000|1610011799000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1611192904,1611197398,1612251405,1612420096; SESSIONID=pmTo4RtcXZFMU0iNbIDSLiOcoMpY5iufUipqTCyLWwC; JOID=VFwQAU_dBR6Fe-PLPNklDCsLpaAtr2lN7E2zvliHXVnPKNGgc9yXBOF74M09KjSHYhEBSIB93Rzy-QBFCdlNv2M=; osd=U1wQBUraBR6BfuTLPN0gCysLoaUqr2lJ6UqzvlyCWlnPLNSnc9yTAeZ74Mk4LTSHZhQGSIB52Bvy-QRADtlNu2Y=; tst=h; tshl=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1612420250; KLBRSID=37f2e85292ebb2c2ef70f1d8e39c2b34|1612420248|1612420093'
,'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
html=requests.get('https://www.zhihu.com/billboard',headers=headers)
html.encoding=html.apparent_encoding
soup=BeautifulSoup(html.text,'lxml')
divs=soup.select('.HotList-item')
num=0
for i in divs:
    title=i.select('.HotList-itemBody .HotList-itemTitle')[0].text
    print('标题：', title)
    hot = i.select('.HotList-itemBody .HotList-itemMetrics')[0].text
    print('热度：', hot)

    try:
        if not os.path.exists('zhihu'):
            os.mkdir('zhihu')
        img = i.select(' .HotList-itemImgContainer img')[0]['src']
        with open('zhihu/{}.jpg'.format(num),'wb') as f:
            f.write(requests.get(img).content)
        num+=1
    except:
        pass

re_mark = re.compile('"excerptArea":{"text":"(.*?)"}')
result=re_mark.findall(html.text)
for j in result:
    print('简介：',j)


