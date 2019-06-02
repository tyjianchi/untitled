from functools import reduce
# MAP(fun,x):fun需一个入参，循环处理每一个入参,最后输出tuple
# Reduce(fun,y)：fun必须2个入参，循环处理每次输入的2个入参（y为集合），最后合并为一个输出

def f(x,y):
    return x*y

# print(list(map(f,L)))

def str2num(x):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}
    return digits[x]
def fn(x,y):
    return x*10+y

num1 = ['1', '2', '3']
num2 = '1234'
num3 = {'1', '2', '3'}

#print(reduce(f,[1,2,3,4]))

str = ['adam', 'LISA', 'barT']


def str2format(x):
 return x[0].upper()+x[1:].lower() #递归切片

 #循环处理
    # z,y=0,''
    # while z < len(x):
    #   if z==0:
    #       y=y+x[z].upper()
    #   else:
    #       y=y+x[z].lower()
    #   z=z+1
    # return y

def prod(x):
    return (reduce(f,x))

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

def str2float(x):
    str=list(map(str2num,x.replace('.','')))
    return reduce(fn,str)/pow(10, len(x) - 1 - x.index('.'))


# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')
def order(x):
    return x[::-1]#倒序输出：input:456 output:654

print(order('abc'))