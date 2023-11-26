import pygame
pygame.init()

# 创建一个窗口
screen = pygame.display.set_mode((800, 600))

# 定义按钮的属性
button_color = (0, 255, 0)
button_position = (350, 250)
button_size = (100, 50)

# 创建一个字体对象
font = pygame.font.Font(None, 25)

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 检测鼠标点击事件
            x, y = pygame.mouse.get_pos()  # 获取鼠标的位置
            # 检查鼠标是否点击了按钮
            if button_position[0] < x < button_position[0] + button_size[0] and button_position[1] < y < button_position[1] + button_size[1]:
                print("Button clicked!")

    # 绘制按钮
    pygame.draw.rect(screen, button_color, pygame.Rect(button_position, button_size))

    # 创建一个包含文字的 Surface 对象
    text = font.render('Start Game!', True, (0, 0, 0))

    # 计算文字的位置
    text_position = (button_position[0] + (button_size[0] - text.get_width()) / 2, 
                     button_position[1] + (button_size[1] - text.get_height()) / 2)

    # 将文字绘制到屏幕上
    screen.blit(text, text_position)

    pygame.display.flip()

pygame.quit()
