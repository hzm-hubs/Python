import pygame.font # pygame中没有内置创建按钮的方法，所以导入font模板，它能让pygame将文本渲染到屏幕上
class Button():
    def __init__(self,ai_settings,screen,msg): #方法__init__接受参数，对象ai_settings,screen,msg(是要在按钮中显示的文本)
        "初始化按钮的属性"
        self.screen=screen
        self.screen_rect=screen.get_rect() #使用get_rect方法获取形参screen的属性并赋予screen_rect
        #设置按钮的尺寸和其他属性
        self.width,self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)  #该行代码指定什么文字渲染文本，实参None让pygame使用默认字体，而48指定了文本的字号
        #创建按钮的rect的对象，并使其居中
        self.rect=pygame.Rect(0,0,self.width,self.height) #创建的按钮并非基于图像，所以必须使用pygame.Rect()类从空白处创建一个矩形。创建这个实例时必须提供矩形左上角的x,y的坐标(这里设为0，0)，还有矩形的高度与宽度
        self.rect.center=self.screen_rect.center  #移动按钮至屏幕中心
        #按钮的标签只需创建一次
        self.prep_msg(msg)#pygame通过你要显示的字符串渲染为图像来处理文本，此处调用prep_msg()来处理这样的渲染
    def prep_msg(self,msg): #方法prep_msg接受实参self以及要渲染为图像的文本(msg)。调用font.render()将储存在msg中的文本转化为图像
        "将msg渲染为图像，并使其在按钮上居中"
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color) #括号内，msg指代文本，True(布尔实参)在这里指定开启还是关闭反锯齿功能(反锯齿让文本的边缘更平滑)，后面俩个实参指定文本颜色与矩形按钮即背景色颜色，若没指定背景色，默认透明背景
        self.msg_image_rect=self.msg_image.get_rect() #让文本图像成于按钮上
        self.msg_image_rect.center=self.rect.center #根据文本创建一个rect,并将其属性设为按钮的center属性
    def draw_button(self):
        #绘制一个用颜色填充的按钮，在绘制文本
        self.screen.fill(self.button_color,self.rect) #调用fill填充颜色
        self.screen.blit(self.msg_image,self.msg_image_rect) #利用blit绘制按钮