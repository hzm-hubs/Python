# import huiyuan   #调用整个文件
# import huiyuan as h #通过给模块指定简短的别名，使调用函数中的模块更
# from 模块名(文件名) import * #通过星号可以调用模块中的全部函数
# from ZIdianJiayuYuansu import build_person,user_huk #调用文件中的一个、多个函数，函数之间用逗号隔开
# from ko import make_pizza as mp #用as（）函数给导入的函数指定一个简短或者特殊的符号，避免函数名称太长或者与程序中现有的函数名称冲突


# from Zilei import U12 #从子类文件中导入Car类，下面开始创建实例:
# my_second_car=U12('Benz','se200','2017')
# print(my_second_car.get_descriptive_name()) 
# my_second_car.odometer_reading=36
# my_second_car.read_odometer() #会发现是导入了整个子类模块中的类,需要在模块中重新在终端运行一次
#导入单个类
# from car import Car
# my_car=Car('bujiadi','pop','2018')
# print(my_car.get_descriptive_name())
# my_car.odometer_reading=80
# my_car.read_odometer()
# my_car.update_odometer(500)
# my_car.read_odometer()
#在一个类中存储多个类，用逗号分隔各个类
# from car import Car,ElectricCar
# myoicar=Car('lanbojini','max','2019')
# print(myoicar.get_descriptive_name())
# myoicar.fill_gas_talk()
# mytesla=ElectricCar('okl','tels','2018')
# print(mytesla.get_descriptive_name())
# mytesla.describe_battery()
#导入整个模块
# import car
#导入模块中的所有类
# from module_name import * #一般不推荐使用这种方法
#在一个模块中导入另一个模块
from car import Car
from electric_car import ElectricCar

my_car=Car('bujiadi','pop','2018')
print(my_car.get_descriptive_name())

mytesla=ElectricCar('okl','tels','2018')  #现在我们恶意通过这种方法从每个模块中导入自己需要的类
print(mytesla.get_descriptive_name())
