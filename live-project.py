import numpy
import operator
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
def sort1(s):
    result = sorted(s,key=operator.itemgetter(0))
    for i in range(len(s)):
        print(result[i],'\n')
   
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
