import pygame
import os

from player import Player
from world import Ground
from world import Sky
from inventory import Inventory

from camera import *

################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 1000, 800
canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W, DISPLAY_H)))
clock = pygame.time.Clock()
TARGET_FPS = 60




def main():
    run = True
    """
    * CHARACTERS *
    """
    player = Player()
    """
    * CAMERA *
    """

    """
        * WORLD *
    """
    ground = Ground()
    sky = Sky()
    """
        * Inventory *
    """
    inventor = Inventory()


    clock = pygame.time.Clock()

    while run:
        dt = clock.tick(60) * .001 * TARGET_FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.LEFT_KEY, player.FACING_LEFT = True, True
                elif event.key == pygame.K_d:
                    player.RIGHT_KEY, player.FACING_LEFT = True, False
                elif event.key == pygame.K_w:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.LEFT_KEY = False
                if event.key == pygame.K_d:
                    player.RIGHT_KEY = False
                if event.key == pygame.K_w:
                    if player.is_jumping:
                        player.velocity.y *= .25
                        player.is_jumping = False

        player.update(dt, canvas)
        canvas.fill((135, 206, 235))


        player.draw(canvas)
        ground.draw(canvas)
        sky.draw(canvas)
        inventor.draw(canvas)


        window.blit(canvas, (0, 0))
        pygame.display.update()


main()
