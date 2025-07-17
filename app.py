import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 900
HEIGHT = 700
GRID_SIZE = 30
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Modern color palette
BACKGROUND = (15, 15, 25)
SNAKE_HEAD = (102, 255, 178)
SNAKE_BODY = (64, 224, 151)
SNAKE_TAIL = (32, 178, 117)
FOOD_COLOR = (255, 107, 107)
FOOD_GLOW = (255, 154, 154)
TEXT_COLOR = (220, 220, 220)
ACCENT_COLOR = (138, 43, 226)
GRID_COLOR = (25, 25, 35)
SHADOW_COLOR = (5, 5, 15)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Snake Game")

# Font setup
title_font = pygame.font.Font(None, 64)
game_font = pygame.font.Font(None, 48)
score_font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 24)

class Particle:
    def __init__(self, x, y, color, velocity, life):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = velocity
        self.life = life
        self.max_life = life
        self.size = random.randint(2, 5)
    
    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.life -= 1
        self.velocity = (self.velocity[0] * 0.98, self.velocity[1] * 0.98)
    
    def draw(self, screen):
        alpha = int(255 * (self.life / self.max_life))
        color = (*self.color, alpha)
        size = int(self.size * (self.life / self.max_life))
        if size > 0:
            pygame.draw.circle(screen, color[:3], (int(self.x), int(self.y)), size)

class Snake:
    def __init__(self):
        center_x = GRID_WIDTH // 2
        center_y = GRID_HEIGHT // 2
        self.body = [(center_x, center_y)]
        self.direction = [1, 0]
        self.grow = False
        self.animation_offset = 0
        self.last_move_time = 0
        self.move_delay = 150  # milliseconds
        
    def can_move(self):
        return time.time() * 1000 - self.last_move_time > self.move_delay
    
    def move(self):
        if not self.can_move():
            return True
            
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        
        # Check for wall collision
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            return False
            
        # Check for self collision
        if new_head in self.body[1:]:
            return False
            
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
            
        self.last_move_time = time.time() * 1000
        return True
    
    def set_direction(self, new_direction):
        # Prevent immediate reversal
        if (new_direction[0] * -1, new_direction[1] * -1) != tuple(self.direction):
            self.direction = new_direction

def draw_rounded_rect(surface, color, rect, radius):
    """Draw a rounded rectangle"""
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def draw_glow_effect(surface, color, center, radius):
    """Draw a glowing effect"""
    for i in range(radius, 0, -2):
        alpha = int(50 * (1 - i / radius))
        glow_color = (*color, alpha)
        pygame.draw.circle(surface, color, center, i)

def draw_grid(screen):
    """Draw a subtle grid"""
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y), 1)

def draw_snake(screen, snake, particles):
    """Draw the snake with modern effects"""
    for i, pos in enumerate(snake.body):
        x = pos[0] * GRID_SIZE
        y = pos[1] * GRID_SIZE
        
        # Create shadow effect
        shadow_rect = pygame.Rect(x + 2, y + 2, GRID_SIZE - 4, GRID_SIZE - 4)
        draw_rounded_rect(screen, SHADOW_COLOR, shadow_rect, 8)
        
        # Determine color based on position
        if i == 0:  # Head
            color = SNAKE_HEAD
            # Add pulsing effect
            pulse = int(20 * math.sin(time.time() * 5))
            color = (min(255, color[0] + pulse), min(255, color[1] + pulse), min(255, color[2] + pulse))
        else:
            # Gradient from body to tail
            factor = i / len(snake.body)
            color = (
                int(SNAKE_BODY[0] * (1 - factor) + SNAKE_TAIL[0] * factor),
                int(SNAKE_BODY[1] * (1 - factor) + SNAKE_TAIL[1] * factor),
                int(SNAKE_BODY[2] * (1 - factor) + SNAKE_TAIL[2] * factor)
            )
        
        # Main body segment
        rect = pygame.Rect(x, y, GRID_SIZE - 2, GRID_SIZE - 2)
        draw_rounded_rect(screen, color, rect, 10)
        
        # Add highlight
        highlight_rect = pygame.Rect(x + 4, y + 4, GRID_SIZE - 10, GRID_SIZE - 10)
        highlight_color = (min(255, color[0] + 30), min(255, color[1] + 30), min(255, color[2] + 30))
        draw_rounded_rect(screen, highlight_color, highlight_rect, 6)
        
        # Add particles for the head
        if i == 0 and random.random() < 0.3:
            particles.append(Particle(
                x + GRID_SIZE // 2 + random.randint(-5, 5),
                y + GRID_SIZE // 2 + random.randint(-5, 5),
                SNAKE_HEAD,
                (random.uniform(-1, 1), random.uniform(-1, 1)),
                30
            ))

def draw_food(screen, food_pos, particles):
    """Draw the food with glow effect"""
    x = food_pos[0] * GRID_SIZE
    y = food_pos[1] * GRID_SIZE
    
    # Pulsing glow effect
    pulse = math.sin(time.time() * 8) * 0.5 + 0.5
    glow_size = int(15 + pulse * 10)
    
    # Draw glow
    for i in range(glow_size, 0, -2):
        alpha = int(30 * (1 - i / glow_size))
        glow_color = FOOD_GLOW
        pygame.draw.circle(screen, glow_color, (x + GRID_SIZE // 2, y + GRID_SIZE // 2), i)
    
    # Draw shadow
    shadow_rect = pygame.Rect(x + 2, y + 2, GRID_SIZE - 4, GRID_SIZE - 4)
    draw_rounded_rect(screen, SHADOW_COLOR, shadow_rect, 12)
    
    # Draw main food
    food_rect = pygame.Rect(x + 3, y + 3, GRID_SIZE - 6, GRID_SIZE - 6)
    draw_rounded_rect(screen, FOOD_COLOR, food_rect, 12)
    
    # Add highlight
    highlight_rect = pygame.Rect(x + 6, y + 6, GRID_SIZE - 12, GRID_SIZE - 12)
    highlight_color = (min(255, FOOD_COLOR[0] + 50), min(255, FOOD_COLOR[1] + 50), min(255, FOOD_COLOR[2] + 50))
    draw_rounded_rect(screen, highlight_color, highlight_rect, 8)
    
    # Add sparkle particles
    if random.random() < 0.4:
        particles.append(Particle(
            x + GRID_SIZE // 2 + random.randint(-10, 10),
            y + GRID_SIZE // 2 + random.randint(-10, 10),
            FOOD_COLOR,
            (random.uniform(-2, 2), random.uniform(-2, 2)),
            40
        ))

def draw_ui(screen, score, high_score):
    """Draw the user interface"""
    # Score display
    score_text = score_font.render(f'Score: {score}', True, TEXT_COLOR)
    screen.blit(score_text, (20, 20))
    
    # High score display
    high_score_text = small_font.render(f'Best: {high_score}', True, ACCENT_COLOR)
    screen.blit(high_score_text, (20, 50))
    
    # Controls hint
    controls_text = small_font.render('Arrow Keys to move', True, (100, 100, 100))
    screen.blit(controls_text, (WIDTH - 150, HEIGHT - 30))

def draw_game_over(screen, score, high_score, particles):
    """Draw game over screen with effects"""
    # Semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill(BACKGROUND)
    screen.blit(overlay, (0, 0))
    
    # Game Over text with glow
    game_over_text = title_font.render('GAME OVER', True, TEXT_COLOR)
    game_over_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/2 - 80))
    
    # Add glow effect to text
    for offset in [(2, 2), (-2, -2), (2, -2), (-2, 2)]:
        glow_text = title_font.render('GAME OVER', True, ACCENT_COLOR)
        glow_rect = glow_text.get_rect(center=(WIDTH/2 + offset[0], HEIGHT/2 - 80 + offset[1]))
        screen.blit(glow_text, glow_rect)
    
    screen.blit(game_over_text, game_over_rect)
    
    # Score display
    score_text = game_font.render(f'Final Score: {score}', True, TEXT_COLOR)
    score_rect = score_text.get_rect(center=(WIDTH/2, HEIGHT/2 - 20))
    screen.blit(score_text, score_rect)
    
    # High score
    if score >= high_score:
        new_best_text = score_font.render('NEW BEST!', True, FOOD_COLOR)
        new_best_rect = new_best_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 20))
        screen.blit(new_best_text, new_best_rect)
    else:
        best_text = score_font.render(f'Best: {high_score}', True, ACCENT_COLOR)
        best_rect = best_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 20))
        screen.blit(best_text, best_rect)
    
    # Restart instruction
    restart_text = score_font.render('Press SPACE to restart', True, TEXT_COLOR)
    restart_rect = restart_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 80))
    screen.blit(restart_text, restart_rect)
    
    # Add explosion particles
    if len(particles) < 50:
        for _ in range(5):
            particles.append(Particle(
                WIDTH // 2 + random.randint(-100, 100),
                HEIGHT // 2 + random.randint(-100, 100),
                random.choice([FOOD_COLOR, SNAKE_HEAD, ACCENT_COLOR]),
                (random.uniform(-3, 3), random.uniform(-3, 3)),
                60
            ))

def create_food_particles(x, y, particles):
    """Create particles when food is eaten"""
    for _ in range(15):
        particles.append(Particle(
            x + random.randint(-15, 15),
            y + random.randint(-15, 15),
            random.choice([FOOD_COLOR, FOOD_GLOW, SNAKE_HEAD]),
            (random.uniform(-4, 4), random.uniform(-4, 4)),
            40
        ))

def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food_pos = None
    score = 0
    high_score = 0
    game_over = False
    particles = []
    
    # Load high score (in a real game, you'd save this to a file)
    # high_score = load_high_score()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_SPACE:
                        # Reset game
                        snake = Snake()
                        food_pos = None
                        score = 0
                        game_over = False
                        particles.clear()
                        continue
                else:
                    if event.key == pygame.K_UP:
                        snake.set_direction([0, -1])
                    elif event.key == pygame.K_DOWN:
                        snake.set_direction([0, 1])
                    elif event.key == pygame.K_LEFT:
                        snake.set_direction([-1, 0])
                    elif event.key == pygame.K_RIGHT:
                        snake.set_direction([1, 0])

        if not game_over:
            # Generate food
            if food_pos is None:
                food_pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
                while food_pos in snake.body:
                    food_pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))

            # Move snake
            if not snake.move():
                game_over = True
                high_score = max(high_score, score)
                continue

            # Check for food collision
            if snake.body[0] == food_pos:
                snake.grow = True
                food_x = food_pos[0] * GRID_SIZE + GRID_SIZE // 2
                food_y = food_pos[1] * GRID_SIZE + GRID_SIZE // 2
                create_food_particles(food_x, food_y, particles)
                food_pos = None
                score += 10
                # Increase speed slightly
                snake.move_delay = max(80, snake.move_delay - 2)

        # Draw everything
        screen.fill(BACKGROUND)
        draw_grid(screen)
        
        # Update and draw particles
        particles = [p for p in particles if p.life > 0]
        for particle in particles:
            particle.update()
            particle.draw(screen)
        
        if not game_over:
            draw_snake(screen, snake, particles)
            
            if food_pos:
                draw_food(screen, food_pos, particles)
            
            draw_ui(screen, score, high_score)
        else:
            draw_game_over(screen, score, high_score, particles)

        pygame.display.flip()
        clock.tick(60)  # Smooth 60 FPS

if __name__ == "__main__":
    main()
    pygame.quit()