# ho=[44,55,66]
# i=
# while (i<3):
#     ho[i]+=100
#     i+=1
# print(ho)
# def add100(x):
#     return x+100
# hh = [22,33,44]
# map(add100,hh)
# print(list(map(add100,hh)))#丢人了哦 py2 print map(add100,hh)  py3 print(list(map(add100,hh)))
# def abc(a,b,c):
#     return a*1000+b*100+c
# list1=[11,22,33]
# list2=[44,55,66]
# list3=[77,88,99]
# map(abc,list1,list2,list3)
# print(list(map(abc,list1,list2,list3))) #
# def aui(s,o):
#     return s*
# list2=[88,77]
# map(aui,list1,list2)
# print(list(map(aui,list1,list2)))
# """difdidvkdvndvdnvhusngjkwbhghushugfiiicmrughr""" #另一种注释
# print("j")
# '''print(fijj)'''  #一种注
# print("iji")
# total=['gef','gdf','dff','dfbd','nnn'] #列表过长需要多行输入时，不能以逗号为断行点
# print(1+2.2j) #这是带括号输出
# print('i+2.2j')#不带括号输出
# print("1+2.2j")
# print("wyh\nssb")
# print(r"wyh\nssb")
# iuo='kokoj'
# print(iuo[0:4])
# print(iuo[-2])
# print(iuo[::-1])#从右往左取完
# print(iuo[-1::-3])
# print(iuo[-1::]) #等价于去右边第一个
# print(iuo[1:4])
# print(iuo[1:4:3])
# print(iuo[-3::-2])
# input("\n按下 enter 键后输出")
# x=input("x:")
# y=input("y:")
# print(x)
# print(y)
# import sys
# x="huh"
# print(sys.stdout.write(x+' '+'\n')) #函数在输出x的同时也会输出write（）里的字符串长度包括换行符、空格符，若有换行符则在下一行输出，没有就紧贴x后面输出
# hu='5959lolhfg'
# print(hu[0:6:2]) #一般格式为下限：上限：步长（每隔多远取一个）
# print(hu[:-2])#从左到右输出到倒数第三个为止
# print(hu[0:-1])#输出到倒数第二个
# print(hu[2:0:-1]) 
# print(hu[0:2])
# print(hu[::-1])#从右到左全部输出
# print(hu[-2:-1])
# print(hu[-1::])
# print(3**2) 
# print('3**2')  
# def jii(year):
#     a=year%4==0 and year%100!=0 or year%400==0 
#     return a
# list1=[2014,2008,2061,2000]
# map(jii,list1) 
# print(map(jii,list1))
# lisus=[2004,2000,1997,2014,2003]
# for lisu in lisus:
#     if lisu%4==0 and lisu%100!=0:
#         print(lisu,"年为普通闰年") 
#     elif lisu%400==0:
#         print(lisu,"年为世纪闰年")
#     else:
#         print(lisu,"年为普通年份，不属于闰年")
# import getpass
# pwd=getpass.getpass("请输入密码:")  #getpass可实行不可见功能
# print(pwd)
#
# lisu1=input("请输入所需判断的年份:")
# print(lisu1)
# lisu1=int(lisu1)
# lisus=[2006,2014]
# lisus.insert(0,lisu1)
# for lisu in lisus:
#  if lisu%4==0 and lisu%100!=0:
#     print(lisu,"年为普通闰年") 
#  elif lisu%400==0:
#     print(lisu,"年为世纪闰年")
#  else:
#     print(lisu,"年为普通年份，不属于闰年")#判断用户输入的年份是否为闰年！

# 内置的complex（变量，认为的变量类型）函数可以用来判断变量所指的对象类型  若是返回true 不是返回false

# sh=['Beijing',' the north of china',(2018,7,13)]
# name,location,(year,month,day)=sh
# print(name,"\n",location,"and now time is",(year,month,day))
# class bird():
#     have_feather=True
#     way_of_reproduction='egg'
# class min():

#     uiu=bird()
#     print(uiu.have_feather)
# cun=2
# while cun<=6:
#     print(cun)
#     cun+=1
# print("最终cun的值为:",cun)
# promt="\nJust give me something,I will repeat it back to you!"
# promt+="\nIf you don't want to repeat back ,you input 'quit' plesae:"
# message=""
# while message != 'quit': 
#     message=str(input(promt))
    
#     if message !='quit':
#         print(message)
# active=True
# while active:
#   message=input(promt)
#   if message==quit:
#       active=False
#   else:
#       print(message)
 
# while True:
#     city=input(promt)
#     if city == 'quit':
#         break
#     else:
#         print("This is a beautiful"+city.title()+"!")
# OPPO="\n 你去哪些地方旅游过:"
# city=str(input(OPPO))
# while True:
#     if city=='beijin':
#        print("it is so beantiful!")
#        break
#     else:
#        print("oh!I don't go to there")
#        break
# unconfirmed_users=['alice','brain','candace']
# confirmed_users=[]
# while unconfirmed_users:
#     current_users=unconfirmed_users.pop()
#     print("verifying users:"+current_users.title()) #\t不排头输出
#     confirmed_users.append(current_users)
# print("\n the followiing users have been confirmed:")
# for confirmed_users in confirmed_users:
#     print(confirmed_users.title())
# confirmed_users=['聂启笛','周帆']
# unconfirmed_users=str(input("请输入注册会员名:"))
# print("verifying user:"+unconfirmed_users)
# confirmed_users.append(unconfirmed_users)
# print("恭喜"+unconfirmed_users+"成为我店会员！！！")
# for confirmed_user in confirmed_users:
#     print("现在我店会员有:"+confirmed_user)
# check_user=str(input("请输入需要查询的会员名:"))
# if check_user in confirmed_users:
#     print("尊敬的"+check_user+"是我店会员，欢迎体验！")
# pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat') #remove(),用来删除列表中的特殊值，但运行一次只能删除一次，所以在这里借助while循环直至将列表中的cat全部删除完。
# print(pets)   #注意cat俩边的'不能少，'cat'表示列表pets里的，而cat则是在外部，且在外部没有cat的定义，会报错
# responses={}  #先定义一个字典
# polling_active=True
# while polling_active:
#     name=str(input("\n请输入你的名字:"))
#     response=str(input("which mountain would you like to climb someday?"))
#     responses[name]=response   #建立键值对关系，前面的表示键，后面的respons表示值
#     repeat = str(input("would you like to let another person respond?(yes/no)"))
#     if repeat=='no': #注意no俩边的'号,没有会显示no没有被定义
#         polling_active=False
#     print("\n---poll results ---")  #poll results 表示
#     for name ,response in responses.items():  #这里的逗号，表示name，response都要参加下面的循环，.items()把字典，用以列表返回可遍历的(键，值)元组数组，与字典搭配使用
#         print(name+"would like to climb "+response+".")

# def greet_users(username):
#     print("Come on,"+username.title()+"!") #此时username为形参(函数完成其工作时所需的一项信息，较抽象，也就是变量),"srars"为实参(调用函数时传递给函数的信息,就是对象，是具体的值)，函数运行时，将实参存储于形参中
# # srars=str(input("请输入你的名字"))
# greet_users("srars") #括号里的引号使srars成为字符串，没有引号会显示srars没有被定义。不用引号，可以像上一行注释定义一个从键盘端输入的字符串，
# def greeting(a,b):
#     print(a*b)
# greeting(3,1) #自定义函数
#下面的函数为关键字实参例子，调用函数时可以不顾实参的先后顺序输入
# def describe_pet(animal_type,pet_name="王钰涵"):                 
#     print("I have a "+animal_type.title()+".")                
#     print("My "+animal_type.title()+"'s name is "+pet_name+".")
# # describe_pet(pet_name='王钰涵',animal_type='girlfriend') #中英文格式很重要！！！！，这里因为逗号耽搁了半小时
# describe_pet("girlfriend") #这里采用了默认值，在定义时赋予了动物名初值，在调用时没有赋予其值，默认使用该形参的默认值
# describe_pet(pet_name="猪婆",animal_type="wife")
#下方代码为return函数应用 可用来存储姓和名，在定义函数时还能多加入几个信息，middle_name
# def get_formatted_name(last_name,first_name='黄'):
#     full_name=first_name+"-"+last_name
#     return full_name.title() #首字母都打写
# # number1=get_formatted_name('艾玛','斯通')
# # print(number1)
# # print(get_formatted_name('marry','lina'))
# print(get_formatted_name('泽民')) #注意非默认参数不能跟随默认参数，也就是定义了默认参数，后面的简化输入顺序应对应非默认参数
#在自定义函数中加入if判断语句
# def huji_name(first_name,last_name,middlr_name=" "): #默认middlr_name为空字符串，当判断时，若没有传递middle_name实参，采用默认的空值，if判定为false，执行else语句，若有实参，将替掉默认值，if判定为true，执行第一条语句
#     if middlr_name:
#         huji_name1=first_name+' '+middlr_name+' '+last_name
#         return huji_name1.title()
#     else:
#         huji_name1=first_name+''+last_name
#         return huji_name1.title()
# print(huji_name('uio','hu'))
# print(huji_name('sds','jij','dsd'))
#以键值的方式返回
# def build_person(first_name,last_name,age=' ',sex=' '):
#     ol={'first':first_name,'last':last_name}
#     if age:
#         ol['age']=age #在列表中新加入一个可选形参age,如果函数调用这个形参，其值就会存入到字典中
#     # return ol  如果这里返回了后面的if语句就直接跳过了，导致后面的语句直接失效
#     if sex:
#         ol['sex']=sex #如果要重现加入多个形参，retrun语句要放在最后
#     return ol
# print(build_person('黄','泽民','20','man')) #以字典的形式输出
# class bird(object):  #class 定义了bird类，object为对象 在类中确定了属性并定义了函数，在之后进行调用
#     have_feather=True 
#     way_of_reproduction='egg'#少了引号会表示egg没有被定义
#     def move(self,dx,dy):
#      position=[0,0]
#      position[0]=position[0]+dx #position[0]指的是列表的第一个元素，position[1]同理
#      position[1]=position[1]+dy 
#      return position
# summer=bird()   #属性（attribute）#调用方法 建立对一个对象： 对象名 = 类名()
# # 引用对象的属性： object.attribute
# print(summer.way_of_reproduction) 
# print('after move:',summer.move(5,8))
# print('again move:',summer.move(7,6))
# class chicken(bird):
#     way_of_reproduction='walk'
#     possible_in_kfc=True
# class oriole(bird):
#     way_of_reproduction='fly'
#     possible_in_kfc=False
# qike=chicken()
# print(qike.way_of_reproduction)
# print(qike.move(9,3))
# def greet_users(names):
#     for name in names:
#      msg="hello,"+name.title()+"!"
#      print(msg)
# usernames=['huu','sds','sdd']
# greet_users(usernames)
# def print_models(unprinted_designs,completed_models):
#     while unprinted_designs:
#         current_design=unprinted_designs.pop()
#         print("printing_name:"+current_design)
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     print("\n\tthe following models have been printed:")#换行和不顶头可以同时使用
#     for completed_model in completed_models:
#          print(completed_model)
# unprinted_designs=['sdis','fuff','fgfyf','ffga','iuohh']
# completed_models=[]
# print_models(unprinted_designs[:],completed_models) #这里的unprinted_desgins[:]表示使用的是unprinted_desgins的副本，这样做的好处是，保留原来列表里的元素，不会使其成为空列表，之后可以继续使用
# show_completed_models(completed_models)
# print(unprinted_designs)#unprinted_desgins中的元素没有被删除
def make_pizza(size,*toppings):#*toppings表示的是一个名为toppings的空元组，会把所有收到的值(不管实参有多少个)都存入这个元组中
    print('\nmaking a '+str(size)+' pizza with the following toppings:') #因为str只能连接到str，元组中的为整数型，所以在size前加入了类型转换
    for topping in toppings:  
        print("-"+topping)
make_pizza(20,'greenpappers','totatoes','extra cheese','redpappers')
make_pizza(16,'pop','dhu')  #此外，如果函数要接受不同类型的实参，必须在函数定义中将接纳任意数量的实参放在最后，先位置实参和关键字实参，在将余下的实参都收集到最后一个形参中。
b=2
print(b**3) #双*号表示次方运算 后边的3表示是3次方 如果是4就是4次方
a=5 
b=4
a+=b#a+=b  ==  a=a+b
print(a)
print('a')
print(b)
