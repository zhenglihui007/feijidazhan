import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个敌机的类"""
    def __init__(self, ai_settings, screen):
        """初始化敌机并设置起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载敌机图像，并设置rect属性
        self.image = pygame.image.load("./feiji/enemy0.png")
        self.rect = self.image.get_rect()

        # 每个敌机最初在屏幕左上角附件
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储敌机的精确位置
        self.x = float(self.rect.x)

    def biltme(self):
        """在指定位置绘制敌机"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果敌机位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向右或向左移动敌机"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x