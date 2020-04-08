from tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色

root.title('my window')
root.geometry('1000x500')
root.resizable(0,0)


s = [(211706135,'wlp','2020-04-20 16:00:00','2020-04-22 23:00:00'),
     (211706127,'ts','2020-04-19 16:00:00','2020-04-22 23:00:00'), 
     (211706147,'lxy','2020-04-16 16:00:00','2020-04-24 22:00:00'),
     (211706167,'hwz','2020-04-29 14:00:00','2020-04-30 23:00:00'),
     (211706127,'wlp','2020-04-19 14:00:00','2020-04-22 23:00:00')]

listb  = Listbox(root,width=50,height=15)          #  创建两个列表组件

for item in s:                 # 第一个小部件插入数据
    listb.insert(0,item)

tianjia = Button(width=15,height=2)
tianjia['text']='登记'
tianjia['command']=tianjia1
tianjia.pack()
tianjia.place(x=100, y=50)

chaxun = Button(width=15,height=2)
chaxun['text']='查询'
chaxun['command']=chaxun1
chaxun.pack()
chaxun.place(x=100, y=100)

shanchu = Button(width=15,height=2)
shanchu['text']='删除'
shanchu['command']=shanchu1
shanchu.pack()
shanchu.place(x=100, y=150)

suoyou = Button(width=15,height=2)
suoyou['text']='所有人员'
suoyou['command']=suoyou1
suoyou.pack()
suoyou.place(x=100, y=200)


listb.pack()                    # 将小部件放置到主窗口中
root.mainloop()                 # 进入消息循环


import numpy
def delete(arr,c):
    s=0
    if len(arr)==0 :
        return '还没有记录，无法删除'
    res_list = [x[0] for x in arr]#获取学号
    for i in range(0,len(res_list)):#查找学号下标
        if res_list[i]==c:
            arr.pop(i) #s删除此条记录
            s=1
    if(s==0):
        return '还未添加此记录'
    else:
        return arr
    
import time
import datetime
s=[(211706127,'ts',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'2020-04-08 18:11:23'),
   (211706129,'wcf',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'2020-04-08 18:11:23'),
   (211706146,'yl',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'2020-04-08 18:11:23'),
   (211706130,'wlp',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'2020-04-08 18:11:23'),]
def deng(num,name):  
    flag=0
    for i in range(len(s)):
        if s[i][0]==num:#判断列表里面有没有此学号
            flag=1#如果有则变为1
    if flag==0:#没有则添加
        s.append((num,name,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),))
deng(211706126,'www')
def display(s):
    #排序函数
    for i in range(len(s)):
        print(s[i])
        
        

import numpy
s =input()
s =s.split(",")
def count1(s):
    count=0
    for i in range(len(s)):
        for j in range(4):
            if s[i][3]==null:
                count +=1
    return count
print("当前离校人数为"，count1(s))
print("当前在校人数为"，len(s)-count1(s))
def sort1(s):
    result = sorted(s,key=operator.itemgetter(0))
    for i in range(len(s)):
        print(result[i],'\n')

import numpy
s =input()
s =s.split(",")
def count1(s):
    count=len(s)
    for i in range(len(s)):
        for j in range(4):
            if string(s[i][3])==null:
            count -=1
    return count
print("当前在校人数为",count1(s))
print("当前离校人数为"，len(s)-count1(s))
