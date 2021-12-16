# 数字类型相关操作
import math

# 随机函数模块
import random
var1 = 1
# 使用del语句删除一些 Number 对象引用。
del var1
# print(var1) 提示var1未定义

# math(数学运算模块) cmath(复数运算模块)
# 列出 math 模块中可以使用的
print(dir(math))
"""
abs(x)	        返回数字的绝对值，如abs(-10) 返回 10

ceil(x)	        返回数字的上入整数，如math.ceil(4.1) 返回 5

cmp(x, y)	    如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1

exp(x)	        返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045

fabs(x)	        返回数字的绝对值，如math.fabs(-10) 返回10.0

floor(x)	    返回数字的下舍整数，如math.floor(4.9)返回 4

log(x)	        如math.log(math.e)返回1.0,math.log(100,10)返回2.0

log10(x)	    返回以10为基数的x的对数，如math.log10(100)返回 2.0

max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。

min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。

modf(x)	        返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。

pow(x, y)	    x**y 运算后的值。

round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。

sqrt(x)	        返回数字x的平方根
"""
print('5.62662 四舍五入2位是', round(5.62662, 2))
print('[1,22,3,34,52,16] 中的最大值是', max([1, 22, 3, 34, 52, 16]))

"""
随机数函数

函数	描述
通过 import random 引入随机模块后 就可以使用choice、randrange()方法了
如： random.randrange(100,1000,3) random.random(100,1000,3)


choice(seq)	                        从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。

randrange([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1

random()	                        随机生成下一个实数，它在[0,1)范围内。

seed([x])	                        改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。

shuffle(lst)	                    将序列的所有元素随机排序

uniform(x, y)	                    随机生成下一个实数，它在[x,y]范围内。
"""

getinput = int(input('请输入随机数的上限'))
outrand = random.choice(range(getinput))
outlitter = random.random()
print('输出随机数', outrand, outlitter)

"""
数学常量
pi 圆周率
e  数学常量e,自然常熟
"""

"""
此外还有三角函数 tan(x)、sin(x)…………
"""
