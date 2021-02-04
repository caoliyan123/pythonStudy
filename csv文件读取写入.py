import csv

#csv 文件写入

# with open('11.csv','w') as csvfile:
#     csvwirter = csv.writer(csvfile,
#                            delimiter=' ')
#
#     csvwirter.writerow(['python']*5)
#     csvwirter.writerow(['scala','go','c++'])

#csv 文件读取
with open('11.csv','r') as file:
    readfile = csv.reader(file)
    for i in readfile:
        if i :print (i)