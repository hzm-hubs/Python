# 条件语句

"""
判断语句
if 条件表达式:
    判断结果为true，执行
elif 二次判断:
    二次判断为true, 执行
else:
    其他情况执行
"""

if 10 > 12:
    print('10 小于 12')
elif 10 > 11:
    print('10 小于 11')
else:
    print('10')

# 写在一行的语句组
if (8 is 0):
    print('检查出是数字类型')
else:
    print(type(8))


# 循环语句
# while
"""
当 condition 一直为true时将会一直执行
while(condition):
    statements
"""
# eg
dataList = [1, 2, 3, 4, 5, 6]
# 偶数列表
even = []
# 奇数列表
odd = []

lengthlist = len(dataList)
i = 0
while i < lengthlist:
    # 能整除 2 的判定为偶数 append 从列表右端推入元素
    if dataList[i] % 2 == 0:
        even.append(dataList[i])
    # 失败的为奇数
    else:
        odd.append(dataList[i])
    i += 1
    # print('i 累加', i)
print('数据源 %s 分类结果:\n偶数列表：%s,奇数列表:%s' % (dataList, even, odd))


"""
for循环 用于遍历任何序列的项目，如一个列表或者一个字符串。
for iterabting in sequence:
    statements(s)
"""

# 起始
forList = [1, 2, 3, 4, 5, 6]
# 输出列表
outputList = []
for i in forList:
    outputList.append(i+2)
print('for 循环处理元素都＋2', outputList)

"""
 while 与 for 都适用
 break 跳出整个循环
 continue 体哦啊出本次循环 执行下一个
"""

"""
pass 语句用于占位，报纸结果完成
下方的 pass 便是占据一个位置，因为如果定义一个空函数程序会报错，
当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行。
"""


def sample():
    pass
