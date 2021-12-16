responses={}  #先定义一个字典
polling_active=True
while polling_active:
    name=str(input("\n请输入你的名字:"))
    response=str(input("which mountain would you like to climb someday?"))
    responses[name]=response   #建立键值对关系，前面的表示键，后面的respons表示值
    repeat = str(input("would you like to let another person respond?(yes/no)"))
    if repeat=='no': #注意no俩边的'号,没有会显示no没有被定义
        polling_active=False  #若执行if语句，会给poll_active赋予false,令while循环结束，若不执行，可以一直循环
    print("\n---poll results ---")  #poll results 表示
    for name ,response in responses.items():  #这里的逗号，表示name，response都要参加下面的循环，.items()把字典，用以列表返回可遍历的(键，值)元组数组，与字典搭配使用
        print(name+" would like to climb "+response+".")   # 注意上方的格式