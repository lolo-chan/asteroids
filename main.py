import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    Player.containers = (group_updatable, group_drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    group_asteroids = pygame.sprite.Group()
    Asteroid.containers = (group_asteroids, group_drawable, group_updatable)

    AsteroidField.containers = (group_updatable)
    asteroidField = AsteroidField()

    group_shots = pygame.sprite.Group()
    Shot.containers = (group_shots, group_updatable, group_drawable)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        group_updatable.update(dt)
        for i in group_asteroids:
            if player.collision(i):
                print("Game over!")
                sys.exit()
        screen.fill((0, 0, 0))
        
        for i in group_drawable:
            i.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()