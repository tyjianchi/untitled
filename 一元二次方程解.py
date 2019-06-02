import math


def quadratic(a, b, c):
    if not isinstance(a, int):
        raise TypeError('参数类型错误')
    t = b * b - 4 * a * c;
    if t >= 0:
        return (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    else:
        return '无解'


print(quadratic(1, 3, -4))
print(quadratic(2, 3, 1))
print(quadratic('a', 'b', 'c'))
