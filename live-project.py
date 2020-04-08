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
