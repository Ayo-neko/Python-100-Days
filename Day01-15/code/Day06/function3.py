"""
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


def myfilter(mystr):
    return len(mystr) == 10


# help()
print(abs(-1.2345))
print(divmod(10, 3))
print(pow(2, 3))
print(round(-1.2345, 2))

print(chr(0x9a86))
print(hex(ord('骆')))

fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)])
fruits2 = list(filter(myfilter, fruits))
print(fruits2)