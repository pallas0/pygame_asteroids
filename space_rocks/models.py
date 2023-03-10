from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_sprite, wrap_position, get_random_velocity

UP = Vector2(0, -1)

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius) #Vector2 will use this number for both values
        surface.blit(self.sprite, blit_position)
    
    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)
    
    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius
    
    
class Spaceship(GameObject):
    MANEUVERABILITY = 3 #determines how fast sprite can rotate
    ACCELERATION = 0.25
    BULLET_SPEED = 3

    def __init__(self, position, create_bullet_callback):
        self.create_bullet_callback = create_bullet_callback
        self.direction = Vector2(UP) #copy of original UP vector

        super().__init__(position, load_sprite("spaceship"), Vector2(0))

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)
    
    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION
    
    def shoot(self):
        bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
        bullet = Bullet(self.position, bullet_velocity)
        self.create_bullet_callback(bullet)

    def draw(self, surface):
        angle = self.direction.angle_to(UP) #calculates angle by which one vector needs to be rotated to point in same direction as other vector
        rotated_surface = rotozoom(self.sprite, angle, 1.0) #rotates the sprite
        rotated_surface_size = Vector2(rotated_surface.get_size()) #recalculate blit position
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

class Asteroid(GameObject):
    def __init__(self, position, create_asteroid_callack, size=3):
        self.create_asteroid_callback = create_asteroid_callack
        self.size = size

        size_to_scale = {
            3: 1,
            2: 0.5,
            1: 0.25,
        }

        scale = size_to_scale[size]
        sprite = rotozoom(load_sprite("asteroid"), 0, scale)

        super().__init__(
            position, load_sprite("asteroid"), get_random_velocity(1, 3))
    
    def split(self):
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroid(
                    self.position, self.create_asteroid_callback, self.size - 1
                )
                self.create_asteroid_callback(asteroid)

class Bullet(GameObject):
    def __init__(self, position, velocity):
        super().__init__(position, load_sprite("bullet"), velocity)
    
    def move(self, surface):
        self.position = self.position + self.velocity
    
