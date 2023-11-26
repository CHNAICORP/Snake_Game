import pygame
import time
import random

# 初始化 Pygame
pygame.init()

# 设置屏幕尺寸
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# 设置标题
pygame.display.set_caption('贪吃蛇游戏')

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 创建一个字体对象
font = pygame.font.Font(None, 25)

# 定义按钮类
class show_button():
    snake_speed = 10
    def __init__(self, font_obj, button_name, button_position) -> None:
        # 定义开始按钮的属性
        self.font_obj = font_obj
        self.button_name = button_name
        self.button_position = button_position
        self.button_color = (0, 255, 0)
        self.button_size = (150, 50)
        self.set_button()
        
    # 初始化按钮
    def set_button(self):
        # 绘制按钮
        pygame.draw.rect(screen, self.button_color, pygame.Rect(
            self.button_position, self.button_size))
        # 创建一个包含文字的 Surface 对象
        text = font.render(self.button_name, True, (0, 0, 0))
        # 计算文字的位置
        text_position = (self.button_position[0] + (self.button_size[0] - text.get_width()) / 2,
                         self.button_position[1] + (self.button_size[1] - text.get_height()) / 2)
        # 将文字绘制到屏幕上
        screen.blit(text, text_position)
    
    # 增加蛇的速度
    def increase_snake_speed(self):
        show_button.snake_speed += 1
    
    # 减少蛇的速度
    def reduce_snake_speed(self):
        show_button.snake_speed -= 1
        if show_button.snake_speed <= 1:
            show_button.snake_speed = 1
    
    # 显示蛇的速度
    def show_snake_speed(self):
        # 绘制按钮
        pygame.draw.rect(screen, self.button_color, pygame.Rect(
            self.button_position, self.button_size))
        # 创建一个包含文字的 Surface 对象
        text = font.render("{}:{}".format(self.button_name, show_button.snake_speed), True, (0, 0, 0))
        # 计算文字的位置
        text_position = (self.button_position[0] + (self.button_size[0] - text.get_width()) / 2,
                         self.button_position[1] + (self.button_size[1] - text.get_height()) / 2)
        # 将文字绘制到屏幕上
        screen.blit(text, text_position)

# 在屏幕中央显示一段文字
def message_display(text):
    largeText = pygame.font.Font(None, 25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width / 2), (height / 2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

# 创建一个包含文字的 Surface 对象和一个 Rect 对象
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# 蛇的绘制函数
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# 游戏内容
def game_contents(snake_speed):
    # 在 game_contents 函数的开始处定义一个标志
    return_to_main_menu = False
    # 游戏状态初始化
    game_over = False
    game_close = False

    # 蛇的大小
    snake_block = 10
    # 变量控制着蛇的移动速度。这个变量的值越大，蛇的速度就越慢。
    snake_speed = snake_speed

    Length_of_snake = 1  # 初始化蛇的长度
    # 蛇的存储数组
    snake_list = []

    # 定义蛇的头部初始位置
    x1 = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    y1 = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # 初始速度
    x1_change = snake_block  # 蛇开始时向右移动
    y1_change = 0           # y 方向上不移动

    # 随机生成食物的位置
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:    # 游戏的主循环
        while game_close == True:
            # 清空屏幕
            screen.fill(white)
            # 显示游戏结束的信息
            message_display('Game Over! Press C to Play Again or Q to Quit.')
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_q or key == pygame.K_c:
                        key = chr(key).lower()  # 将按键转换为小写字母
                        if key == 'q':
                            pygame.quit()
                            quit()
                        elif key == 'c':
                            game_close = False  # 退出这个循环，重置游戏状态
                            game_over = False   # 修改这里，使游戏可以重新开始

                            # 重置蛇的位置和长度
                            snake_list = []
                            Length_of_snake = 1

                            # 重新设置蛇的头部位置
                            # 定义蛇的头部初始位置
                            x1 = round(random.randrange(
                                0, width - snake_block) / 10.0) * 10.0
                            y1 = round(random.randrange(
                                0, height - snake_block) / 10.0) * 10.0

                            # 重新生成食物的位置
                            foodx = round(random.randrange(
                                0, width - snake_block) / 10.0) * 10.0
                            foody = round(random.randrange(
                                0, height - snake_block) / 10.0) * 10.0

                            break  # 重要：退出事件循环，以便重新开始游戏

        for event in pygame.event.get():
            # 用户点击窗口的关闭按钮，退出游戏
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:  # 只有当蛇不在水平移动时，才能左右移动
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:  # 只有当蛇不在水平移动时，才能左右移动
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:  # 只有当蛇不在垂直移动时，才能上下移动
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:  # 只有当蛇不在垂直移动时，才能上下移动
                    y1_change = snake_block
                    x1_change = 0

        # 更新蛇的头部位置
        x1 += x1_change
        y1 += y1_change
        # 检查蛇是否碰到边界
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # 保持游戏窗口背景
        screen.fill(white)

        # 绘制食物
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        # 存储蛇的头部
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # 处理蛇的移动
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        # 处理蛇的碰撞检测
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # 将蛇绘制到屏幕上
        our_snake(snake_block, snake_list)
        pygame.display.update()

        # 当蛇吃到食物时
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # 设置游戏速度
        time.sleep(1.0 / snake_speed)

# 游戏主界面
def gameLoop():
    running = True # 游戏循环
    start_button = show_button(font, "start game", (125, 125))  # 创建开始按钮
    show_snake_speed_button = show_button(font, "Snake Speed", (125, 425))
    increase_snake_speed_button = show_button(font, "Increase speed", (525, 125))
    reduce_snake_speed_button = show_button(font, "Reduce speed", (525, 425))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 检测鼠标点击事件
                x, y = pygame.mouse.get_pos()  # 获取鼠标的位置
                # 检查鼠标是否点击了按钮
                if start_button.button_position[0] < x < start_button.button_position[0] + start_button.button_size[0] and start_button.button_position[1] < y < start_button.button_position[1] + start_button.button_size[1]:
                    game_contents(show_snake_speed_button.snake_speed) # 开始游戏
                if increase_snake_speed_button.button_position[0] < x < increase_snake_speed_button.button_position[0] + increase_snake_speed_button.button_size[0] and increase_snake_speed_button.button_position[1] < y < increase_snake_speed_button.button_position[1] + increase_snake_speed_button.button_size[1]:
                    increase_snake_speed_button.increase_snake_speed()
                    print("increase snake speed!", increase_snake_speed_button.snake_speed)
                if reduce_snake_speed_button.button_position[0] < x < reduce_snake_speed_button.button_position[0] + reduce_snake_speed_button.button_size[0] and reduce_snake_speed_button.button_position[1] < y < reduce_snake_speed_button.button_position[1] + reduce_snake_speed_button.button_size[1]:
                    reduce_snake_speed_button.reduce_snake_speed()
                    print("reduce snake speed!", reduce_snake_speed_button.snake_speed)
        # 显示设置按钮
        show_snake_speed_button.show_snake_speed()
        # 更新整个游戏窗口
        pygame.display.flip()
gameLoop()
