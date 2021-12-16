confirmed_users=["聂启笛",'周帆']
 # 还需要解决相同元素同时出现的问题  ，如何将新加入的会员永久保存在列表里，或者在一定时间后自动删除，或加入新的判定列表 电话、性别 加油！！！！！！
unconfirmed_users=str(input("请输入注册会员名:"))
print("verifying user:"+unconfirmed_users)
confirmed_users.append(unconfirmed_users)
print("恭喜"+unconfirmed_users+"成为我店会员！！！")
while True: 
    for confirmed_user in confirmed_users:
        print("现在我店会员有:"+confirmed_user)
    check_user=str(input("请输入需要查询的会员名:"))
    if check_user in confirmed_users:
        print("尊敬的"+check_user+"是我店会员，欢迎体验！")
    else:
        print("该用户尚未成为我店会员，是否需要立即注册！") #\t 不顶头输出，\n 换行输出,\end=""使下一行输出跟着上一行 在这些前面加r可以阻止其生效
        print("立即注册请输入:666,离开输入:555")
        ok=int(input())
        if ok ==666:
            unconfirmed_users=str(input("请输入注册会员名:"))
            print("verifying user:"+unconfirmed_users)
            confirmed_users.append(unconfirmed_users)
            print("恭喜"+unconfirmed_users+"成为我店会员！！！")
        elif ok==555:
            print("欢迎下次光临!")
        print("若需要继续使用请输入YES，退出请按任意键")
        ji=str(input())
    if ji.upper()=='YES':  #upper()是全部变为大写，lower()全部变为小写  ，title()是首字母大写输出
        print('将继续执行')
        continue
    else:
        print("欢迎下次使用!")
        break  