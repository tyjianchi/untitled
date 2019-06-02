
# d={'a':'1','b':'2','c':'3'}
#
# for i in d.values():
#     print(i)
# for i in d:
#     print(i)
# for i in 'asdfads':
#     print(i)

# Iterable模块，检查是参数是否能迭代
# enumerate模块，能同时迭代list的下标和值
# from collections import Iterable
# x='123456'
# if isinstance(x,Iterable):
#     for i,value in enumerate(x):
#         print(i,value)

# 使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if(len(L)==0):
        return(None,None)
    for i,num in enumerate(L):
#        if(i >0 and num<L[i-1]):
        if(num<L[i-1]):
            temp = L[i-1]
            L[i-1] = num
            L[i] = temp
        print(i,num,L[0],L[-1])
    minNum = L[0]
    maxNum = L[-1]

    return(minNum,maxNum)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')