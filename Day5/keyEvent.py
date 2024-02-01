import pygame

# 기본 설정
pygame.init()
SCREEN = pygame.display.set_mode((400, 500))
pygame.display.set_caption("myGame")

# 이미지 로딩 및 크기 변경
plane = pygame.image.load("img/plane.png")
plane = pygame.transform.scale(plane, (64, 64))
plane_Rect = plane.get_rect()
plane_Rect.centerx = 200
plane_Rect.centery = 460


status = True
clock = pygame.time.Clock()
while status:
    # 60fps
    clock.tick(60)

    SCREEN.fill((255, 255, 255))
    #SCREEN.blit(plane, [165, 430])
    SCREEN.blit(plane, plane_Rect)
    pygame.display.flip()

    # Key 이벤트 핸들러
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("왼쪽")
            if event.key == pygame.K_RIGHT:
                print("오른쪽")
            if event.key == pygame.K_UP:
                print("위쪽")
            if event.key == pygame.K_DOWN:
                print("아래쪽")
