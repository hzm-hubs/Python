# msg="hello word"
# print(msg)
# a,b=4,8
# c=a+b 
# c1=a*c
# c2=b/a
# print("c={}\nc1={}\nc2={}".format(c,c1,c2))
# h=(a+b)*b/6
# print(a,h)
# o='wyhdmzswlp'
# print(o)
# print(o[0:2])
# print(o[5:6])
# print(o[-3])
# print(o[-1: ])
# list=['VN',322,584,'LeeSin','lejiasi',9.632]#列表
# bulist=['EZ','Zed',567]
# print (list+bulist)
# print  (list[3:5])
# print  (list*3+bulist*2)
# koouo=('jioij',528,2.30,'huyg')#元组
# rti={}
# rti['one']="this is one"
# rti[2]="this is two"
# ioj={'name':'LeeSin','damage':'4396','kill':'12','assisant':'6','death':'0'}#字典
# print(rti)
# print(rti[2])
# print(ioj.keys())
# print(ioj.values())
# str(5)
# print(5)
# j=5+7
# print(j)
# g,i,v=9,4,9.2
# print(g-i,g/i,g%i,g**i,g//i,g/v) # %是取余数，//是整数除，a**b结果为a的b次幂
# if v-1>i:
#     print("v是大于i的")
# else:
#     print("v小于等于i的")
# # if (a in rti：
# #     print("a在字典rti里面")
# print (int('100101',2))
# print(bin(4535351354))
# print(oct(653))
# a=0
# g=60
# i=13
# c=0
# a=g&i
# print(bin(a))
# if (g and i):
#  print("g与i都不为0")
# else:
#  print("俩者中至少有一个不为true") #可以用于判断用户是否完成任务的俩个以上要求
# if (g or i):
#  print("恭喜您已经完成任务")
# else:
#  print("您还没有完成俩个任务中的任何一个") # 用于任务二选一完成
# if not (a and c):
#     print("俩这中至少有一个为0")
# else:
#     print("俩者都为0")
# if (g and i and c):
#     print("三者中没有一个为0")  #三选任务
# else:
#     print("三者中至少有一个为0")
# a=20
# b=20
# c=15
# if(a is b):
#    print("a和b具有相同的标识")  
# else:
#    print("俩者不等")   
# if(a is not c):
#    print("a与b没有相同的标识")
# else:
#    print("俩者相等")
# num=9
# if num==3:
#     print('boss')
# elif num==2:
#     print('user')
# elif num==1:
#     print("worker")
# elif num<0:
#     print('error')
# else:
#     print('roadman')
# oio=3
# if oio>=5 and oio<=9:
#     print("you'are welcome!!!")
# else:
#     print("error")  
#     print("请重新输入")
# numbers=[56,45,52,33,51,23,1]
# even=[]
# odd=[]
# print(len(numbers))
# while len(numbers)>0:
#  number=numbers.pop() #移除列表中的一个元素，并返回该元素的值，默认从最后一个元素开始
#  if(number % 3 ==0):
#   even.append(number)
#  else:
#   odd.append(number)
# # print("列表even为:",even) , print(odd)#函数语句之间可以用+号，变量用逗号
# i=1
# while i<10:
#     i+=1
#     if i%2>0: #通过相同的缩进表示同意循环
#         continue #对齐格式很重要
#     print(i)
# i=1
# while 1:
#   print(i)
#   i+=1
#   if i>6:#
#    break 
# sum10=5
# k=0
# while k<5:
#    sum10+=k  #中英文输入
#    k+=1
#    print(k)
# else:
#    print(sum10)
# kill=1
# while 1:print("given my heart to you!") #当while后面的判断之为true时程序会进入无限循环，可用ctrl+c中断
# print("Good bye!")
# for letter in 'take myheart': #注意意外缩进
#      print("当前字母:",letter)
# hero_lols=['EZ','Leesin','VN','Yasuo','Zed']
# for hero_lol in hero_lols:
#     print("当前英雄有:",hero_lol),     print('加油') #一行若有俩个print，之间需要加入逗号(',')
# for i in range(1,9): #range()函数用于指定变量范围，如此时为1到9，但只可以从1取到8
#     print(i)
# for num in range(10,20):
#     for i in range(2,num):
#         if num%i==0:
#          j=num/i
#          print('%d等于 %d*%d'%(num,i,j))
#          break #跳出循环
#     else:
#          print ("%d是一个质数！"%(num)) #注意语句之间的搭配，在这里else是与第二个for形成循环，不是与与他离得近的if，所以else应该与第二个for对齐
# i=2
# while (i<100):
#     j=2
#     while(j<=(i/j)):
#         if not(i%j):  break
#         j=j+1 #if的下一行语句应与其缩进相同
#     if (j>i/j): print(i,'是素数') #continue 语句跳出本次循环，而break跳出整个循环，
#     i+=1 #continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。continue语句用在while和for循环中
# print("good bye!") #python中的pass语句用作站位
# a=51
# print(a)
# pass
# pass
# print(a)#del语句用于删除一些number对象引用
# del a
# print(a)#此时会显示a没有被定义
# x=96.321
# print(x.__int__())#取整数部分，若要得到96.0，可以采用整数除1的方法
# farvorite_foods={'green pepper':'6','red pepper':'9','totatoes':'789'}
# for name in sorted(farvorite_foods.keys()):
#   print(name.title()+", thank you for takeing the poll") 
# print('dhudhdhfddshdhdhdknvud')

# i=1
# if i>0:
#     print('positive i',end="") #是与下面的输出语句之间不换行
#     i=i+1
#     if i>1:
#         print('加油')
# elif i==0:
#     print('i is 0')
#     i=i*10
# else:
#     print('negative i')
#     i=i-1
# print('new i:',i)

# for i in range(9):#默认是从0开始
#     if i==2:
#         continue
#     print(i,end="")
#     if i==7:
#         break
#     print(i,end=" ")
# passmap
# print()
# wyh=52 
# while wyh<60:
#     print(wyh,end=" ") #end=""是不换行，"\n"是换行的。
#     wyh+=1
# def  yuhj(year,month,day):
#     hui=['1998,2,6','2000,2,5','2004,4,9','2018,4,5']
#     map(yuhj,hui)
#     if month==2 and day==29 :
#         return True
#         print('lead year')
#     elif (year%4==0 and year%100!=0) or year%400==0:
#         return True
#     else:
#         return False 
   
# import datetime
# nowtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print('北京时间:',nowtime)
#类
class Dog():
    def __init__(self,name,age):
        self.a=name  #self(自身)，当创建实例时，将自动传入实参self,self再自动传递，英雌我们只需要输入最后俩个形参(name和age)
        self.b=age   #以self为前缀的变量都可供类中的所有方法使用，通过实例来访问这些变量，如在这里，self.a获取实参中的值并赋予给变量name。name,a,b也称为属性
    def sit(self):    
        print(self.a.title()+" is sitting now")
    def roll_over(self):
        print(self.a.title()+" had "+str(self.b)+" and rolled over!")#age前后都是str,str只能链接到str,所以这里把age从整型转化成了字符串类型
huhu=Dog('旦旦','20') #实例化 
print(huhu.a) #要访问实例的属性,可使用句点(.)表示法。如huhu.a
print(huhu.b)
huhu.sit()   #因为在自定义函数中加入了print方法加上这里又加入了print语句会导致在输出方法结果后的下一行输出None。
huhu.roll_over()
jijk=Dog('Koko','5')
print(jijk.a)
print(jijk.b)
jijk.sit()
jijk.roll_over()#可根据一个类创建任意数量的实例，前提是存储的变量不一样
