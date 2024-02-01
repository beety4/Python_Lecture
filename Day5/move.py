import pygame

# 기본 설정
pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("myGame")

# 이미지 로딩 및 크기 변경
plane = pygame.image.load("img/plane.png")
plane = pygame.transform.scale(plane, (64, 64))
plane_Rect = plane.get_rect()
plane_Rect.centerx = 200
plane_Rect.centery = 460

dx = 0
dy = 0


status = True
clock = pygame.time.Clock()
speed = 3
while status:
    # Key 이벤트 핸들러
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -speed
                print("왼쪽")
            if event.key == pygame.K_RIGHT:
                dx = speed
                print("오른쪽")
            if event.key == pygame.K_UP:
                dy = -speed
                print("위쪽")
            if event.key == pygame.K_DOWN:
                dy = speed
                print("아래쪽")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_RIGHT:
                dx = 0
            if event.key == pygame.K_UP:
                dy = 0
            if event.key == pygame.K_DOWN:
                dy = 0

    # 60fps
    clock.tick(60)

    # 배경 설정 및 plan 생성
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(plane, plane_Rect)
    pygame.display.flip()

    # 키 누른 만큼 위치 조정
    plane_Rect.x += dx
    plane_Rect.y += dy

    # Screen OUT 방지
    if plane_Rect.left < 0:
        plane_Rect.left = 0
    if plane_Rect.right > SCREEN_WIDTH:
        plane_Rect.right = SCREEN_WIDTH
    if plane_Rect.top < 0:
        plane_Rect.top = 0
    if plane_Rect.bottom > SCREEN_HEIGHT:
        plane_Rect.bottom = SCREEN_HEIGHT

