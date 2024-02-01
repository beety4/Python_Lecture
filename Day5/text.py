import pygame

# 기본 설정
pygame.init()
SCREEN = pygame.display.set_mode((400, 500))
pygame.display.set_caption("myGame")


status = True
clock = pygame.time.Clock()
while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
            pygame.quit()

    # 60fps
    clock.tick(60)
    SCREEN.fill((255,255,255))

    # Font 생성
    myFont = pygame.font.SysFont("arial", 30, True, False)
    # Surface객체에 Text 그리기
    title = myFont.render("Pygame Text", True, (0,0,0))

    # Rect 생성
    txt_Rect = title.get_rect()

    # 위치 지정
    txt_Rect.centerx = 165
    txt_Rect.y = 140

    # Text Surface SCREEN 복사, Rect사용
    SCREEN.blit(title, txt_Rect)
    # SCREEN.blit(title, [50,200])
    pygame.display.flip()

