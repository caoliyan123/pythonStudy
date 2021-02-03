import requests


url = 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3210048090,1421505547&fm=26&gp=0.jpg'

html=requests.get(url)
html.encoding='utf8'
html.encoding=html.apparent_encoding
print(html.content)
with open('1.jpg','wb') as f:
    f.write(html.content)
