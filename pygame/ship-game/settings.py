class Settings():
    """ 存储游戏的所有设置的类  """
    def __init__(self):
        ''' 初始化游戏的设置 '''
        #屏幕的设置
        self.screen_width = 1200 #
        self.screen_height = 800 #左上角坐标为（0，0），右下角坐标为（1200，800）单位为像素 1200为宽 800为高
        self.bg_color = (230,230,230)  #更改参数后要运行\保存一次终端才会更改
        self.ship_speed_factor=1.5 #当飞船持续移动时 更改飞船的移动的速度 飞船速度为1.5像素
        self.bullet_speed_factor = 3
        self.ship_limit=3
        self.bullet_width = 50 #创建宽3像素，高15像素，深灰色子弹 子弹速度为1，比飞船慢
        self.bullet_height = 15
        self.bullet_color=255,0,0
        self.bullets_allowed=5 #限制子弹的颗数，让屏幕上最多存在3颗
        self.alien_speed_factor=0.7
        self.fleet_drop_speed=50 #制定了有外星人撞到屏幕边缘时，外星人群向下移动的速度。将它与水平速度分开的好处在于可以分开调整
        #fleet_direction为1表示右移，同理-1表示左移
        self.fleet_direction=1 #1与-1通过if-elif语句来切换方向 向右移动 移动一下x增大1 向左移动一下x减小1
        #以什么样的速度加快游戏节奏
        self.speedup_scale=1.1 #游戏节奏速度翻倍数
        self.initalize_dynamic_settings()
        self.score_scale=1.5 #为了提高点数的速度
    def initalize_dynamic_settings(self):
        self.ship_speed_factor=1.5 
        self.bullet_speed_factor=3
        self.alien_speed_factor=0.7
        self.fleet_direction=1
        self.aliens_points=50 #每个外星人的值为50
    def increase_speed(self): #为提高游戏元素的速度，将每个速度设置都乘以speedup_scale
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale 
        self.aliens_points=int(self.aliens_points*self.score_scale) #更新点数值
        print(self.aliens_points)  #现在每提高一个等级，都会在终端看到新的点数值