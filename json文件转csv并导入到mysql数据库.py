#coding:utf-8
import json
import csv

with open('E:\\学习\\数据分析\\SQL作业附件 (1)\\SQL作业附件\\airplanes.json','r',encoding='utf-8')as fp:
    json_data=json.load(fp)
    json_str=json_data['data']
    with open('E:\\学习\\数据分析\\SQL作业附件 (1)\\SQL作业附件\\airplanes.csv','a',encoding='utf-8',newline='')as fc:
        csv_writer = csv.writer(fc)
        count=0
        for i in json_str:
            if count==0:
                #写入表头
                csv_writer.writerow(i.keys())
                count+=1
            csv_writer.writerow(i.values())




