import pygame
from pygame.math import Vector2

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BALL_RADIUS = 20

class Ball:
  def __init__(self, screen, x, y):
    self.position = Vector2(x, y)
    self.velocity = Vector2(0, 0)
    self.screen = screen

  def move(self):
    self.velocity += Vector2(0, 9.81 * 0.01)
    self.position += self.velocity

    if self.position.y >= WINDOW_HEIGHT - BALL_RADIUS:
      self.velocity = Vector2(0, 0)
      self.position.y = WINDOW_HEIGHT - BALL_RADIUS

  def jump(self):
    self.velocity = Vector2(0, -2)

  def update(self):
    self.move()
    self.draw()

  def draw(self):
    pygame.draw.circle(self.screen, (255, 255, 255), self.position, BALL_RADIUS)

def main():
  pygame.init()
  screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

  ball = Ball(screen, WINDOW_WIDTH / 2, WINDOW_HEIGHT - BALL_RADIUS)

  def handleKeyDown(event):
    if event.key == 32: # space bar
      ball.jump()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return

      if event.type == pygame.KEYDOWN:
        handleKeyDown(event)

    screen.fill((0, 0, 0))
    ball.update()
    pygame.display.flip()

if __name__ == "__main__":
  main()
