import pygame

from models import Spaceship, Asteroid
from utils import load_sprite, get_random_position

class SpaceRocks:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock() #allows for setting FPS

        self.asteroids = [
            Asteroid(get_random_position(self.screen)) for _ in range(6)
            ]
        self.spaceship = Spaceship((400, 300))

    def _get_game_objects(self):
        return [*self.asteroids, self.spaceship]


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
        
        is_key_pressed = pygame.key.get_pressed()

        if is_key_pressed[pygame.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.spaceship.rotate(clockwise=False)
        if is_key_pressed[pygame.K_UP]:
            self.spaceship.accelerate()

    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move(self.screen)

    def _draw(self):
        self.screen.blit(self.background, (0,0))

        for game_object in self._get_game_objects():
            game_object.draw(self.screen)


        pygame.display.flip()
        self.clock.tick(60) #fixes FPS to 60