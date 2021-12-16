import pygame
from pygame.sprite import Sprite  # d


class Ship(Sprite):  # 建立ship类
    # 定义函数，并调用已赋予参数的变量。此外self1可以理解为飞船的形参，并不强调要用self(教材函数中引用self),只是大家习惯使用self并且python中也默认它的存在及功能
    def __init__(self, ai_settings, screen):
        """ 初始化飞船并设置其初始位置 """
        super(Ship, self).__init__()
        # 获取形参screen中的值 储存到以self为前缀的screen中。以self为前缀的变量名可被该类中的任何函数如下面update函数直接调用，当该类被导用时也可被直接调用
        self.screen = screen
        self.ai_settings = ai_settings  # 添加属性
        # 获取飞船存储位置并获取其外接矩形,返回一个表示飞船的surface并储存到self.image中
        self.image = pygame.image.load('ship.bmp')
        # self.rect用来接收self1.image.get_rect()获得的rect属性，换句话说就是将存储的飞船属性与定义的形参对等。此外更简短的语句便于之后的简化引用
        self.rect = self.image.get_rect()
        # 使用get_rect函数获取相应surface(对象)的属性rect rect属性包括居中：center,centerx,centery与屏幕边缘对齐：top,bottom,left,righ水平或垂直：x,y(分别是矩形左上角的x,y的坐标)
        self.screen_rect = screen.get_rect()  # 将形参screen的矩形rect属性赋给self1.screen_rect
        # rect的意思是矩形再把rect属性与screen_rect相连  使用get_rect函数获取窗口screen的属性rect 将表示屏幕的矩形储存在self1.screen_rect中
        # 将每个飞船中心的x坐标设置在屏幕矩形的centerx 也就是屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom  # 将每个飞船的bottom（底部）放在屏幕矩形底部
        # 定义一个存储小数的变量 并将self.rect.centerx赋予seld.center 但rect的centerx等属性只能储存整数值，所以为了更准确表示飞船的位置 定义了新的储存小数值的self.center，使用函数float()将self.rect.centerx的值转换为小数
        self.center = float(self.rect.centerx)
        self.moving_right = False  # 添加了self.moving_right属性 默认状态下设置为False
        self.moving_left = False  # 原理同上

    def update(self):  # 移动标志
        # self.screen_rect.right表示矩形外框的右边缘x坐标 当然可以直接用1200代替 self.rect.right表示飞船的右边缘x坐标 大于这个值 就为越过右边界
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 执行向右持续移动 更新的是飞船的center值，而不是rect
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:  # 0是矩形外框的左边界坐标 大于这个值表示为越过左边界  若左移或游移的值大于左边界或右边界坐标江在触及矩形外框边缘后停止移动
            # 执行向左持续移动移动 速度增加 循环一次 移动一次 达到一直移动的目标
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center  # 根据self.center更新rect对象 前者指存储了后者的整数部分 对显示而言问题不大

    def blitme(self):  # 定义blitme函数，他根据self.rect知道的位置将图像绘制到
        # 利用screen.blit()方法 在指定位置(rect)绘制飞船(image)
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        "让飞船在屏幕上居中"
        self.center = self.screen_rect.centerx
