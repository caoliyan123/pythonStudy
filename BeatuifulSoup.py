import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.baidu.com/s?word=python'
headers = {
'Cookie': 'BIDUPSID=337EDD6B3E02CD60B034BB1D17A83E05; PSTM=1608530794; BD_UPN=12314753; BAIDUID=61DE3F27658F126305D7D81ADD81D779:FG=1; BDUSS=FUZ2RsaWt6Q0I3UHpSSUdnUmJTRU1QVXpvNkFwa002eEVPRjA1TFltU0h-QnhnRVFBQUFBJCQAAAAAAAAAAAEAAABO6QUb0-q8vtGpx6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIdv9V-Hb~VfRl; BDUSS_BFESS=FUZ2RsaWt6Q0I3UHpSSUdnUmJTRU1QVXpvNkFwa002eEVPRjA1TFltU0h-QnhnRVFBQUFBJCQAAAAAAAAAAAEAAABO6QUb0-q8vtGpx6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIdv9V-Hb~VfRl; __yjs_duid=1_d905ab1de7f15e22a1071d62157c681e1611537975521; MCITY=-288%3A; BAIDUID_BFESS=6D4B3CD035392BBE33DC98FA18636A53:FG=1; BDRCVFR[8gzLr2xelNt]=IdAnGome-nsnWnYPi4WUvY; delPer=0; BD_CK_SAM=1; PSINO=2; H_PS_PSSID=33423_33517_33358_33273_31254_33595_33460_26350; sugstore=1; COOKIE_SESSION=13_0_4_5_7_2_0_0_4_1_0_0_5012_0_0_0_1612341745_0_1612402842%7C9%23350804_12_1611629593%7C7; H_PS_645EC=a7c7lp%2FOqGkroPHgpGevA%2FAsiiPQbFOSApepYG0Yc%2Bi3mHXdO5PC2BiupqE; BA_HECTOR=al850g05848k0l017h1g1mk4r0r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1611629114,1611890190,1612238963,1612402846; Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1612402846'
,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

html = requests.get(url,headers=headers)
html.encoding=html.apparent_encoding
soup=BeautifulSoup(html.text,'lxml')
for i in soup.select('div.result.c-container h3 a'):
    print(i['href'])
