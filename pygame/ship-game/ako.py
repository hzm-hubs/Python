class AnonymousSurvey():
    def __init__(self,question):  #在调用该类时自动也就调用__init__函数，通过实参向AnonymousSurvey类传递question,self可以自动传递,当下次利用该类创建实例时
        self.question=question     #只需要提供后面呢一个形参question,如第14排的AnonymousSurvey(question) ；self.question=question 以self为前缀的变
        self.responses=[]          #量都可供整个类的中的所有方法使用，可以通过类的任何实例来访问这些变量，获取形参self.name中的值再付给实参name，然后可以被创建
    def show_question(self):       #的实例访问 
        print(self.question)
    def store_response(self,new_response):   #往空列表self.response中增加新答案
        self.responses.append(new_response)
    def show_results(self):
        print("Survey results:")           #利用for循环按一定格式依次输出答案
        for response in self.responses:
            print('-'+response)
# question='what language did you first learn to speak?'
# my_survey=AnonymousSurvey(question)
# my_survey.show_question()
# print("Enter 'q' at any time to quit.\n")
# while True:
#     reponse=input("language:") #获取答案
#     if reponse=='q': #输入q就推出
#         break
#     my_survey.store_response(reponse.title())  #调用添加函数并使答案首字母大写输出
# print("\n thank you to everyone who praticipated in the survey!")
# my_survey.show_results()  #调用输出函数
# import unittest
# class TestAnonymousSurvey(unittest.TestCase):  #首先导入模块unittest和要测试的类AnonymousSurvey，并继承了unittest.TextCase
#     def test_store_single_response(self):                         
#         question="what language did you first learn to speak? "
#         my_survey=AnonymousSurvey(question)  #使用问题创建了一个名为my_survey的实例
#         my_survey.store_response('English')   #向其中存储了一个答案
#         self.assertIn('English',my_survey.responses)  #核实答案是否在其中
#     def test_store_three_responses(self):
#         question="what language did you first learn to speak?"
#         my_survey=AnonymousSurvey(question)
#         responses=['Chinese','English','Mandarin+']
#         for reponse in responses:                 #核实各个答案是否在其中
#             my_survey.store_response(reponse)
#         for reponse in responses:
#             self.assertIn(reponse,my_survey.responses)
# unittest.main()  #运行代码

#方法setup()
import unittest
class Testagain(unittest.TestCase):
    def setUp(self):
        question="what language did you first learn to speak? "
        self.my_survey=AnonymousSurvey(question)   #self是方便在整个类中使用，可以先撇开。变量名(my_survey)= 调用的类名(对象）
        self.responses=['English','Spanish','Mandarin']  #通过类AnonymousSurvey先创建一个调查对象，以self为前缀的变量可在这个类的任何地方使用
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
unittest.main()
       