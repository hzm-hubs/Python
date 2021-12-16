from car import Car #电动汽车类需要访问其父类，所以在这里导入了Car类  书158页
class Battery():
    def __init__(self,battery_size=100): #定义的一个新类，没有继承任何属性
        self.battery_size=battery_size
    def describe_batteryo(self):
        print("this car has a "+str(self.battery_size)+" -kwh battery.")
    def get_rang(self):
        if self.battery_size==100:
            range=240
        elif self.battery_size==85:
            range=270
        message="this car can go approximately "+str(range)
        message+=" miles on a full charge." #将类继续扩展提示续航能力
        print(message)
class ElectricCar(Car):
    def __init__(self,make,model,year):#初始化父类的属性
        super().__init__(make,model,year)#super()为一特殊函数，帮助python将父类与子类联系起来
        self.battery_size=70 #给子类定义属性和方法以区分子类与父类、或者完善补足信息,
    def describe_battery(self): #在子类中定义函数，使用的变量需要先定义,定义在函数前面才能在之后进行函数属性的修改
        # self.battery_size=70 
        print("this car has a "+str(self.battery_size)+"-kwh battery.")
    def fill_gas_talk(self): #根据实例的世纪情况对父类中的方法进行重写，注意括号里的self不能省略，self对应一个位置参数
        print("this car doesn't need a gas tank!")