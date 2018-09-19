import pygame
from pygame.locals import *
import time
import random


# 我方飞机
class Wofangfeij():
    def __init__(self, dyck):
        self.x = 200
        self.y = 700
        self.screen = dyck
        self.image = pygame.image.load("./feiji/hero1.png")
        self.cczd = []

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.cczd:
            bullet.display()
            bullet.move()
            if bullet.judge():# 判断子弹是否越界
                self.cczd.remove(bullet)

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5

    def fire(self):
        self.cczd.append(Wofangzidan(self.screen, self.x, self.y))


#敌方飞机
class Difangfeij():
    def __init__(self, dyck):
        self.x = 0
        self.y = 0
        self.screen = dyck
        self.image = pygame.image.load("./feiji/enemy0.png")
        self.cczd = []  # 存储发射出去的子弹对象引用
        self.direction = "right"  # 用来存储飞机默认的显示方向

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.cczd:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                self.cczd.remove(bullet)

    def move(self):
        if self.direction=="right":
            self.x += 5
        elif self.direction=="left":
            self.x -= 5

        if self.x>480-50:
            self.direction = "left"
        elif self.x<0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1, 200)
        if random_num == 8 or random_num == 90:
            self.cczd.append(Difazidan(self.screen, self.x, self.y))


#子弹类
class Wofangzidan:
    def __init__(self, dyck, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = dyck
        self.image = pygame.image.load("./feiji/bullet.png")
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 20

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class Difazidan:
    def __init__(self, dyck, x, y):
        self.x = x + 25
        self.y = y
        self.screen = dyck
        self.image = pygame.image.load("./feiji/enemy0.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 2

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False


# 控制飞机
def jianpan(key):
    # 获取事件，比如按键等
    jian_a = pygame.key.get_pressed()
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            # print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                # print('space')
                key.fire()
            # 检测按键是否是a或者left
    if jian_a[pygame.K_a] or jian_a[pygame.K_LEFT]:
                # print(KEYDOWN)
        key.move_left()
            # 检测按键是否是d或者right
    elif jian_a[pygame.K_d] or jian_a[pygame.K_RIGHT]:
                # print('right')
        key.move_right()
    elif jian_a[pygame.K_w] or jian_a[pygame.K_UP]:
                # print('right')
        key.move_up()
    elif jian_a[pygame.K_s] or jian_a[pygame.K_DOWN]:
                # print('right')
        key.move_down()
            # 检测按键是否是空格键
    # elif jian_a[pygame.K_SPACE]:
    #     print('space')
    #     key.fire()

# 创建主函数
def main():
    # 1.创建一个窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 2.创建背景图片
    background = pygame.image.load("./feiji/background.png")

    # 3.创建玩家飞机
    wjfj = Wofangfeij(screen)

    # 4.创建敌机
    dffj = Difangfeij(screen)

    # 5.加载图片
    while True:
        screen.blit(background,(0,0)) # 加载背景图片

        wjfj.display()  # 加载我方飞机

        dffj.display()  # 加载敌方飞机
        jianpan(wjfj)   # 控制飞机
        # jian(wjfj)
        dffj.move()     # 调用敌方飞机移动
        dffj.fire()     # 敌方飞机开火
        pygame.display.update()
        time.sleep(0.01)


if __name__ == "__main__":
    main()