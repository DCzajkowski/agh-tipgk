import pygame
from pygame.math import Vector2

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

def main():
  pygame.init()
  screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

  while True:
    for event in pygame.event.get():
      pass

    screen.fill((0, 0, 0))
    pygame.display.flip()

if __name__ == "__main__":
  main()
