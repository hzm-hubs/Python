# class bird(object): #父类 #class 定义了bird类，object为对象 在类中确定了属性并定义了函数，在之后进行调用
#     have_feather=True 
#     way_of_reproduction='egg'#少了引号会表示egg没有被定义
#     def move(self,dx,dy): #在定义方法时，必须有self这一参数。这个参数表示某个对象。对象拥有类的所有性质，那么我们可以通过self，调用类属性。
#      position=[0,0]
#      position[0]=position[0]+dx #position[0]指的是列表的第一个元素，position[1]同理
#      position[1]=position[1]+dy 
#      return position
# summer=bird()   #属性（attribute）#调用方法 建立对一个对象： 对象名 = 类名()
# # 引用对象的属性： object.attribute
# print(summer.way_of_reproduction) 
# print('after move:',summer.move(5,8))
# print('again move:',summer.move(7,6))
# class chicken(bird):#子类 子类与父类的声明方式：class 子类名(父类名):
#     way_of_move='walk' #一个父类能有多个子类
#     possible_in_kfc=True  #子类调用父类属性、方法时，在声明子父类关系后，对象=子类名（），然后对象.方法，当子类、父类中有相同的方法时,调用执行子类的方法
# class oriole(bird):#子类
#     way_of_move='fly'
#     possible_in_kfc=False
# class phoenix(bird):#子类
#     way_of_move='fly plus'
#     possible_in_kfc=False
#     appearance='so beautiful'
# class cock(phoenix):#子类的子类
#     way_of_move='walk2'
#     appearance='ordinary' #appearan(外观)
# qike=chicken() #建立调用关系
# print(qike.way_of_move) #调用方法并输出
# print(qike.move(9,3)) #通过对象可以修改类属性值。但这是危险的。类属性被所有同一类及其子类的对象共享。类属性值的改变会影响所有的对象。
# phoenix1=phoenix()
# print(phoenix1.way_of_move)
# print(phoenix1.appearance)
# cock1=cock()
# print(cock1.way_of_move)
# print(cock1.way_of_reproduction) #子1类的子类也可以调用子1类的父类中的方法
# #包含双下划线的函数
# class Dog():
#     def __init__(self,name,age):
#         #因为类中的每个属性都必须有初始值（这个值为0或空字符串都行）下面俩行是__init__内指定的初始值提供法
#         self.a=name  #self(自身)，当创建实例时，将自动传入实参self,self再自动传递，英雌我们只需要输入最后俩个形参(name和age)
#         self.b=age   #以self为前缀的变量都可供类中的所有方法使用，通过实例来访问这些变量，如在这里，self.a获取实参中的值并赋予给变量name。name,a,b也称为属性
#     def sit(self):    
#         print(self.a.title()+" is sitting now")
#     def roll_over(self):
#         print(self.a.title()+" had "+str(self.b)+" and rolled over!")#age前后都是str,str只能链接到str,所以这里把age从整型转化成了字符串类型
# huhu=Dog('旦旦','20') #实例化 
# print(huhu.a) #要访问实例的属性,可使用句点(.)表示法。如huhu.a
# print(huhu.b)
# huhu.sit()   #因为在自定义函数中加入了print方法加上这里又加入了print语句会导致在输出方法结果后的下一行输出None。
# huhu.roll_over()
# jijk=Dog('Koko','5')
# print(jijk.a)
# print(jijk.b)
# jijk.sit()
# jijk.roll_over()#可根据一个类创建任意数量的实例，前提是存储的变量不一样
#类3

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()#使long_name中的字符串都大写后返回
    def read_odometer(self):
        print("this car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage): # 第二种
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage  #此处进行了扩展，禁止将里程表里的数回拨
        else:
            print("you can't roll back an odometer!")
    def increment_odometer(self,miles): # 第三种
        self.odometer_reading+=miles

my_new_car=Car('Bwm','x7','2017')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#直接修改属性的值（第一种修改属性的方法）
my_new_car.odometer_reading=250 
my_new_car.read_odometer()

#第二种修改属性值的方法
my_new_car.update_odometer(23)
my_new_car.read_odometer()  #这种方法是在类里加入了一个更新函数update_odometer()

#第三种修改属性的方法
my_uesd_car=Car('subaru','outback',2013)
print(my_uesd_car.get_descriptive_name())
my_uesd_car.increment_odometer(100)#给属性传递特定的量
my_uesd_car.read_odometer()