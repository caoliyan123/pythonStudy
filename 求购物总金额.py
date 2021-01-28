#coding:utf-8
"""
根据图书单价，购买数量及快递费，计算买家需要支付的总金额
假设店铺满68包邮。
"""

class payMoney:
    book = {'Python':45,'Math':23,'English':44}  #定义书名及价格

    def __init__(self,bookName,num,freePrice):
        self.bookName = bookName
        self.num = num
        self.freePrice = freePrice  #免运费的阈值


    def buyBook(self):
        price = payMoney.book.get(self.bookName)
        if price:
            total = price * self.num
            return total + 5 if total < self.freePrice else total
        return '这不是我们店铺的书{0}'.format(self.bookName)

        #return float(price) * int(self.num) + 5 if float(price) * int(self.num) < self.freePrice else float(price) * int(self.num)


a = payMoney('python',1,88)
print(a.buyBook())