
# Pygame Asteroids

This is a Pygame version of the classic game Asteroids, where you control a spaceship and shoot asteroids with bullets.

## Gameplay Screenshot
<img width="796" alt="Screenshot 2023-05-26 at 4 13 06 PM" src="https://github.com/pallas0/pygame_asteroids/assets/52135849/e18dae44-7eb3-4ed4-8123-e33ea646cd65">


## Installation

1. Clone the repository: `git clone https://github.com/YOUR-USERNAME/pygame-asteroids.git`
2. Navigate to the directory: `cd pygame-asteroids`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Start the game: `python3 space_rocks.py`
2. Use the arrow keys to move the spaceship.
3. Use the spacebar to shoot bullets.
4. Press 'r' to reset the game.
5. Press 'd' to toggle debug mode on/off.
6. Quit the game by closing the window or pressing the escape key.

## Gameplay

The game starts with six randomly placed asteroids. You must use your spaceship to shoot these asteroids and avoid colliding with them. If your spaceship collides with an asteroid, it will be destroyed and the game will end. Shooting an asteroid will cause it to split into smaller pieces, which can also be destroyed. The game continues until all asteroids are destroyed or the spaceship collides with one.

## Customization

You can customize the game by adjusting various settings in the `SpaceRocks` class:

- `MIN_ASTEROID_DISTANCE`: The minimum distance between asteroids and the spaceship when they are generated.
- `show_debug`: Whether or not to show debug information on the screen.

You can also customize the images used for the spaceship, asteroids, and background by replacing the corresponding image files in the `assets` directory.

## Acknowledgements

This game was created using the Pygame library and inspired by the classic game Asteroids. The code was adapted from a tutorial by [Real Python](https://realpython.com/pygame-a-primer/).

## License

This game is licensed under the [MIT License](LICENSE).
