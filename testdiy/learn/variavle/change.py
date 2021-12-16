"""
    类型转化
"""

var_str = "7"

# type(x) 可以检测x的类型

# str(x) 将目标x转化为字符串格式
print("str({'name':'hzm'})", str({'name': 'hzm'}))

# repr(x) 将对象x转化为表达式字符串,返回一个对象的 string 格式。
print("repr({'name':'hzm',age:23})", repr({'name': 'hzm', 'age': 20}))

# 将var_str 转化为整型 int(x,base+10)  x字符串或数字 base --进制数 默认十进制
var_num = int(var_str) + 1
print('var_str:', var_str, type(var_str), 'var_num:', var_num, type(var_num))

# 长整型 Python3.x 版本已删除 long() 函数。
# var_long = long(1)

# float() 函数用于将整数和字符串转换成浮点数。
var_f1 = float(var_str)

var_f2 = float(var_num)

print('float函数', var_f1, var_f2)


# complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
print('complex(1,3)生成复数:', complex(1, 3))

# 括号中有使用+号时不能出现空格
print("complex('2+5j')生成复数:", complex('2+5j'))

# eval(expression[, globals[, locals]]) 迎来执行一个表达式字符串
# eg: eval('3*2') 6
var_eval1 = '2+2'
# 输出语句带变量
print('eval(%s) output %d' % (var_eval1, eval(var_eval1)))


# tuple() 将序列转化为一个元组
var_list = [1, 2, 3, 5]
# 针对字典，会返回字典key值组成的tuple
var_dic = {1: 3, 2: 'name'}

print('tuple( % s) output %r, tuple(%s) output %r' %
      (var_list, tuple(var_list), var_dic, tuple(var_dic)))


# list(tup) 方法用于将元组tup转换为列表
var_tuple = (1, 3, 5, 7, 9)
print('list(%s) output %s' % (var_tuple, list(var_tuple)))

# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
var_setx = set('runoob')
var_sety = set('google')
print(var_setx, var_sety)

print('求 var_setx | var_sety 的 并集 output %s' % (var_setx | var_sety))

print('求 var_setx & var_sety 的 交集 output %s' % (var_setx & var_sety))

print('求 var_setx - var_sety 的 差集 output %s' % (var_setx - var_sety))

print('求 var_setx ^ var_sety 的 补集 output %s' % (var_setx ^ var_sety))


# dict() 创意一个字典
"""
class dict(**kwarg)  **kwargs -- 关键字
class dict(mapping, **kwarg) mapping -- 元素的容器。
class dict(iterable, **kwarg) iterable -- 可迭代对象。
"""
# 直接调用 返回空字典
var_dic1 = dict()  # {}
# 传入关键字
var_dic2 = dict(a='a', b='b', c='c')
# 映射函数方式来构造字典
var_dic3 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# 可迭代对象方式来构造字典
var_dic4 = dict([('name', 'hzm'), ('age', 20)])
print(var_dic2, var_dic3, var_dic3)

# frozenset([iterable]) 函数将传入的可迭代的对象字典、列表、元组等返回为一个冻结集合，不能做任何处理
var_fro1 = frozenset([1, 2, 3, 4, 5, 6])
print(var_fro1)


# chr(i) 用一个范围在range(256)内的整数作为参数 返回相应的字符
print('十六进制', chr(0x30), chr(0x31), '十进制', chr(48))

# unichr(x) 将一个整数转化为Unicode字符 python 3以上改用chr()
# print('unichr(48)', unichr(48))

# ord(c) 将字符转化为整数
print("ord('a')", ord('a'))

# hex(x) 函数用于将10进制整数转换成16进制，以字符串形式表示。
print("整数转10进制 hex(120)", hex(120))

# oct(x) 将一个整数转换成 8 进制字符串
# Python2.x 版本的 8 进制以 0 作为前缀表示。
# Python3.x 版本的 8 进制以 0o 作为前缀表示。
print("整数转8进制 oct(120)", oct(120))
