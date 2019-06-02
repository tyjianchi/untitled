import numpy as np

def test():
    n1=np.dtype([('name', 'S20'),('age','i1'),('amount','i1')])
    n2=np.array([('ddd',10,1000),('xxxxx',12,2222)],dtype=n1)
    print(n2[:2]['age'])

def test1():
    list = range(5)
    it = iter(list)
    # 使用迭代器创建 ndarray
    print(it)
    x = np.fromiter(it, dtype=float)
    print(x)
def test2():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # print(a[..., 1])  # 第2列元素
    # print(a[1, ...])  # 第2行元素
    print(a[...,1:])
def test3():
    x = np.arange(32).reshape((8, 4))
    print(x)
    print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
def test4():
    a = np.array([[0, 0, 0],
                  [10, 10, 10],
                  [20, 20, 20],
                  [30, 30, 30]])
    b = np.array([1, 2, 3])
    bb = np.tile([1,2,3], (4,1))
    print(bb)
    print(a + b)
def test5():
    a = np.arange(6).reshape(2, 3)
    print('原始数组是：')
    print(a)
    print('\n')
    print('迭代输出元素：')
    for x in np.nditer(a):
        print(x, end=", ")
    print('\n')
def test6():
    x = np.array([[1], [2], [3]])
    y = np.array([[4, 5, 6]])

    # 对 y 广播 x
    b = np.broadcast(x, y)
    # 它拥有 iterator 属性，基于自身组件的迭代器元组
    print(((b.iters)))
    print('对 y 广播 x：')
    r, c = b.iters

    # Python3.x 为 next(context) ，Python2.x 为 context.next()
    # print(next(r), next(c))
    # print(next(r), next(c))
    # print(next(r), next(c))
    # print('\n')
    # shape 属性返回广播对象的形状

    # print('广播对象的形状：')
    # print(b.shape)
    # print('\n')
    # 手动使用 broadcast 将 x 与 y 相加
    b = np.broadcast(x, y)
    c = np.empty(b.shape)

    print('手动使用 broadcast 将 x 与 y 相加：')
    print(c.shape)
    print('\n')
    c.flat = [u + v for (u, v) in b]

    print('调用 flat 函数：')
    print(c)
    print('\n')

    # # 获得了和 NumPy 内建的广播支持相同的结果
    #
    print('x 与 y 的和：')
    print(x + y)
test6()