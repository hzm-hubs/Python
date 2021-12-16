import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '表示单个外星人的类'

    def __init__(self, ai_settings, screen):  # 定义形参 初始化外星人并设置其起始位置
        super(Alien, self).__init__()  # 基类的init方法
        self.screen = screen  # 实例 以self为前缀的变量名可供后面的函数直接调用 将已有形参的值赋给新变量 新变量在等号前 已有变量在等号后
        self.ai_settings = ai_settings
        # 获取外星人图像储存位置 load()方法里的单引号 \\ 和冒号
        self.image = pygame.image.load(
            'Alien.bmp')
        self.rect = self.image.get_rect()  # 设置其rect属性
        self.rect.x = self.rect.width  # 将每个外星人的左边距设为精灵的宽度
        self.rect.y = self.rect.height  # 将每个外星人的长设为精灵的高度 设置外星人最初位置在屏幕左上角
        # 利用float()方法将self.rect.x转化为更精确的小数值并储存到self.x
        self.x = float(self.rect.x)

    def blitme(self):
        "在指定位置绘制外星人"
        self.screen.blit(self.image, self.rect)

    def check_edgs(self):
        "如果外星人位于屏幕边缘，就返回true"
        # 获取屏幕的rect属性赋值给screen_rect 新变量名与已有形参或宾凉转换时 新变量名在前
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:  # 当外星人右边碰到屏幕右边缘就返回True
            return True
        elif self.rect.left <= 0:  # 外星人左边碰到屏幕左边缘返回true ture用于返回循环
            return True

    def update(self):
        "向右或向左移动外星人"
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)  # 括号里改变持续移动的方向
        # self.x=self.x+(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = self.x  # 更新 将后者的值传递给前者
