import datetime

# 输出语法 print(……)
print('hello, word')

nowTime = datetime.datetime.now().strftime('%m/%d %H:%M')
# 同行输出 用逗号隔开
print('hello, word'), print('当前时间:', nowTime)


# 接收语法 input()
var1 = input('请输入你的名字')
print('接收到的输入值', var1)
