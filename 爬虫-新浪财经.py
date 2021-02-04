import requests
from bs4 import BeautifulSoup

url='https://finance.sina.com.cn/'
html=requests.get(url)
html.encoding=html.apparent_encoding
soup=BeautifulSoup(html.text,'lxml')
divs=soup.select('.m-p1-m-blk2 .m-p1-mb2-list.m-list-container ul li a')
for i in divs:
    if len(i.text)>3 and i['href'].endswith('shtml'):
        innerUrl=i['href']
        innerHtml=requests.get(innerUrl)
        innerHtml.encoding=innerHtml.apparent_encoding
        soup=BeautifulSoup(innerHtml.text,'lxml')
        innerDivs=soup.select('.article p')
        content=''
        for j in innerDivs:
            content+=j.text
        print(i.text,i['href'])
        print(content)

        with open('sinaFinance.txt','a',encoding='utf8')as f:
            f.write(content+'\n')


