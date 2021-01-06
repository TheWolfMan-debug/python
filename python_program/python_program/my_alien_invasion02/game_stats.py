import os

class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 让游戏一开始处于非活跃状态
        self.game_active = False

        # 初始化最高分
        self.initial_high_score()
        
        # 帮助文档
        self.help_filename = r"E:\python_program\python_program\my_alien_invasion02\help_document.txt"
        self.game_pause_filename = r"E:\python_program\python_program\my_alien_invasion02\game_pause.txt"


        
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.alien_number = self.ai_settings.alien_number

    def initial_high_score(self):
        """初始化最高分"""
        self.filename = r"E:\python_program\python_program\my_alien_invasion02\highest_score.txt"
        self.high_score = 0
        # 如果存在highest_score.txt文件，则打开并初始化最高分
        if os.path.exists(self.filename):
            f_open = open(self.filename)
            self.high_score = int(f_open.read())
        else:
            # 如果不存在此文件，便创建一个highest_score.txt文件，并将最高分置为零
            f_open = open(self.filename,"w")
            f_open.write(str(self.high_score))
        f_open.close()
        
