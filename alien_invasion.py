import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
# from alien import Aliem
from game_stats import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象

    # 初始化背景设置
    pygame.init()
    # 创建Settings的对象
    ai_settings = Settings()
    # 设置显示窗口大小
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 设置窗口标题
    pygame.display.set_caption("飞机大战")
    # 创建一个用于存储游戏统计信息的对象
    stats = GameStats(ai_settings)
    # 创建飞机对象
    ship = Ship(ai_settings, screen)
    # 设置背景颜色
    # bg_color = (230, 230, 230)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个敌机编组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            # 控制飞机移动
            ship.update()
            # 加载子弹
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # 敌机移动
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 加载敌机
        # 每次循环时都重绘屏幕
        # 让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == "__main__":
    run_game()