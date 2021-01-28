#coding:utf-8
"""
定义一个类，用阿拉伯数字实例化以后，得到罗马数字
"""
#阿拉伯数字转换成罗马数字
class albaInt:
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    str_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]



    def albatormon(self,n):
        number = n
        result = ""
        for i in range(len(self.num_list)):
            while number >= self.num_list[i]:
                number -= self.num_list[i]
                result += self.str_list[i]
        return  result

#罗马数字转换为阿拉伯数字

    def romantoalba(self,roman):
        intger = 0
        for i in range(len(self.num_list)):
            while roman >=





a = albaInt()

print (a.albatormon(1024))
