import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 50
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (50, 168, 82)  # Softer green
RED = (220, 53, 69)    # Softer red
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)    # Background color
BLUE = (0, 123, 255)   # Score color

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Snake Game")

# Font setup
game_font = pygame.font.Font(None, 74)
score_font = pygame.font.Font(None, 36)

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = [1, 0]
        self.grow = False
        self.color = GREEN
        
    def move(self):
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
        return True

def draw_game_over(screen, score):
    screen.fill(GRAY)
    
    # Game Over text
    game_over_text = game_font.render('GAME OVER', True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
    screen.blit(game_over_text, game_over_rect)
    
    # Score text
    score_text = score_font.render(f'Final Score: {score}', True, WHITE)
    score_rect = score_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 20))
    screen.blit(score_text, score_rect)
    
    # Restart instruction
    restart_text = score_font.render('Press SPACE to restart', True, WHITE)
    restart_rect = restart_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 70))
    screen.blit(restart_text, restart_rect)
    
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food_pos = None
    score = 0
    game_over = False
    
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
                        continue
                else:
                    if event.key == pygame.K_UP and snake.direction != [0, 1]:
                        snake.direction = [0, -1]
                    elif event.key == pygame.K_DOWN and snake.direction != [0, -1]:
                        snake.direction = [0, 1]
                    elif event.key == pygame.K_LEFT and snake.direction != [1, 0]:
                        snake.direction = [-1, 0]
                    elif event.key == pygame.K_RIGHT and snake.direction != [-1, 0]:
                        snake.direction = [1, 0]

        if game_over:
            draw_game_over(screen, score)
            continue

        # Generate food
        if food_pos is None:
            food_pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
            while food_pos in snake.body:
                food_pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))

        # Move snake
        if not snake.move():
            game_over = True
            continue

        # Check for food collision
        if snake.body[0] == food_pos:
            snake.grow = True
            food_pos = None
            score += 10

        # Draw everything
        screen.fill(GRAY)
        
        # Draw snake with gradient effect
        for i, pos in enumerate(snake.body):
            color = (max(GREEN[0] - i*3, 20), 
                    max(GREEN[1] - i*3, 50), 
                    max(GREEN[2] - i*3, 20))
            pygame.draw.rect(screen, color, 
                           (pos[0]*GRID_SIZE, pos[1]*GRID_SIZE, 
                            GRID_SIZE-2, GRID_SIZE-2))

        # Draw food
        if food_pos:
            pygame.draw.rect(screen, RED, 
                           (food_pos[0]*GRID_SIZE, food_pos[1]*GRID_SIZE, 
                            GRID_SIZE-2, GRID_SIZE-2))

        # Draw score
        score_text = score_font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
    pygame.quit()