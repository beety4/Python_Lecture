import pygame
import random

# 초기 설정
pygame.init()
clock = pygame.time.Clock()
SW = 800
SH = 800
status = 0
SCREEN = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Pac-Man")


# load map
maze = []
for i in range(SH):
    maze.append([0] * SW)

def make_maze():
    XP = [0,1,0,-1]
    YP = [-1,0,1,0]
    
    # 주변 벽
    for x in range(SW):
        maze[0][x] = 1
        maze[SW - 1][x] = 1
    for y in range(1,SH - 1):
        maze[y][0] = 1
        maze[y][SW - 1] = 1

    # 안을 아무것도 없는 상태로
    for y in range(1, SH - 1):
        for x in range(1, SW - 1):
            maze[y][x] = 0

    # 기둥
    for y in range(2, SH -2, 2):
        for x in range(2, SW - 2, 2):
            maze[y][x] = 1

    # 기둥에서 상화좌우 벽 생성
    for y in range(2, SH -2, 2):
        for x in range(2, SW - 2, 2):
            d = random.randint(0,3)
            if x > 2:
                d = random.randint(0,2)
            maze[y + YP[d]][x + XP[d]] = 1


# Player
player = pygame.image.load("img/player.png")
player = pygame.transform.scale(player, (25, 25))
player_Rect = player.get_rect()
player_Rect.centerx = 0
player_Rect.centery = 0
speed = 16
dx = 0
dy = 0


if __name__ == "__main__":
    playing = True
    make_maze()
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: dx = -speed
                if event.key == pygame.K_RIGHT: dx = speed
                if event.key == pygame.K_UP: dy = -speed
                if event.key == pygame.K_DOWN: dy = speed

                if event.key == pygame.K_KP_ENTER: status = 1
                if event.key == pygame.K_SPACE: make_maze()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: dx = 0
                if event.key == pygame.K_RIGHT: dx = 0
                if event.key == pygame.K_UP: dy = 0
                if event.key == pygame.K_DOWN: dy = 0


        # 게임상태 ( 0: 메인화면, 1: 게임화면, 2: 대기화면, 3: 탈락 )
        if status == 0:
            pass
        elif status == 1:
            pass



        # 배경 및 FPS 설정
        clock.tick(60)
        SCREEN.fill((0,0,0))

        # 화면 출력
        for y in range(SH):
            for x in range(SW):
                X = x * 25
                Y = y * 25
                if maze[y][x] == 0:
                    pygame.draw.rect(SCREEN, (144,143,234), [X, Y, 25, 25])
                if maze[y][x] == 1:
                    pygame.draw.rect(SCREEN, (14,124,34), [X, Y, 25, 25])


        SCREEN.blit(player, player_Rect)
        pygame.display.flip()


        # player 이동 및 Screen Out 방지
        player_Rect.x += dx
        player_Rect.y += dy
        if player_Rect.left < 0: player_Rect.left = 0
        if player_Rect.right > SW: player_Rect.right = SH
        if player_Rect.top < 0: player_Rect.top = 0
        if player_Rect.bottom > SH: player_Rect.bottom = SH


