import pygame

from models import Spaceship, Asteroid
from utils import load_sprite, get_random_position

class SpaceRocks:
    MIN_ASTEROID_DISTANCE = 250
    show_debug = False
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock() #allows for setting FPS
        self.debug_surface = pygame.Surface((200, 100))
        self.debug_surface.fill((255, 255, 255))

        self.asteroids = []
        self.bullets = []
        self.spaceship = Spaceship((400, 300), self.bullets.append)

        self.asteroids_gen()

    
    def reset_game(self):
        self.asteroids = []
        self.bullets = []
        self.spaceship = Spaceship((400, 300), self.bullets.append)

        self.asteroids_gen()

    def asteroids_gen(self):
        for _ in range(6):
            while True:
                position = get_random_position(self.screen)
                if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
                ):
                    break
            self.asteroids.append(Asteroid(position, self.asteroids.append))

    def _get_game_objects(self):
        game_objects = [*self.asteroids, *self.bullets]

        if self.spaceship:
            game_objects.append(self.spaceship)
        
        return game_objects


    def main_loop(self): #game loop
        while True:
            self._handle_input()
            self._process_game_logic() #updates each frame
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
            elif (
                self.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.spaceship.shoot()
        
        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()

        if is_key_pressed[pygame.K_r]:
            self.reset_game()
        
        if is_key_pressed[pygame.K_d]:
            self.show_debug = not self.show_debug


    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move(self.screen)

        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None
                    break

        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.split()
                    break
        
        for bullet in self.bullets[:]:
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)

    def _draw(self):
        self.screen.blit(self.background, (0,0))

        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        if self.show_debug:
            self.screen.blit(self.debug_surface, (600, 0))


        pygame.display.flip()
        self.clock.tick(60) #fixes FPS to 60