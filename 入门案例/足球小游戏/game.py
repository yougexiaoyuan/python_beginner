import pygame
pygame.init()

canvas = pygame.display.set_mode((800,540))
pygame.display.set_caption('足球弹弹弹')

bg = pygame.image.load('images/bg.png')
ball = pygame.image.load('images/ball.png')
speed = [2,1]
position = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                speed[0] = -2
            elif event.key==pygame.K_d:
                speed[0] = 2
            elif event.key==pygame.K_w:
                speed[1] = -1
            elif event.key==pygame.K_s:
                speed[1] = 1
    position = position.move(speed)
    if position.left<0 or position.right>800:
        speed[0] = -speed[0]
    if position.top<0 or position.bottom>540:
        speed[1] = -speed[1]
    canvas.blit(bg,(0,0))
    canvas.blit(ball,position)
    pygame.display.update()