import pygame 
import sys     #"""重构模块：旨在简化既有的代码结构，使其更容易扩展 check_events()函数可以简化run_game()并隔离事件管理循环"""
from alien import Alien #导入alien文件中的Alien类
from bullet import Bullet
from time import sleep
def check_keydown_events(event,ai_settings,screen,ship,bullets): #def括号类的数为之后函数类需要调用的变量名
    if event.key==pygame.K_RIGHT:  #检测到为右移事件 用户点击一次右箭头键 飞船将向右移动1像素
        ship.moving_right = True #循环移动
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        #注意大写 根据自己喜欢的按键设置触发事件发生的，数字已大键为准 格式如 K_
        #if len(bullets)<ai_settings.bullets_allowed:
        #    new_bullet=Bullet(ai_settings,screen,ship)
        #    bullets.add(new_bullet)  将开火功能换至以下新函数管理
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()
def fire_bullet(ai_settings,screen,ship,bullets):
    """ 如果还没有达到限制，就发射一颗子弹 """
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings,screen,ship) #当玩家按下开火键就通过类的实例化创建一个新子弹 并通过add()方法将其储存到bullets编组中
        bullets.add(new_bullet) 
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:  #停止移动
        ship.moving_right=False
    elif event.key == pygame.K_LEFT: #停止移动
          ship.moving_left=False
def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    "响应按键和鼠标事件"
    #把管理时间的代码移到移到一个名为check_events()的函数中，以简化run_game()隔离事件并管理循环
    for event in pygame.event.get(): #for事件循环 if判断事件
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN: #检测是否为特定的键
           # if event.key==pygame.K_RIGHT:  #检测到为右移事件 用户点击一次右箭头键 飞船将向右移动1像素
              # ship.moving_right = True #循环移动
           # elif event.key==pygame.K_LEFT:
                #ship.moving_left=True
            check_keydown_events(event,ai_settings,screen,ship,bullets) #调用之前的keydown函数
        elif event.type==pygame.KEYUP:  
           #if event.key == pygame.K_RIGHT:  #停止移动
               # ship.moving_right=False
           # elif event.key == pygame.K_LEFT: #停止移动
               # ship.moving_left=False
            check_keyup_events(event,ship)  #调用之前的keyup函数
        elif event.type==pygame.MOUSEBUTTONDOWN: #MOUSEBUTTONDOWN:鼠标按钮响应事件
            mouse_x,mouse_y=pygame.mouse.get_pos() #get_pos()方法，返回一个元组，其中包含玩家单击时鼠标的x，y坐标,
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    "在玩家单击play按钮时开始新游戏"
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y) #button_clicked只能为true或false collidepoint()检查鼠标单击位置坐标是否在play按钮的rect内
    if button_clicked and not stats.game_active: #当位于play和游戏处于非开始状态是，游戏才重新开始，避免play按钮不存在时 单击该区域也会重新开始游戏
        #重置游戏设置
        ai_settings.initalize_dynamic_settings()
        pygame.mouse.set_visible(False) #通过向set_visible()传递false，让pygame在光标位于游戏窗口内时将其隐藏起来
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active=True #你上次打stats.pygame_active=True 是什么意思？？？？？
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        #重置记分牌图像
        sb.prep_score() 
        sb.prep_high_score() #重新开始游戏需要重置计分图像
        sb.prep_level()
        sb.prep_ships()
        #创建一群新的外星人，并在飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
def create_fleet(ai_settings,screen,ship,aliens):
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings,screen,aliens,alien_number,row_number)
def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update() 
    for bullet in bullets.copy(): #删除已经飞过屏幕的子弹，以免占用内存和处理能力 在for循环中不应从列表或编组中删除条目 所以通过copy()方法遍历编组的副本
        if bullet.rect.bottom <=0:#以子弹的底部所在的坐标到达窗口上边坐标为0
            bullets.remove(bullet) #使用remove方法移除
    "检查是否有子弹击中了外星人，如果是这样就删除相应的外星人与子弹"
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets) #调用check_bullet_alien_collisions方法需要传递实参 所以在函数形参里加入了stats和sb
def  check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True) #遍历编组bullets中的每个子弹 在遍历编组aliens中的每个外星人 当有子弹和外星人重叠时 groupcollide()就在它返回的字典中添加一个键（子弹）-值（外星人）对。俩个实参（布尔值）true告诉pygame删除这个键值对 前false后true删除外星人保留子弹 前true后false删除子弹保留外星人
    #方法sprite.groupcollide将每个外星人的rect属性和每颗子弹的rect属性比较 并返回一个字典 储存发生了碰撞的外星人
    if collisions: #检查字典是否存在，如果产生碰撞，就在得分上加上一个外星人值的点数
        for aliens in collisions.values(): #如果一次循环中有俩颗子弹射中外星人，或因子弹更宽同时击中了多少个外星人，只能得到一个被消灭的外星人点数。所以遍历collisions键值对中aliens元素值
           stats.score +=ai_settings.aliens_points*len(aliens) #更新得分和记分牌。 
           sb.prep_score() #利用prep_score()来更新得分图像
           check_high_score(stats,sb) #检查最高得分
    if len(aliens)==0:
        #删除现有子弹，加快游戏节奏，并创建新的外星人
        bullets.empty()
        ai_settings.increase_speed()
        #消灭完一次外星人，提升一次等级
        stats.level+=1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x=ai_settings.screen_width-2*alien_width #可利用的水平空间=屏幕窗口的宽度-2个外星人的宽度(代表的是留出的屏幕俩边的边距)
    number_aliens_x=int(available_space_x/(2*alien_width)) #水平外星人的数量=可利用的水平空间/2个外星人的宽度(代表一个外星人的宽度+俩个外星人之间的间距) 的整数部分
    return number_aliens_x  #返回number_aliens_x
def get_number_aliens_y(ai_settings,alien_height,ship_height): #添加多行外星人除去第一行外星人 需要使用的形参在括号里
    available_space_y=ai_settings.screen_height-3*alien_height-ship_height #屏幕里可以用的垂直空间为屏幕高度减去飞船高减去第一行外星人的上边距(外星人高)和第一行外星人高度与第一行与第二行的间距(外星人高度)
    number_rows=int(available_space_y/(2*alien_height)) #可以用的垂直空间行数
    return number_rows#返回值
def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y=(ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    #alien_width=alien.rect.width #将外星人的rect的width属性赋予alien_width
    alien=Alien(ai_settings,screen) #遍历一次创建一个外星人
    alien_width=alien.rect.width #将外星人的rect的width属性赋予alien_width
    alien.x=alien_width+2*alien_width*alien_number #算出的宽度设置为外星人的x坐标 例：第一个alien_bumber的x坐标只需隔一个屏幕左边距 而第二个alien_number的xz坐标需要隔一个屏幕左边距+一个外星人的宽度+一个外星人之间的间距
    alien.rect.x=alien.x  #将x坐标赋给外星人的rect中的x属性
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number#添加y坐标属性
    aliens.add(alien) #将创建的外星人通过add方法加入aliens编组
def check_fleet_edgs(ai_settings,aliens):
    "有外星人到达边缘时采取相应的措施"
    for alien in aliens.sprites(): #遍历外星人精灵组
        if alien.check_edgs():  #引用方法判断alien外星人是否达到改变方向的条件 成立就执行以下语句 否定直接跳出 开始下一遍历 直至遍历结束
            change_fleet_direction(ai_settings,aliens)#改变方向和下移
            break #跳出循环
def change_fleet_direction(ai_settings,aliens):
    "将整群外星人下移，并改变他们的方向"
    for alien in aliens.sprites(): #遍历外星人精灵组
        alien.rect.y +=ai_settings.fleet_drop_speed #外星人的坐标都向下移动fleet_drop_speed的值
    ai_settings.fleet_direction*=-1 #改变方向
def check_high_score(stats,sb):
    "检查是否诞生了新的最高得分"
    if stats.score > stats.high_score:
        stats.high_score=stats.score # 比较修改最高得分值
        sb.prep_high_score() #利用prep_high_score来更新包含最高得分的图像
def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    "响应被外星人撞到的飞船"
    #将ships_left减少1
    if stats.ships_left>0:
        stats.ships_left -=1
        #清空外星人列表和子弹列表
        sb.prep_ships( )#刷新一次少一艘飞船 
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人，并将飞船放到屏幕低端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #暂停
        sleep(0.5) #使用sleep函数实现暂停
    else:
        stats.game_active=False#当外星人的数量中卫0，将结束游戏 
        pygame.mouse.set_visible(True) #结束游戏使光标可见
def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    "检查是否有外星人到达了屏幕底端"
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            #像飞船被撞到一样处理
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break
def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #"检查是否有外星人位于屏幕边缘，更新外星人群中所有外星人的位置"
    check_fleet_edgs(ai_settings,aliens)
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)
    aliens.update()#调用alien文件中的update函数
    if pygame.sprite.spritecollideany(ship,aliens): #检测外星人和飞船之间的碰撞
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button): 
    """ 更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color) #使设置函数充满屏幕
    sb.show_score() #显示得分
    for bullet in bullets.sprites():  #方法bullets.sprites():返回一个列表，包含bullets中的所有精灵 也就是储存在bullets中的所有子弹
        bullet.draw_bullet() #遍历编组中的所有精灵并都采用draw_bullet()方法
    #如果游戏处于非活跃状态，就绘制play按钮
     #if not stats.game_active:
     #   play_button.draw_button()
    ship.blitme() #ship是单个调用blitme函数
    aliens.draw(screen) #在屏幕上绘制编组的每个外星人  对编组调用draw()时，pygame自动绘制编组的每个元素，绘制位置由元素的属性rect决定
    "在窗口上用pygame中的blitme方法绘制飞船函数" #注释#方法在任何位置都行，是忽略该行在#之后的所有内容 而单三"注释必须单独提行与代码语句分开
    if not stats.game_active:
        play_button.draw_button() #让play按钮放在最后，可以使play置于一切元素之上优先显示
    pygame.display.flip()