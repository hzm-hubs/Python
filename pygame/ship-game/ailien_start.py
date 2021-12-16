# import sys
# import pygame
# def run_game():  #开头函数
#     # 初始化游戏并并创建一个屏幕对象
#     pygame.init() #运用init()初始化背景设置
#     screen = pygame.display.set_mode((1200,800)) #运用display.set_mode来创建一个名为screen的显示窗口  set_mode 定义了窗口的大小（宽1200，高800）
#     pygame.display.set_caption("Alien Invasion")  #设置窗口标题
#     bg_color=(240,250,230)#定义一个背景色，并存储在bg_color
#     # 开始游戏的循环
#     while True:
#         #监视键盘和鼠标事件
#         for event in pygame.event.get(): #事件循环 所有键盘和鼠标时间都将促使for循环运行
#             if event.type == pygame.QUIT: #使用if语句来检测并响应特定的事件  当玩家单击游戏窗口关闭按钮时，将检测到pygame.quit事件
#                 sys.exit() #调用sys.exit来退出游戏
#         screen.fill(bg_color) #调用fill方法 让背景色充满整个屏幕
#         pygame.display.flip() #命令pygame让最近绘制的屏幕可见
# run_game()#初始化游戏并开始主循环 
#第二种方法
import sys   #sys模块包含了与Python解释器和它的环境有关的函数。
import pygame 
import datetime
from alien import Alien
from settings import Settings 
from ship import Ship
from pygame.sprite import Group #导入精灵组功能 来统一管理精灵的绘制和更新 因此精灵组更像一个简单的容器
from game_stats import GameStats
import game_functions as gf #导入重构模块并给与命名调用
from button import Button
from scoreboard import Scoreboard
def run_game():
  pygame.init()
  ai_settings = Settings() #实例化Settings,将其中的属性存储在变量ai_settings中方便后面调用
  screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
  #nowtime=datetime.datetime.now().strftime('%Y-%m-%d')
  #pygame.display.set_caption("Alien Invasion"+"  Time:"+nowtime)
  ship=Ship(ai_settings,screen)  # 导入Ship类并实例化。传入实参screen，将Ship类中的screen与实参screen(创建的窗口)联系起来。传入实参ai_settings ,现在只要速度的值大于1 飞船的移动速度就比以前大。在创建屏幕后创建一个名为ship的Ship的实例
  bullets=Group()#创建一个group实例并命名为bullets 子弹编组
  aliens=Group()
  alien=Alien(ai_settings,screen) #创建一个实参外星人 注意()里一定要有足够的形参
  gf.create_fleet(ai_settings,screen,ship,aliens)
  stats=GameStats(ai_settings) #创建一个用于存储游戏统计信息的实例
  play_button=Button(ai_settings,screen,"Play") #创建按钮实例，根据形参对应的原则 msg=="play"
  sb=Scoreboard(ai_settings,screen,stats)
  while True: #开始游戏主循环
    nowtime=datetime.datetime.now().strftime(' %Y/%m/%d %H:%M:%S')
    pygame.display.set_caption("Alien Invasion"+"  北京时间:"+nowtime)
    # for event in pygame.event.get():   #所有键盘和鼠标事件都将触发FOR循环
    #     if event.type == pygame.QUIT:   #当用户出发的时间类型为单击游戏窗口关闭时  quit(退出)
    #         sys.exit()   #一般执行到末尾程序会自动退出  但若需要中途退出就需要使用exit函数
    gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
    if stats.game_active:
      ship.update()
      #gf.update_aliens(aliens)               
      # bullets.update() 当你对编组使用update功能 编组将自动对其中的每个精灵使用update() bullets.update()将为编组bullets中的每颗子弹调用bullet.update()  将该组模块的内容移到game_functions.py中，为避免函数冲突 将此处的功能注释掉
      # for bullet in bullets.copy(): #删除已经飞过屏幕的子弹，以免占用内存和处理能力
      #     if bullet.rect.bottom <=0:
      #  bullets.remove(bullet)
      #print(len(bullets)) 输出bullets编组的长度
      gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets) #更新子弹
      gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
    gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button) #更新 各个定义函数、方法和调用时形参与实参的位置要一一对应并且统一，若随意排序会报错
    # screen.fill(ai_settings.bg_color) #调用fill方法 让背景色充满整个屏幕
    # ship.blitme()  #调用blitme方法将飞船图像绘制出来
    # pygame.display.flip() #命令pygame让最近绘制的屏幕可见
    #gf.update_screen(ai_settings,screen,ship,bullets) 在python中出现俩条相同语句时只执行一条
run_game() #初始化游戏并开始主循环 
  