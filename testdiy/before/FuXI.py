n1=['2','4','5','6','4']
# print(dir(n1))#dir()函数用来查询一个类或者对象所有属性
# print(help(n1))#用来查询的说明文档
print(n1.count('4')) #count(),计数函数，在此统计列表中共有多少个4
print(n1.index('5'))#index(),查询函数，在此查询列表中第一个5的下标
n1.append('7')#append(),末添加函数，在此是在列表的最后添加一个元素7
print(n1)
#sort(),永久性排序函数，在此将列表中的元素按从大到小排序
n1.sort()
print(n1)
print(n1.pop())#pop(),末删除函数,在此删除列表中最后一个函数
n1.remove('2') #remove(),移除函数，在此移除列表中的第一个2
print(n1)
n1.insert(0,'9')#insert(),指定添加函数(),在此是在列表中的首位添加一个9
print(n1)
运算符
n2=[5,4,3]
n3=[9,7]
print(n2+n3)# 是在第一个列表的后面加入第二个列表中的元素
#列表之间的减法函数，减法后的结果（被减列表除去俩个列表中共同含有的元素后的列表，不管俩个列表之间的长度差异，只与俩者的共同元素有关)
class superlist(list):
    def _sub_(self,h,l):#self 参数是必须的，
        a=h[:]
        x=l[:]
        while len(l)>0:
            element_b=x.pop()
            if element_b in a:
                a.remove(element_b)
                return a
c=superlist() #类实例化
# v=[1,2,3]
# f=[3,5]
print(c._sub_([1,2,3],[3,5,8,9,4]))#调用方法并输出
