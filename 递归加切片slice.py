#递归加切片处理，可以减少各种循环代码

#包含起始位置，不包含结束位置
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[:3])
print(L[-2:-1])

X=list(range(100))
print(X[:10:2])
#list可变，可变更，tuple不可变
Z=tuple(range(10))
print(Z[:3])
Y='abcdrcfafg'
print(Y[:3])

def my_trim(str):
    x = len(str)
    str1=str
    if x==0 or str[0]!=" " and str[-1]!=" ":
       return str
    if str[0]==" ":
       str1=str[1:]
    if str[-1]==" ":
        str1=str[:-1]
    return my_trim(str1)

if my_trim('hello  ') != 'hello':
    print('测试失败!')
elif my_trim('  hello') != 'hello':
    print('测试失败!')
elif my_trim('  hello  ') != 'hello':
    print('测试失败!')
elif my_trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif my_trim('') != '':
    print('测试失败!')
elif my_trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

