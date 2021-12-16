class GameStats(): #gen
    def __init__(self,ai_settings):
        """ 初始化统计信息 """
        self.ai_settings=ai_settings
        self.reset_stats()
        self.game_active=False #使游戏刚启动处于开始状态,为创建play按钮此处修改成立非活动状态
        "在任何情况下都不应该重置最高分"
        self.high_score=0 #不重置所以放在__init__函数中
    def reset_stats(self):
        #初始化在游戏期间可能变化的统计信息
        self.ships_left = self.ai_settings.ship_limit
        self.score=0    #因为每次重开都需要重置得分，所以放置reset_stats方法下
        self.level=1 #起始等级为1

