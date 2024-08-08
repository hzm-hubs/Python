# 字典
confirm_users={}
while True:
    name=str(input("请输入需要充值的账号:"))
    password=str(input("请输入密码:"))  
    confirm_users[name]=password  #建立键值关系
    print("\t请输入需要充值点卷数目，注意请输入100的倍数:")
    su9=0
    while True:
        money=int(input())
        if money%100==0:
            print("账户充值成功")
        else:
            print("数值格式输入错误!,请重新输入")
            continue
        su9+=money #累加
        repeat=str(input("would you need to 充值 again ?(yes(输入yes后，下一步直接输入需要充值的数目))/no)")) 
        if repeat=='no':
            print("你总共充值点卷:",su9)    #yes.bug
            break
    repeat2=str(input("would you like to let other people recharge ?(yes/no)"))
    if repeat2=='no':
        break
for name,password in confirm_users.items():
    print("\t账号:"+name+"\n密码:"+password[0:2]+"******"+"！")  #只输出代码的前俩位，后面都带*号
