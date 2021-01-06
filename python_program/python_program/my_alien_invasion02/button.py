import pygame.font


class Button():
    def __init__(self, ai_settings, screen):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.o_msg = "Play"
        self.n_msg = "Play new game"
        self.q_msg = "Quit the game"
        self.h_msg = "Help"

        # 设置开始游戏按钮的尺寸和其他属性
        self.width, self.height = 300, 50
        self.button_color = (0, 255, 0)
        self.button_new_game_color = (0, 0, 255)
        self.button_quit_game_color = (255,0,0)
        self.button_help_game_color = (255,255,0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建开始游戏按钮的rect对象，并使其居中
        self.play_rect = pygame.Rect(0, 0, self.width, self.height)
        self.play_rect.centerx = self.screen_rect.centerx
        self.play_rect.top = self.screen_rect.centery - self.height * 2

        # 按钮的标签只需创建一次
        self.prep_msg(self.o_msg)

        ################################################################

        # 创建开始新游戏按钮的rect对象，并使其居中
        self.play_new_game_rect = pygame.Rect(0, 0, self.width, self.height)
        self.play_new_game_rect.centerx = self.screen_rect.centerx
        self.play_new_game_rect.top = self.play_rect.bottom

        # 创建开始新游戏的按钮
        self.prep_new_game(self.n_msg)

        ################################################################

        # 创建开始新游戏按钮的rect对象，并使其居中
        self.quit_game_rect = pygame.Rect(0, 0, self.width, self.height)
        self.quit_game_rect.centerx = self.screen_rect.centerx
        self.quit_game_rect.top = self.play_new_game_rect.bottom

        # 创建开始新游戏的按钮
        self.prep_quit_game(self.q_msg)

        ################################################################
        # 创建帮助按钮的rect对象，并使其居中
        self.help_game_rect = pygame.Rect(0, 0, self.width, self.height)
        self.help_game_rect.centerx = self.screen_rect.centerx
        self.help_game_rect.top = self.quit_game_rect.bottom

        # 创建开始新游戏的按钮
        self.help_game(self.h_msg)

    def prep_msg(self, o_msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.o_msg_image = self.font.render(
            o_msg, True, self.text_color, None)
        self.o_msg_image_rect = self.o_msg_image.get_rect()
        self.o_msg_image_rect.center = self.play_rect.center

    def prep_new_game(self, n_msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.n_msg_image = self.font.render(
            n_msg, True, self.text_color, None)
        self.n_msg_image_rect = self.n_msg_image.get_rect()
        self.n_msg_image_rect.center = self.play_new_game_rect.center

    def prep_quit_game(self,q_msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.q_msg_image = self.font.render(
            q_msg, True, self.text_color, None)
        self.q_msg_image_rect = self.q_msg_image.get_rect()
        self.q_msg_image_rect.center = self.quit_game_rect.center

    def help_game(self,h_msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.h_msg_image = self.font.render(
            h_msg, True, self.text_color, None)
        self.h_msg_image_rect = self.h_msg_image.get_rect()
        self.h_msg_image_rect.center = self.help_game_rect.center  


    def draw_button(self):
        # 绘制开始游戏按钮
        self.screen.fill(self.button_color, self.play_rect)
        # 开始游戏文本
        self.screen.blit(self.o_msg_image, self.o_msg_image_rect)
        # 绘制开始新游戏按钮
        self.screen.fill(self.button_new_game_color, self.play_new_game_rect)
        # 开始新游戏文本
        self.screen.blit(self.n_msg_image, self.n_msg_image_rect)
        # 绘制退出游戏按钮
        self.screen.fill(self.button_quit_game_color, self.quit_game_rect)
        # 退出游戏文本
        self.screen.blit(self.q_msg_image, self.q_msg_image_rect)
        # 绘制帮助游戏按钮
        self.screen.fill(self.button_help_game_color, self.help_game_rect)
        # 帮助游戏文本
        self.screen.blit(self.h_msg_image, self.h_msg_image_rect)
