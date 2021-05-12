#coding:utf-8

import os
import pandas as pd
from openpyxl import load_workbook
import win32com.client as win32


def xlstoxlsx(f):
    fname=dirPath
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(fname)
    wb.SaveAs(fname + "x", FileFormat=51)  # FileFormat = 51 is for .xlsx extension
    wb.Close()  # FileFormat = 56 is for .xls extension
    excel.Application.Quit()
    n_fname=fname.split('.')[0]+'.xlsx'
    os.remove(fname)
    return n_fname

if __name__ == '__main__':
    dirPath = r'C:\Users\Yan\Desktop\1-7子表\1-7子表\中学合格\莲塘六中-省廉洁档案\莲塘六中-省廉洁档案\表4\36012119861120392X万萍兰.xls'
    print(xlstoxlsx(dirPath))
    #print(addSheet(dirPath))