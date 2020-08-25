import pandas as pd                         #导入pandas包
import re
import tkinter as tk
from tkinter import filedialog

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()
Filepath = filedialog.askopenfilename() #获得选择好的文件
print('Filepath',Filepath)
midfile = 'C:/CSVtoTXT/'+Filepath[-13:-4]+'_temp.txt'
outfile = 'C:/CSVtoTXT/'+Filepath[-13:-4]+'.txt'
Filepath.replace('\\', '@')


data = pd.read_csv(Filepath,encoding = "utf-16-le",error_bad_lines=False)           	#读取csv文件
print(data)
data.to_csv(midfile, sep=' ')
ressave = ''


with open(midfile, 'r',encoding = "utf-8") as fr:     #打开中转文档
    pattern_obj = re.compile('=')
    res1=re.sub(pattern_obj,'',fr.read())          #将等号替换
    list1 = []
    list1 = res1.split('''\"''')              #按""分割
    x = 0
    for i in list1:
        pattern_obj = re.compile('(;.*)')     #re过滤;后字符
        res = re.search(pattern_obj,i)
        if res != None:                        #排除空行
            ressave = res.group(0)
            ressave2 = ressave.replace(";","")      #过滤无效字符
            ressave3 = ressave2.replace(' ',';',2)
            with open(outfile, 'a+',encoding = "utf-8") as fr2:           #保存
                fr2.write(ressave3+"\n")
        x+=1

