import pygame


class Music(object):
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.music_path = self.ai_settings.current_file_path
        self.m_music = pygame.mixer.Sound(
            self.music_path +r'\musics\主菜单背景音乐.wav')
        self.m_music.set_volume(0.5)  # 设置音量

        self.g_music = pygame.mixer.Sound(
            self.music_path + r'\musics\游戏中背景音乐.wav')
        self.g_music.set_volume(0.3)  # 设置音量

        self.b_music = pygame.mixer.Sound(
            self.music_path + r'\musics\子弹音效.wav')
        self.b_music.set_volume(0.2)  # 设置音量

        self.d_music = pygame.mixer.Sound(
            self.music_path + r'\musics\爆炸声.wav')
        self.d_music.set_volume(0.3)  # 设置音量


    def menu_music(self):
        self.m_music.play(-1)#播放

    def menu_music_stop(self):
        self.m_music.stop()

    def game_music(self):
        self.g_music.play(-1)#播放

    def game_music_stop(self):
        self.g_music.stop()

    def bullet_music(self):
        self.b_music.play()#播放

    def bomb_music(self):
        self.d_music.play()#播放


    

    
