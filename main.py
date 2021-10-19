import pygame

class dvd_logo:
  def __init__(self, master, speed):
    self.master = master

    self.master_bounds = self.master.get_size()

    self.img = pygame.image.load("dvd.png").convert_alpha()
    self.img = pygame.transform.scale(self.img, (173,100)).convert_alpha()

    self.width = self.img.get_width()
    self.height = self.img.get_height()

    self.speed = speed
    self.x = 0
    self.y = 0
    self.x_vel = self.speed
    self.y_vel = self.speed

  def update(self):
    if self.x <= 0:
      self.x_vel = self.speed
    elif self.x >= self.master_bounds[0] - self.width:
      self.x_vel = -self.speed

    if self.y <= 0:
      self.y_vel = self.speed
    elif self.y >= self.master_bounds[1] - self.height:
      self.y_vel = -self.speed

    self.x += self.x_vel
    self.y += self.y_vel

    self.master.blit(self.img, (self.x, self.y))

def main_loop(tick_speed, logo_speed, size):
  root = pygame.display.set_mode((size))
  clock = pygame.time.Clock()
  dvd = dvd_logo(root, logo_speed)

  while 1:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    if keys[pygame.K_p]:
      while 1:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
          break

    root.fill((0,0,0))     
    dvd.update()
    clock.tick(tick_speed)
    pygame.display.update()

if __name__ == "__main__":
  main_loop(60, 1, (519, 300))
