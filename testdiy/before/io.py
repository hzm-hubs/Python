# with open(r'C:\Users\46725\Desktop\pi_ko.txt') as lol:  #因为pi_ko.txt文本不在.vscode文件夹里，所以这里采用绝对文件路径，linux系统里用斜杠分隔上下级，
#     contents=lol.read()                          #windows系统使用反斜杠(\)分隔，但是反斜杠在python中被视为转义标记，所以采用在引号前加上r或者双斜杠分隔如左
#     print(contents)
# pass
# file_1='C:\\Users\\46725\\Desktop\\pi_ko.txt'
# with open(file_1) as file_1: #这里之所以会有多个分行符是因为在这个文件中每行的末尾都有一个看不见的换行服，其次print语句自带一个换行，可以像上面的函数
#     for line in file_1:      #采用rstrip()函数消除这些空白行
#         print(line)          #read()函数读取快简单，单文件过大时内存占用大，readline()函数速度较慢：逐行读取,readlines()函数野在在内存占用问题：一次性读取完所有内容，所以相比之下
#                          #for循环是最好的选择/try....finally....if与with open('')同样可以使用，

# file_2='C:\\Users\\46725\\Desktop\\pi_ko.txt' #将问文本列表存储到变量lines中在with代码外依然可以使用这个变量输出，可以在其他位置继续调用
# with open(file_2) as file_3:                  #由于lines的每个元素都对应文件中的每一行，因此输出与文件内容完全一致
#     lines=file_3.readlines()
# for line in lines:
#     print(line)

# try:
#     f=open(r'C:\Users\46725\Desktop\pi_ko.txt')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# # a={'-':1}                  
# # a['-']   #小插曲
# # print(a)  
# # print(type(a))
# pi_string=''  #在此处调用lines，先定义一个变量pi_rstring，接着使用一个循环将各行都加入pi_string通过rstrip()函数删除末尾的换行符
# pi_string1=''
# for line in lines:
#     pi_string+=line.rstrip() 
#     pi_string1+=line.strip() #通过strip()函数删除每行左边的空格，输出为一个前后无空格的字符串。
# print(pi_string)             #读取文本文件时，python将其中的所有文本都解读为字符串，如果读取的数字野作为字符串使用，入药作数值使用可以通过int()或float()函数
# print(len(pi_string))
# print(pi_string1)  #输出这个字符串长度                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
# print(len(pi_string1))
# bithday=''
# birthday=input('Enter your birthday,in the form mmddyy:')  #判断生日死否出现在了圆周率中
# if bithday in pi_string1:
#     print('your birthday appears in the first million digits of pi:!')
# else:
#     print('your bithday does not appear in the first million of pi:!')



# a='  a  dc   '
# b='123'
# print(a.rstrip()+b) #rstrip()函数删除每行字符串后面的换行符(空格))
# print(a+b)
# print(a.strip()+b) #strip()函数删除字符串前后的空格
# print(''.join(a.split())+b)#''.join(变量名.split())删除字符串中所有的空格
# print(a.replace(' ','')+b) #变量名.replace('c1','c2')把字符串中所有的c1都换成c2,删除字符串中所有的空格

# file_name2=r'C:\Users\46725\Desktop\oloming.txt'          #当文件不存在时，利用函数open()自动在.vscode文件夹下创建改名文件 
# with open(file_name2,'w') as kol:  #'w'写入模式，'r'读取模式，'a'附加模式,'r+'既能读取也能写入模式,如果省去了实参模式，python默认采用只读模式打开
#     kol.write("I love programming every moment!"+str(2)+"\n") #若指定文件已经存在，python会在每次返回文件对象前清空该文件,另外python只能将字符串存入文本中，若要存入数值数据需要使用函数str()转换
#     kol.write("I LOVE RIO & lol")  #write函数不会在你写入的文本末尾添加换行符，若要在文本中写入多行需要自己在字符串末尾加入换行符
# with open(file_name2,'a') as plo:  #附加模式，给文件在之前的基础上添加内容而不清空，同样若文件不存在或自动创建一个空文件
#     plo.write("\n哇社会是真的险恶！") #利用绝对文件路径在想要的位置添加文本文件
#     plo.write("烦")

#try''''except代码块
# print(5/0) #这里显示是一个异常对象，无法创建对象，就会停止程序；可以采用try....except代码块，即便程序出现异常也会继续运行，兵可以显示你编写的错误提示信息
# try:
#     print(5/0)   #代码没有问题程序将跳过except代码块;若有问题,将运行except
# except:
#     print('you can not divide by zero!') #友好提示0不能被当作除数
#处理ZEROdivisionerror异常
# print("Give me two numbers,and I will divide them!")
# print("Enter 'q' to quit")
# while True:
#     first_number = input("\nFirst number:")
#     if first_number=='q':
#         break
#     second_number=input("\nsecond number:")  #输入的数也可能是0，会导致程序出错停止，所以在这里加入try  except代码块，完善程序
#     try:
#         answer=int(first_number)/int(second_number)
#     except:                          #try except else 组成一个健全的代码组
#         print('you can not divide by zero!')
#     else:
#         print(answer)

#处理Filenotfounderror异常
# filename='alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents=f_obj.read()
# except :
#     msg="Sorry,the file"+filename+" does not exist."
#     print(msg)

#分析文本
# file_name='C:\\Users\\46725\\Desktop\\kom.txt' #对应文本文件
# try:
#     with open(file_name) as plp:
#         contents=plp.read() #读取文本文件兵存储在变量contents中
# except FileNotFoundError:  #代码块中的代码导致了错误，python将查找这样的except代码块，并运行其中的代码
#     msg="Sorry,the file "+file_name+" does not exist."   #若try就不会执行exceptdai
#     print(msg)
# else:           #依赖于try代码块执行成功的代码都应该放到else代码块中，意味这try语句成功就会调起后面的else语句
#     words=contents.split()  #以空格为标志将字符串分隔成列表里的元素
#     num_words=len(words)    #统计列表的长度
#     print("the file "+file_name+" has about:"+str(num_words)+" words")

#查询多个文件，定义成函数
# def count_words(filename1):
#     try:
#         with open(filename1) as jui:
#             contents=jui.read()
#     except FileNotFoundError:
#         msg="Sorry,the file "+filename1+" does not exist." 
#         print(msg)
#         #pass #要程序在失败时无响应，可把except代码块中的语句换为pass，这样就不会出现traceback，且pass充当了占位符
#     else: 
#         """计算文件中多少个单词"""
#         words=contents.split()  #以空格为标志将字符串分隔成列表里的元素
#         num_words=len(words)    #统计列表的长度
#         print("the file "+filename1+" has about:"+str(num_words)+" words.") 
# filename=r'C:\Users\46725\Desktop\oloming.txt'  #注意绝对文件路径，因Desktop输入错误耽搁了半小时
# count_words(filename)
# filename=r'C:\Users\46725\Desktop\kom.txt'
# count_words(filename)
# file_lists=['po.txt','C:\\Users\\46725\\Desktop\\loki.txt','oloming.txt','C:\\Users\\46725\\Desktop\\kom.txt'] #s使用FOR循环分别计算各个列表中的单词
# for file_list in file_lists:              #注意中文可能识别不来
#     count_words(file_list)          #在for循环里调用自定义函数，逐个执行，

#使用模块json来存储数据,一边程序下次运行时加载该文件，此外json还可以用来在python程序之间分享数据。JOSN数据格式还能与使用编程语言的人分享使用
# import json #因为json为python内函数,所以先导入json模块
# numbers = ['2','8','9','3','8']  #给定要存储的数字列表
# filename='numbers.json'       #指定要接受数据的文件名称,并指定属性为JOSN数据格式
# with open(filename,'w') as lo:  #以写入模式打开该文件
#     json.dump(numbers,lo)  #使用json.jump()将数字列表写入到文件中，不过没有输出出来，因为没有输出语句，可以在相对文件夹下找到该文件
# """json.dump()函数用于存储，json.load()用于读取"""
# filename='numbers.json' 
# with open(filename) as los: #指定要打开的文件夹
#     p=json.load(los)  #使用json.load函数读取该文件，将读取的数据赋予给变量p
# print(p)  #输出p

#保存和读取用户生成的数据
# import json   #使用json保存大有好处，如果不以某种形式存储，等程序停止时用户的信息将会丢失
# usename=input('请输入你的名字:') #输入中文存储到文本文件中，打开会显示乱码，
# filename='usersname.json'  #寻找当前文件夹下是否有文件名称为usersname属性为json的
# with open(filename,'w') as opo: #当该文件不存在时自动创建一个，进入写入模式
#     json.dump(usename,opo) ''' json.dump()函数内，前者为要写入文件的数据，后者为写入的文件的名称'''
#     print('我记住你了， '+usename)
# with open('usersname.json') as uio: #打开该文件
#     o=json.load(uio)  #读取文件数据赋值给变量o
# print(o+'  welcome back!') #输出

'''升级版'''
# import json
# filename='C:\\Users\\46725\\Desktop\\如今.json'  #注意绝对文件路径不要再再写错了 ，在桌面寻找名为如今的文件
# try:
#     with open('C:\\Users\\46725\\Desktop\\如今.json') as qwer: 
#         o=json.load(qwer)          #若存在就读取
# except FileNotFoundError:
#     usename=input("Please enter your name:")  #提示输入名字
#     with open(filename,'a') as pola:  #不存在引发except语句，在之前的路径下创建一个名字相同的的文件，以附加模式打开
#         json.dump(usename,pola)   #写入数据
#         print("Expect your next use, respect "+usename)
# else:
#     print("welcome back "+o+' !') #重新打开运行程序，文件存在，try语句执行正确，执行try....else代码块

#重构:代码能够正确运行，但可做进一步的改进——将代码划分为一系列完成具体工作的函数。重构用于让代码更清晰、更易于理解、更利于扩展
# import json
# filenamae='C:\\Users\\46725\\Desktop\\56.json'
# def no_1(): #先定义一个函数，该函数只负责获取文件中的用户名
#     try:
#         with open(filenamae) as t:
#             p=json.load(t)
#     except FileNotFoundError:
#         return None
#     else:
#         return p
# def no_2():
#     usename=input('请输入你的名字:') #此次定义的函数只负责获取并存储新用户的用户名
#     with open(filenamae,'w') as oq:
#         json.dump(usename,oq)
#     return usename
# def no_3():  #负责调用前面的俩类函数不是欢迎就是问候新用户
#     username=no_1()
#     if username:
#         print("welcome back "+username+' !')
#     else:
#         username=no_2()
#         print("when you come back ,I must kown you "+username+' .')
# no_3()  #调用函数3 

#测试函数
import unittest
def get_formatted_name(first,last,middle=''):
    '''创造一个完整格式的全名'''
    if middle:
        full_name=first+' '+middle+' '+last 
    else:
        full_name=first+' '+last
    return full_name.title()
# print("Enter 'q' at any time to quit")
# while True:
#     first=input("\n please give me your first name:")
#     if first=='q':
#         break
#     last=input("give me your last name:")
#     if last=='q':
#         break
#     fomatted_name=get_formatted_name(first,last)
#     print("\t Neatly formatted name:"+fomatted_name+'.')
class namestestcase(unittest.TestCase):   #unittest测试函数
    def test_first_last_name(self):  #所有以test打头的方法都将自动运行
        fomatted_name=get_formatted_name('janis','joplin')  #调用之前创建的方法
        self.assertEqual(fomatted_name,'Janis Joplin') #断言方法，用来判断括号里的俩者是否相等
    def test_first_last_middle_name(self):
        fomatted_name=get_formatted_name('dso','fefe','polq')
        self.assertEqual(fomatted_name,'Dso Polq Fefe')
unittest.main()  #让代码运行这个测试
#测试未通过时应该怎么办 #在上式加入可判断的middle语句
