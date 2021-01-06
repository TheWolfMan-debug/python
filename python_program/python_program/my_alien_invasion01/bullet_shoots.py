from bullet import Bullet
from time import sleep


class BulletShoots():
    def __init__(self, ai_settings, screen, ship):
        self.ai_settings = ai_settings
        self.screen = screen
        self.ship = ship

        # 使子弹持续射击标志为假
        self.bullet_shoot = False

    def update_shoots(self, bullets):
        """使子弹持续射击"""
        new_bullet = Bullet(self.ai_settings, self.screen, self.ship)
        bullets.add(new_bullet)

        # for i in range(5):
        #     new_bullet = Bullet(self.ai_settings, self.screen, self.ship)
        #     new_bullet.y += (i * new_bullet.ai_settings.bullet_height + i*10)
        #     bullets.add(new_bullet)

