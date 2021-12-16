import pygame.font #创建记分板，因为需要在屏幕上显示，所以大致方法与button类相似
from pygame.sprite import Group #使用GROUP方法 是需要从pygame.sprite中导入的
from ship import Ship
class Scoreboard():
    "显示得分信息的类"
    def __init__(self,ai_settings,screen,stats):
        "初始化显示得分涉及的属性"
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats
        #显示得分信息时使用的字体设置
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        #准备初始得分函数
        self.prep_score() #调用方法为什么不带() ????
        self.prep_high_score()  #最高得分应与得分分开来 所以编写了一个新方法
        self.prep_level()
        self.prep_ships()
    def prep_ships(self):
        "显示还剩下几次玩的机会也就是显示还剩下多少艘飞船"
        self.ships=Group() #创建一个空编组实例
        for ship_number in range(self.stats.ships_left): #根据还有多少艘飞船进行一个循环的相应次数
            ship=Ship(self.ai_settings,self.screen) #使飞船成像
            ship.rect.x=12+ship_number*ship.rect.width #设置位置
            ship.rect.y=4
            self.ships.add(ship)
    def prep_score(self):
        "将得分转换为一幅渲染的图像"
        score_str=str(self.stats.score) #因为倍数是1.5,可能会出现非整得分
        rounded_score=int(round(self.stats.score,-1)) #round函数让self.stats.score的小数精确到小数点后多少位，小数位数由第二个实参确定，若为负数，round函数将圆整到最近的10，100，1000等整数倍，此处为-1，则最近的整倍数为10
        score_str="{:,}".format(rounded_score) #    使用了一个字符串格式，在数值转换为字符串时在其中插入逗号，输出100,000,而不是100000
        #字符串类型格式化采用format()方法，基本使用格式是：
        #<模板字符串>.format(<逗号分隔的参数>)
        #调用format()方法后会返回一个新的字符串，参数从0 开始编号。
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        #将得分放在屏幕右上角
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20 #得分渲染文本距离上顶框20像素
    def prep_high_score(self):
        "将最高分渲染为图像"
        high_score=int(round(self.stats.high_score,-1))
        high_score_str="{:,}".format(high_score) #用逗号表示千分位分隔符
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
        #将得分放在屏幕顶中央
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx #最高分图像的center中心x坐标与屏幕一致
        self.high_score_rect.top=self.score_rect.top #最高得分的top与屏幕一样高
    def prep_level(self):
        "将等级渲染为图像"
        self.level_image=self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.bg_color) #因为等级不用太多显示
        #设置位置
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.screen_rect.right-20
        self.level_rect.top=self.score_rect.bottom+80
    def show_score(self):
        "在屏幕上显示得分"
        self.screen.blit(self.score_image,self.score_rect) #blit方法绘制渲染文本
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen) #为显示飞船，调用了draw()