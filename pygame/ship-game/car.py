class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()#使long_name中的字符首字母都大写后返回，以空格划界
    def read_odometer(self):
        print("this car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage  #此处进行了扩展，禁止将里程表里的数回拨
        else:
            print("you can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
    def fill_gas_talk(self):
        print("this car has a 100L's gas tank")
class ElectricCar(Car):
    def __init__(self,make,model,year):#初始化父类的属性
        super().__init__(make,model,year)#super()为一特殊函数，帮助python将父类与子类联系起来
        self.battery_size=70 #给子类定义属性和方法以区分子类与父类、或者完善补足信息,
    def describe_battery(self): #在子类中定义函数，使用的变量需要先定义,定义在函数前面才能在之后进行函数属性的修改
        # self.battery_size=70 
        print("this car has a "+str(self.battery_size)+"-kwh battery.")
    def fill_gas_talk(self): #根据实例的世纪情况对父类中的方法进行重写，注意括号里的self不能省略，self对应一个位置参数
        print("this car doesn't need a gas tank!")
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