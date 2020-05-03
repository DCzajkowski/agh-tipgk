import pygame
from pygame.math import Vector2
from pygame.time import Clock

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BALL_RADIUS = 20
FPS = 120
PLATFORM_WIDTH = 100

class Ball:
  def __init__(self, screen, platforms, x, y):
    self.position = Vector2(x, y)
    self.velocity = Vector2(0, 0)
    self.platforms = platforms
    self.screen = screen

  def collide_with_walls(self):
    ball_bottom = pygame.Rect(self.position.x - BALL_RADIUS, self.position.y + BALL_RADIUS, BALL_RADIUS * 2, 1)

    z = self.platforms
    z = filter(lambda p: p.rect != None, z)
    z = map(lambda p: p.rect, z)
    z = list(z)

    if ball_bottom.collidelist(z) != -1 and self.velocity.y > 0:
      self.velocity = Vector2(0, 0)

  def move(self, dt):
    self.position += self.velocity * dt
    self.velocity += Vector2(0, 9.81 * 13) * dt

    if self.position.y >= WINDOW_HEIGHT - BALL_RADIUS:
      self.velocity = Vector2(0, 0)
      self.position.y = WINDOW_HEIGHT - BALL_RADIUS

  def jump(self):
    self.velocity = Vector2(0, -150)

  def update(self, dt):
    self.collide_with_walls()
    self.move(dt)
    self.draw()

  def draw(self):
    pygame.draw.circle(self.screen, (255, 255, 255), self.position, BALL_RADIUS)

class Platform:
  def __init__(self, screen, x, y):
    self.position = Vector2(x, y)
    self.screen = screen
    self.rect = None

  def update(self):
    self.draw()

  def draw(self):
    self.rect = pygame.draw.rect(self.screen, (255, 255, 255), (self.position.x, self.position.y, PLATFORM_WIDTH, 5))

def main():
  pygame.init()
  screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

  clock = Clock()

  platforms = [
    Platform(screen, WINDOW_WIDTH / 2 - PLATFORM_WIDTH / 2, 100),
    Platform(screen, WINDOW_WIDTH / 2 - PLATFORM_WIDTH / 2, 200),
    Platform(screen, WINDOW_WIDTH / 2 - PLATFORM_WIDTH / 2, 300),
    Platform(screen, WINDOW_WIDTH / 2 - PLATFORM_WIDTH / 2, 400),
  ]
  ball = Ball(screen, platforms, WINDOW_WIDTH / 2, WINDOW_HEIGHT - BALL_RADIUS)

  def handleKeyDown(event):
    if event.key == 32: # space bar
      ball.jump()

  while True:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return

      if event.type == pygame.KEYDOWN:
        handleKeyDown(event)

    screen.fill((0, 0, 0))
    ball.update(dt)
    for platform in platforms:
      platform.update()
    pygame.display.flip()

if __name__ == "__main__":
  main()
