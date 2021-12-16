# __init__()是一个特殊方法(special method)。Python有一些特殊方法。Python会特殊的对待它们。特殊方法的特点是名字前后各有两个下划线。
# 如果你在类中定义了__init__()这个方法，self一般都会需要，创建对象时，Python会自动调用这个方法。这个过程也叫初始化
class human(object):
    print("接收数据"+str(object))

    def __init__(self, wangyuhan):
        self.gend = wangyuhan  # 看不太懂啊！

    def printGender(self):
        print(self.gend)


li_lei = human('shazi')
# print(li_lei.gend) #只需要第一个自定义函数就能输出'shazi',通过双下划线自动调动的方法，self为对象，wangyuhan为变量，在类实例化后，将'shazi'赋值给变量，li_lei.gend会自动调用_init_中的方法，收获wanyuhan中存储的值
li_lei.printGender()  # 需要使用俩个自定义函数，在类实例化后，先通过第一个函数获取赋值，再通过第二个函数，调用其方法实现输出。
# 总的来说双下滑线函数，比普通函数来得简单，省事，
