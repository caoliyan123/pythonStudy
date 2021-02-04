import requests

html=requests.get('https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20180715%2F1e7cddb491fa40058b33cb47c15925e9.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1614998623&t=b2571112cf4527b2f731dd3728f8efd3')
print(html.content)

with open('1.jpg','wb') as f:
    f.write(html.content)

