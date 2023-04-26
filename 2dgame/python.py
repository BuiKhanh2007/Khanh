import pygame

pygame.init()
screen = pygame.display.set_mode((500, 300))
dx, dy = 1, 1
rect = pygame.Rect(dx, dy, 20, 20)
floor = pygame.Rect(0, 290, 500, 10)
gravity = 1
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # Xoá màn hình
    screen.fill((255, 255, 255))

    # Di chuyển hình chữ nhật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect.move_ip(-1, 0)
    if keys[pygame.K_RIGHT]:
        rect.move_ip(1, 0)
    if keys[pygame.K_UP]:
        rect.move_ip(0, -2)
    if keys[pygame.K_DOWN]:
        rect.move_ip(0, 1)
    else:
        rect.move_ip(0, gravity * dy)
    
    if rect.colliderect(floor):
        rect.bottom = floor.top

    # Vẽ lại hình chữ nhật ở vị trí mới
    pygame.draw.rect(screen, (250, 0, 255), rect)
    pygame.draw.rect(screen, (0, 255, 0), floor)
    pygame.display.update()

pygame.quit()
