import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
WHITE = (255,255,255)
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = (80,60)

YELLOW_SHIP_IMAGE = pygame.image.load(
    os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)

RED_SHIP_IMAGE = pygame.image.load(
    os.path.join('Assets','spaceship_red.png'))
RED_SHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), -90)

pygame.display.set_caption("My First Game!")

def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SHIP, (red.x, red.y))
    pygame.display.update()

def controller(key_pressed, red, yellow):
    if key_pressed[pygame.K_a]: red.x -= 4 
    if key_pressed[pygame.K_d]: red.x += 4
    if key_pressed[pygame.K_w]: red.y -= 4
    if key_pressed[pygame.K_s]: red.y += 4
    if key_pressed[pygame.K_LEFT]: yellow.x -= 4 
    if key_pressed[pygame.K_RIGHT]: yellow.x += 4
    if key_pressed[pygame.K_UP]: yellow.y -= 4
    if key_pressed[pygame.K_DOWN]: yellow.y += 4

def main():
    red = pygame.Rect(40, 230, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(800, 230, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()
        controller(key_pressed, red, yellow)

        draw_window(red, yellow)

    pygame.quit()

if __name__ == '__main__':
    main()