import pygame
from pygame.sprite import Sprite #在pygame.sprite模块里面包含了一个名为Sprite类，他是pygame本身自带的一个精灵。但是这个类的功能比较少，因此我们新建一个类对其继承，在sprite类的基础上丰富，以方便我们的使用。
#导入精灵功能 pygame.sprite.Sprite(*groups): return Sprite  派生类想要重写sprite.更新方法并分配sprite.图像和sprite.rect属性。初始化器可以接受精灵将成为其成员的任意数量的组实例。当子类对精灵类进行分类时，一定要在将精灵类添加到组之前调用基初始化程序。
class Bullet(Sprite): #此类为对飞船发射子弹进行管理  Bullet为子类 Sprite为父类
    def __init__(self,ai_settings,screen,ship): # 形参
        pygame.sprite.Sprite.__init__(self)
        #super(Bullet,self).__init__() #super(bullet,self).__init__()=pygame.sprite.Sprite.__init__(self) self此时成为了bullet的形参
        #super()函数帮助子类和父类联系起来 为__init__传递ai_settings、screen、ship等实例 创建子弹bullet实例化  改代码也可简写成super().__init__()
         #导入sprite类，通过使用精灵，可将游戏中相关的元素编组，进而同时操作编组中的所有元素。为创建子弹实例，需要向__init__()传递ai_settings、screen、ship实例，调用super()来继承sprite
        self.screen = screen
        #在（0，0）处建立一个子弹的矩形，在设置正确的位置
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx #把子弹设置在飞船中心
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y
    def draw_bullet(self):#精灵组也有update和draw函数
        pygame.draw.rect(self.screen,self.color,self.rect) #括号里依次为子弹位置，子弹颜色，子弹属性
        


