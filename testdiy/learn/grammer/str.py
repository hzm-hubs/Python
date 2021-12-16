# 字符串语法

var1 = 'Hello World!'

print("输出 :- ", var1[:6] + 'Runoob!')

# """
# 转义字符
# \(在行尾时)	续行符
# \\	反斜杠符号
# \'	单引号
# \"	双引号
# \a	响铃
# \b	退格(Backspace)
# \e	转义
# \000	空
# \n	换行
# \v	纵向制表符
# \t	横向制表符
# \r	回车
# \f	换页
# \oyy	八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
# \xyy	十六进制数，以 \x 开头，yy代表的字符，例如：\x0a代表换行
# \other	其它的字符以普通格式输出
# """


# """
# 字符串运算符

# +	字符串连接
# >>>a + b
# 'HelloPython'


# *	重复输出字符串
# >>>a * 2
# 'HelloHello'


# []	通过索引获取字符串中字符
# >>>a[1]
# 'e'


# [ : ]	截取字符串中的一部分
# >>>a[1:4]
# 'ell'


# in	成员运算符 - 如果字符串中包含给定的字符返回 True
# >>>"H" in a
# True


# not in	成员运算符 - 如果字符串中不包含给定的字符返回 True
# >>>"M" not in a
# True


# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
#  原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
# >>>print r'\n'
# \n
# >>> print R'\n'
# \n
# """

# """
# 字符串格式化
# %c	 格式化字符及其ASCII码
# %s	 格式化字符串
# %d	 格式化整数
# %u	 格式化无符号整型
# %o	 格式化无符号八进制数
# %x	 格式化无符号十六进制数
# %X	 格式化无符号十六进制数（大写）
# %f	 格式化浮点数字，可指定小数点后的精度
# %e	 用科学计数法格式化浮点数
# %E	 作用同%e，用科学计数法格式化浮点数
# %g	 %f和%e的简写
# %G	 %F 和 %E 的简写
# %p	 用十六进制数格式化变量的地址
# """

test_str = 'hello, world !'

# capitalize() 将字符串首字母大写
print('首字符', test_str.capitalize())

# center(width), 返回一个原字符串居中，并使用空格填充至长度width的新字符串
print('调用字符串center功能', test_str.center(2))

# count(str,deg-0,end=len(string)) 返回str在string 中出现的次数
# 如果beg或end知道则返回指定范围内str出现的次数
print('统计l出现的次数', test_str.count('l'))

# encode(encoding='UTF-8',errors="strict") encoding指定的编码格式编码string 如果出错默认报出
# 一个valueError的异常,除非errors指定的是'ignore'或者'replace'
encode_str = test_str.encode(encoding='UTF-8', errors="strict")
print('encode编码格式输出', encode_str)

# decode(encoding='UTF-8',errors="strict") 以encoding指定的编码格式解码string 如果出错默认报出
# 一个valueError的异常,除非errors指定的是'ignore'或者'replace'
print('decod解码格式输出', encode_str.decode('UTF-8', "strict"))
