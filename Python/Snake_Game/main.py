import pygame
import time
from snake import Snake
from food import Food

# font
pygame.font.init()

WIDTH = 800
HEIGHT = 800
SIZE = (WIDTH,HEIGHT)
SCREEN = pygame.display.set_mode(SIZE)
# title
pygame.display.set_caption("Snake Game by.: Mark Bakonyi")

# game
FPS = 5
FONT = pygame.font.SysFont('comicsans', 40)

# player
POINTS = 0
LOST = False

def update_screen(snake,food):
    SCREEN.fill((30,30,30))
    SCREEN.blit(FONT.render(f'Points: {snake.points}',1,(255,255,255)),(100,100))
    snake.update(SCREEN)
    food.update(SCREEN)

    if LOST:
        SCREEN.blit(FONT.render('Game Over', 1, (255, 255, 255)), (WIDTH / 2, HEIGHT / 2))

    pygame.display.update()

def main():
    run = True
    snake = Snake(SCREEN)
    food = Food(SCREEN)

    while run:
        time.sleep(0.1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.up()
                if event.key == pygame.K_LEFT:
                    snake.left()
                if event.key == pygame.K_DOWN:
                    snake.down()
                if event.key == pygame.K_RIGHT:
                    snake.right()

        run = snake.collision()
        food.collision(snake,SCREEN)
        snake.move()
        update_screen(snake,food)

        # game over loop
        if not run:
            sub_run = True
            cc = 0

            while sub_run:
                time.sleep(0.1)
                game_over_text = FONT.render('Game Over',1,(255,255,255))
                SCREEN.blit(game_over_text, ((WIDTH / 2)-game_over_text.get_width()+100, (HEIGHT/2)-game_over_text.get_height()-15))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()

                cc += 1
                print(cc)
                if cc >=60:
                    sub_run = False
                    pygame.quit()

                pygame.display.update()




if __name__ == '__main__':
    main()