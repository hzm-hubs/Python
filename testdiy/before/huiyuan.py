
confirmed_users=["聂启笛",'周帆'] # 已注册的列表集合，字符串用单引号 ' 或双引号 " 括起来
# 还需要解决相同元素同时出现的问题  ，如何将新加入的会员永久保存在列表里，或者在一定时间后自动删除，或加入新的判定列表 电话、性别 加油！！！！！！

while True:
    input_=str(input("请输入注册会员名:"))
    if (input_):
        if (confirmed_users.count(input_)):
            print("尊敬的%s已是我店会员，您可直接体验！" % (input_))
        else:
            # \t 不顶头输出，\n 换行输出,\end="" 使下一行输出跟着上一行 在这些前面加 r 可以阻止其生效
            # ok=int(input("立即注册请输入:YES,离开任意键"))
            if int(input("立即注册请输入1,退出按任意键:")) == 1:
                confirmed_users.append(input_)
                print("恭喜"+input_+"成为我店会员！！！")
            else:
                break
    input__=str(input("重新注册请输入YES，退出请按任意键"))
    if input__.upper()=='YES':  #upper()是全部变为大写，lower()全部变为小写  ，title()是首字母大写输出
        print('将继续执行')
        continue # 从头继续循环
    else:
        print("欢迎下次使用!")
        break  # 瑞出