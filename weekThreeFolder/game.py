import pygame
import random
import math


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("oop")
clock = pygame.time.Clock()


class Shape:
    def __init__(self, x, y, vx=None, vy=None):
        self.__x = x
        self.__y = y
        if vx is not None and vy is not None:
            self.vx = vx
            self.vy = vy
        else:
            self.vx = random.uniform(-2, 2)
            self.vy = random.uniform(-2, 2)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def update(self):
        self.__x += self.vx
        self.__y += self.vy
        self._wrap_screen()

    def _wrap_screen(self):
        if self.__x < 0:
            self.__x = WIDTH
        elif self.__x > WIDTH:
            self.__x = 0
        if self.__y < 0:
            self.__y = HEIGHT
        elif self.__y > HEIGHT:
            self.__y = 0

    def draw(self, screen):
        pass


class Ship(Shape):
    def __init__(self, x, y):
        super().__init__(x, y, vx=0, vy=0)
        self.angle = 0
        self.radius = 15

    def rotate(self, direction):
        self.angle += direction * 5

    def thrust(self):
        angle_rad = math.radians(self.angle)
        self.vx += math.cos(angle_rad) * 0.3
        self.vy += math.sin(angle_rad) * 0.3

    def update(self):
        super().update()
        # Apply friction
        self.vx *= 0.98
        self.vy *= 0.98

    def draw(self, screen):
        points = []
        for angle_offset in [0, 140, 220]:
            angle = math.radians(self.angle + angle_offset)
            px = self.get_x() + math.cos(angle) * self.radius
            py = self.get_y() + math.sin(angle) * self.radius
            points.append((px, py))
        pygame.draw.polygon(screen, (255, 255, 255), points, 2)

    def shoot(self):
        angle_rad = math.radians(self.angle)
        bullet_x = self.get_x() + math.cos(angle_rad) * self.radius
        bullet_y = self.get_y() + math.sin(angle_rad) * self.radius
        bullet_vx = math.cos(angle_rad) * 8 + self.vx
        bullet_vy = math.sin(angle_rad) * 8 + self.vy
        return Bullet(bullet_x, bullet_y, bullet_vx, bullet_vy)


class Bullet(Shape):
    def __init__(self, x, y, vx, vy):
        super().__init__(x, y, vx, vy)
        self.life = 60

    def update(self):
        super().update()
        self.life -= 1

    def is_alive(self):
        return self.life > 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.get_x()), int(self.get_y())), 2)


class Asteroid(Shape):
    def __init__(self, x, y, size):
        vx = random.uniform(-2, 2)
        vy = random.uniform(-2, 2)
        super().__init__(x, y, vx, vy)
        self.size = size
        self.radius = size * 15
        self.flash_timer = 0
        self.pending_split = False 

    # def draw(self, screen):
    #     pygame.draw.circle(screen, (255, 255, 255), (int(self.get_x()), int(self.get_y())), self.radius, 2)
    def draw(self, screen):
        x = int(self.get_x())
        y = int(self.get_y())

        # face color (red while hit)
        face_color = (255, 255, 0) if self.flash_timer <= 0 else (255, 100, 100)
        pygame.draw.circle(screen, face_color, (x, y), self.radius)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), self.radius, 2)

        # eyes
        eye_offset_x = self.radius // 3
        eye_offset_y = self.radius // 3
        eye_radius = max(2, self.radius // 6)
        pygame.draw.circle(screen, (0, 0, 0), (x - eye_offset_x, y - eye_offset_y), eye_radius)
        pygame.draw.circle(screen, (0, 0, 0), (x + eye_offset_x, y - eye_offset_y), eye_radius)

        # smile or frown depending on flash_timer
        mouth_rect = pygame.Rect(x - self.radius // 2, y, self.radius, self.radius // 2)
        if self.flash_timer <= 0:
            # normal happy smile 🙂
            # upside-down frown 🙁
            frown_rect = pygame.Rect(x - self.radius // 2, y - self.radius // 2, self.radius, self.radius // 2)
            pygame.draw.arc(screen, (0, 0, 0), frown_rect, math.radians(200), math.radians(340), 2)

            # pygame.draw.arc(screen, (0, 0, 0), mouth_rect, math.radians(20), math.radians(160), 2)
        else:
            # upside-down frown 🙁
            # frown_rect = pygame.Rect(x - self.radius // 2, y - self.radius // 2, self.radius, self.radius // 2)
            # pygame.draw.arc(screen, (0, 0, 0), frown_rect, math.radians(200), math.radians(340), 2)
            pygame.draw.arc(screen, (0, 0, 0), mouth_rect, math.radians(20), math.radians(160), 2)

        def update(self):
            super().update()
            if self.flash_timer > 0:
                self.flash_timer -= 1



    def split(self):
        if self.size > 1:
            return [
                Asteroid(self.get_x(), self.get_y(), self.size - 1),
                Asteroid(self.get_x(), self.get_y(), self.size - 1),
                Asteroid(self.get_x(), self.get_y(), self.size - 1),
                Asteroid(self.get_x(), self.get_y(), self.size - 1)
            ]
        return []

    def collides_with(self, other_x, other_y, other_radius):
        distance = math.sqrt((self.get_x() - other_x)**2 + (self.get_y() - other_y)**2)
        return distance < (self.radius + other_radius)


ship = Ship(WIDTH // 2, HEIGHT // 2)
bullets = []
asteroids = [
    Asteroid(100, 100, 3),
    Asteroid(100, 100, 3),
    Asteroid(700, 100, 3),
    Asteroid(400, 500, 3),
    Asteroid(400, 500, 3),
]

score = 0
running = True

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(ship.shoot())

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.rotate(-1)
    if keys[pygame.K_RIGHT]:
        ship.rotate(1)
    if keys[pygame.K_UP]:
        ship.thrust()

    ship.update()

    for bullet in bullets:
        bullet.update()

    for asteroid in asteroids:
        asteroid.update()

    bullets = [b for b in bullets if b.is_alive()]

    # new_asteroids = []
    # for asteroid in asteroids[:]:
    #     hit = False
    #     for bullet in bullets[:]:
    #         if asteroid.collides_with(bullet.get_x(), bullet.get_y(), 2):
    #             hit = True
    #             bullets.remove(bullet)
    #             score += (4 - asteroid.size) * 10
    #             new_asteroids.extend(asteroid.split())
    #             break

    #     if hit:
    #         asteroids.remove(asteroid)

    # asteroids.extend(new_asteroids)

        # Check for bullet–asteroid collisions
    for asteroid in asteroids:
        for bullet in bullets[:]:
            if asteroid.collides_with(bullet.get_x(), bullet.get_y(), 2):
                bullets.remove(bullet)
                asteroid.flash_timer = 15       # make it frown & flash red
                asteroid.pending_split = True   # delay splitting until frown ends
                score += (4 - asteroid.size) * 10
                break  # stop checking this asteroid for more bullets
    

    for asteroid in asteroids:
        if asteroid.collides_with(ship.get_x(), ship.get_y(), ship.radius):
            print(f"Game Over! Final Score: {score}")
            running = False

    screen.fill((0, 0, 0))

    ship.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    for asteroid in asteroids:
        asteroid.draw(screen)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if len(asteroids) == 0:
        win_text = font.render("You Win! Press ESC to exit", True, (255, 255, 255))
        screen.blit(win_text, (WIDTH // 2 - 150, HEIGHT // 2))

    pygame.display.flip()

pygame.quit()

