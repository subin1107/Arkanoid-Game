import pygame
import random

# 게임 화면 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arkanoid Game")

clock = pygame.time.Clock()

# 공, 야구 선수 이미지 로드
ball_image = pygame.image.load("ball.png")
player_image = pygame.image.load("player.png")

# 공 크기와 속도
BALL_RADIUS = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = -3

# 야구 선수 크기
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 20

# 벽돌 크기
BRICK_WIDTH = 60
BRICK_HEIGHT = 40

# 게임 시작
def run_game():
    player_rect = player_image.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 10))
    ball_rect = ball_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    ball_dx = BALL_SPEED_X
    ball_dy = BALL_SPEED_Y

    bricks = []
    brick_colors = [(255, 0, 0)] # 벽돌 생각은 빨간색

    for row in range(5):
        for col in range(10):
            brick_x = 70 + col * (BRICK_WIDTH + 5)
            brick_y = 50 + row * (BRICK_HEIGHT + 5)
            brick_color = brick_colors[0]  # 빨간색으로 통일
            brick_rect = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
            bricks.append({"rect": brick_rect, "color": brick_color})

    score = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.left -= 5
            if player_rect.left < 0:
                player_rect.left = 0
        if keys[pygame.K_RIGHT]:
            player_rect.right += 5
            if player_rect.right > SCREEN_WIDTH:
                player_rect.right = SCREEN_WIDTH

        # 공 이동
        ball_rect.x += ball_dx
        ball_rect.y += ball_dy

    
        if ball_rect.left <= 0 or ball_rect.right >= SCREEN_WIDTH:
            ball_dx *= -1
        if ball_rect.top <= 0:
            ball_dy *= -1
        if ball_rect.colliderect(player_rect):
            ball_dy *= -1

        for brick in bricks:
            if brick["rect"].colliderect(ball_rect):
                brick["rect"].y = -200
                ball_dy *= -1
                score += 1

        # 게임 오버 체크
        if ball_rect.bottom >= SCREEN_HEIGHT:
            game_over = True

        screen.fill((0, 0, 0))

        # 벽돌 그리기
        for brick in bricks:
            pygame.draw.rect(screen, brick["color"], brick["rect"])

        # 선수 그리기
        screen.blit(player_image, player_rect)

        # 공 그리기
        screen.blit(ball_image, ball_rect)

        # score 표시
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    # 게임 끝날 시 game over 출력
    font = pygame.font.Font(None, 48)
    game_over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) // 2, (SCREEN_HEIGHT - game_over_text.get_height()) // 2))

    pygame.display.flip()
    pygame.time.wait(2000) 

    pygame.quit() # 게임 종료


run_game()
