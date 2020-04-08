import numpy
import operator
#删除
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
#登记    
import time
import datetime
s=[]
def deng(num,name,s):  
    flag=0
    n=0
    for i in range(len(s)):
        if (s[i][0]==num): #判断列表里面有没有此学号      
            flag=1#如果有则变为1
            if(len(s[i])==4):
                n=1
            else:
                n=0
    if flag==1:
        if n==1:
            s.append((num,name,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),))
        else:
            return '该同学在校园内'
    if flag==0:#没有则添加
        s.append((num,name,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),))
        return '登记成功'

#添加离校时间        
def lixiao(arr,c):
    a=[]
    s=0
    num=len(arr)
    print(num)
    if num==1:
        num=num+1
    for i in range(0,num-1):
        if arr[i][0]==c:
            a=arr[i]
            arr.pop(i)
            b= list(a)#将元祖转换成列表
            b.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            arr.append(tuple(b))
            s=1
    if(s==0):
        return '没有找到此记录'
    return arr

def display(s):
    sort1(s)  #排序函数
    for i in range(len(s)):
        print(s[i])
#离校人数
def count1(s):
    count=0
    for i in range(len(s)):
        if len(s[i])==4:
            count +=1
    return count

def sort1(s):
    result = sorted(s,key=operator.itemgetter(0))
    for i in range(len(s)):
        print(result[i],'\n')

#按照登记时间查询        
def time_filter(s,st,et):
    for i in range(len(s)):
        if (s[i][2]>=st):  #开始时间
            if (s[i][2]<=et):  #末尾时间
                print(s[i])

#按照学号查询
def research(a,x):
    flag=0
    for i in range(0,len(a)):
        if a[i][0]==x:
            if(len(a[i])==3):
                 print("学号:%s, 姓名:%s, 进校时间:%s"%(a[i][0],a[i][1],a[i][2]))
            else:
                print("学号:%s, 姓名:%s, 进校时间:%s, 离校时间:%s"%(a[i][0],a[i][1],a[i][2],a[i][3]))
            flag=1
    if flag==0:
        print("未查询到相关信息")
                
       
  
            
            
        
