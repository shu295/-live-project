#!/usr/bin/env python
# coding: utf-8

# In[7]:


def info():#界面


    huabu = Canvas(root,width=1000,height=500,background="white")
    huabu.place(x=0, y=0)
    huabu.pack()
    huabu.create_line(300, 0,300, 500)
    huabu.create_line(0, 140,300, 140)
    huabu.create_line(0, 270,300, 270)
    huabu.create_line(0, 400,300, 400)
    huabu.create_line(160, 270,160, 400)

    w = Label(root, text="学号：")
    w.pack()
    w.place(x=20, y=30)
    
    s = Label(root, text="姓名：")
    s.pack()
    s.place(x=150, y=30)

    #v1 = StringVar()
    #p1 = StringVar()
    #text1 = Entry(root, textvariable=v1)  # Entry 是 Tkinter 用来接收字符串等输入的控件.
    #text2 = Entry(root, textvariable=p1)
    text1=Text(root,width=10,height=1)#创建text组件
    text1.pack()
    text1.place(x=60, y=30)
    
    text2=Text(root,width=10,height=1)#创建text组件
    text2.pack()
    text2.place(x=190, y=30)

    tianjia = Button(width=15,height=2, command= lambda: deng(int(text1.get('0.0',END)),text2.get('0.0',END),datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),''))
    tianjia['text']='入校登记'
    tianjia.pack()
    tianjia.place(x=100, y=70)


    w = Label(root, text="学号：")
    w.pack()
    w.place(x=20, y=160)
    
    
    text3=Text(root,width=10,height=1)#创建text组件
    text3.pack()
    text3.place(x=60, y=160)
    

    shanchu = Button(width=15,height=2, command= lambda: lixiao(int(text3.get('0.0',END))))
    shanchu['text']='离校登记'
    shanchu.pack()
    shanchu.place(x=100, y=200)

    w = Label(root, text="学号：")
    w.pack()
    w.place(x=20, y=290)
    
    s = Label(root, text="时间：")
    s.pack()
    s.place(x=180, y=290)
    
    text5=Text(root,width=10,height=1)#创建text组件
    text5.pack()
    text5.place(x=60, y=290)
    
    text6=Text(root,width=10,height=1)#创建text组件
    text6.pack()
    text6.place(x=220, y=290)

    shanchu = Button(width=10,height=2, command= lambda: research(int(text5.get('0.0',END))))
    shanchu['text']='查询'
    shanchu.pack()
    shanchu.place(x=30, y=330)

    shanchu = Button(width=10,height=2, command= lambda: time_filter(text6.get('0.0',END)))
    shanchu['text']='查询'
    shanchu.pack()
    shanchu.place(x=200, y=330)

    xianshi = Button(width=15,height=2)
    xianshi['text']='显示数据'
    xianshi['command']=xianshi1
    xianshi.pack()
    xianshi.place(x=10, y=450)
    
    renshu()


# In[8]:


def xianshi1():#显示数据
    listb=Label(root, text="出入学校信息")
    listb.pack()
    listb.place(x=400, y=30)
    mlb = MultiListbox(root,(('学号', 10),('姓名', 10),("入校时间", 25),("离校时间", 25)))
    for item in sorted(s,key=operator.itemgetter(0)):
        mlb.insert(END,('%d' % item[0],'%s' % item[1], '%s' % item[2], '%s' % item[3]))
    mlb.pack(expand=YES, fill=BOTH)
    mlb.place(x=400, y=50)


# In[9]:


def deng(num,name,time1,time2):  #入校登记
    flag=0
    t1=time1
    for i in range(len(s)):
        if (s[i][0]==num) & (s[i][3]==''): #判断列表里面有没有此学号且没有写离开时间       
            flag=1#如果有则变为1
    if flag==0:#没有则添加
        s.append((num,name,t1,time2))
        tkinter.messagebox.showinfo('提示', '登记成功')
    else:
        tkinter.messagebox.showinfo('提示', '该同学还在学校')
    renshu()


# In[17]:


class MultiListbox(Frame):

    def __init__(self,master,lists):
        Frame.__init__(self,master)
        self.lists = []
        for l, w in lists:
            frame = Frame(self)
            frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=0, selectborderwidth=0, relief=FLAT, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind("<B1-Motion>",lambda e, s=self: s._select(e.y))
            lb.bind("<Button-1>",lambda e,s=self: s._select(e.y))
            lb.bind("<Leave>",lambda e: "break")
            lb.bind("<B2-Motion>",lambda e,s=self: s._b2motion(e.x,e.y))
            lb.bind("<Button-2>",lambda e,s=self: s._button2(e.x,e.y))
        frame = Frame(self)
        frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame,orient=VERTICAL, command=self._scroll)
        sb.pack(side=LEFT, fill=Y)
        self.lists[0]["yscrollcommand"] = sb.set

    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return "break"

    def _button2(self, x, y):
        for l in self.lists:
            l.scan_mark(x,y)
        return "break"

    def _b2motion(self, x, y):
        for l in self.lists:
            l.scan_dragto(x, y)
        return "break"

    def _scroll(self, *args):
        for l in self.lists:
            apply(l.yview, args)
        return "break"

    def curselection(self):
        return self.lists[0].curselection()

    def delete(self, first, last=None):
        for l in self.lists:
            l.delete(first,last)

    def get(self, first, last=None):
        result = []
        for l in self.lists:
            result.append(l.get(first,last))
        if last:
            return apply(map, [None] + result)
        return result

    def index(self, index):
        self.lists[0],index(index)

    def insert(self, index, *elements):
        for e in elements:
            i = 0
            for l in self.lists:
                l.insert(index, e[i])
                i = i + 1

    def size(self):
        return self.lists[0].size()

    def see(self, index):
        for l in self.lists:
            l.see(index)

    def selection_anchor(self, index):
        for l in self.lists:
            l.selection_anchor(index)

    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first,last)

    def selection_includes(self, index):
        return self.lists[0].seleciton_includes(index)

    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)


# In[20]:


#添加离校时间        
def lixiao(c):
    a=[]
    q=0
    num=len(s)
    #if num==1:
        #num=num+1
    for i in range(0,num):
        if s[i][0]==c and s[i][3]=='':
            a=s[i]
            s.pop(i)
            b= list(a)#将元祖转换成列表
            b[3]=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            s.append(tuple(b))
            q=1
    if(q==1):
        tkinter.messagebox.showinfo('提示', '登记成功')
    if(q==0):
        tkinter.messagebox.showinfo('提示', '没有找到此记录')
    renshu()


# In[12]:


#按照学号查询
def research(x):
    a=s
    q=[]
    flag=0
    for i in range(0,len(a)):
        if a[i][0]==x:
            q.append(tuple(a[i]))
            flag=1
    xianshi2(q)
    if flag==0:
        tkinter.messagebox.showinfo('提示', '未查询到相关信息')


# In[13]:


def xianshi2(s):#显示查询结果
    listb=Label(root, text="出入学校信息")
    listb.pack()
    listb.place(x=400, y=30)
    mlb = MultiListbox(root,(('学号', 10),('姓名', 10),("入校时间", 25),("离校时间", 25)))
    for item in sorted(s,key=operator.itemgetter(0)):
        mlb.insert(END,('%d' % item[0],'%s' % item[1], '%s' % item[2], '%s' % item[3]))
    mlb.pack(expand=YES, fill=BOTH)
    mlb.place(x=400, y=50)


# In[14]:


#按照登记时间查询        
def time_filter(st):
    q=[]
    flag=0
    for i in range(len(s)):
        if (int(s[i][2].split(" ")[1].split(":")[0])==int(st)):  #开始时间
            q.append(tuple(s[i]))
            flag=1
    xianshi2(q)
    if flag==0:
        print(2)
        tkinter.messagebox.showinfo('提示', '未查询到相关信息')


# In[15]:


#离校人数
def count1():
    count=0
    for i in s:
        if i[3]=='':
            count=count+1
    return count
def count2():
    count=0
    for i in s:
        if i[3]!='':
            count=count+1
    return count


# In[19]:


def renshu():#人数、人次统计
    s = Label(root, text="在校人数：")
    s.pack()
    s.place(x=400, y=400)
    
    s = Label(root, text=count1())
    s.pack()
    s.place(x=470, y=400)
    
    w = Label(root, text="出校人次：")
    w.pack()
    w.place(x=600, y=400)
    
    w = Label(root, text=count2())
    w.pack()
    w.place(x=670, y=400)


# In[22]:


import time
import datetime
from tkinter import *           # 导入 Tkinter 库
import tkinter as tk
import tkinter.messagebox
import numpy
import operator
s=[]
root = Tk()                     # 创建窗口对象的背景色
root.title('my window')
root.geometry('1000x500')
root.resizable(0,0)
  
info()

mainloop() 


# In[ ]:




