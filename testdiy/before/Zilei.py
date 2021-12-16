class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()  # 使long_name中的字符串都大写后返回

    def read_odometer(self):
        print("this car has"+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage  # 此处进行了扩展，禁止将里程表里的数回拨
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_talk(self):
        print("this car has a 100L's gas tank")
# 创建子类时，父类必须包含在当前文件夹，且位于子类前面


class ElectricCar(Car):
    def __init__(self, make, model, year):  # 初始化父类的属性
        super().__init__(make, model, year)  # super()为一特殊函数，帮助python将父类与子类联系起来
        self.battery_size = 70  # 给子类定义属性和方法以区分子类与父类、或者完善补足信息,

    def describe_battery(self):  # 在子类中定义函数，使用的变量需要先定义,定义在函数前面才能在之后进行函数属性的修改
        # self.battery_size=70
        print("this car has a "+str(self.battery_size)+"-kwh battery.")

    def fill_gas_talk(self):  # 根据实例的世纪情况对父类中的方法进行重写，注意括号里的self不能省略，self对应一个位置参数
        print("this car doesn't need a gas tank!")
# my_tesla=ElectricCar('tesla','model s',2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery_size=80
# my_tesla.describe_battery()
# my_tesla.fill_gas_talk()
# my_tesla.update_odometer(2500)
# my_tesla.read_odometer()  #对于特殊的双下滑线函数，需要先出事化父类属性，在连接。而对于一般的函数在实例化后可以用句点调用法
# 或者你也可以想这样创建子类：
# class Tcar(Car):
#     my_tesl=Car('audi','a6',2016)
#     print(my_tesl.get_descriptive_name())
#     my_tesl.update_odometer(240)
#     my_tesl.read_odometer()
#     my_tesl.fill_gas_talk()
# 给子类定义属性和方法以区分子类与父类、或者完善补足信息
    #     # self.battery_size=70
    # def describe_battery(self):
    #     print("this car has a"+str(self.battery_size))+"-kwh battery."
    # my_tesl.describe_battery()


class Battery():
    def __init__(self, battery_size=100):  # 定义的一个新类，没有继承任何属性
        self.battery_size = battery_size

    def describe_batteryo(self):
        print("this car has a "+str(self.battery_size)+" -kwh battery.")

    def get_rang(self):
        if self.battery_size == 100:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "this car can go approximately "+str(range)
        message += " miles on a full charge."  # 将类继续扩展提示续航能力
        print(message)


class U12(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # 将一个大类拆分成多个协同工作的小类
        # 将实例用作属性 ，将一个Battery实例用作ElectricCar类的一个属性，在此处添加了self.battery属性,将实例存储在其中，每当__init__
        self.battery = Battery()
        # 被调用时，都将执行该操作，因此现在每个ElectricCar()实例都包含一个自动创建的Battery实例
# my_okoj=U12('ta','find x','2018') #实例名=类名（对象）
# print(my_okoj.get_descriptive_name())
# my_okoj.battery.describe_batteryo()
# my_okoj.battery.get_rang()
