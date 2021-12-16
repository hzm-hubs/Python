# dsf
from flask import Flask
#  escape() 可以用户老转义字符
from markupsafe import escape

app = Flask(__name__)

# 首页


@app.route('/')
def homepage():
    return 'hello, word'


@app.route('/info')
def hello_world():
    return {
        'name': "hliuiu",
        'age': 19
    }


# 接收路径参数 设置的函数变量key值要与路径上设置的一致
@app.route('/user/<name>')
def handleFunc(name):
    print('获取到的name参数值' + name)
    return f"欢迎，{escape(name)}"

# 单行注解
# powershell 启动
# 环境 通过将FLASK_ENV环境变量设置为development来启用开发模式。
# > $env:FLASK_ENV = "development"
# 名字
# > $env:FLASK_APP = "hello"
# > flask run
# or
# $ export FLASK_APP = hello.py
# $ python - m flask run


"""
多行注解
"""
