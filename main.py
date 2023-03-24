#Inport Library
import pygame
from sprites import *
pygame.init()

# Open Window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 15, 100)
paddleA.rect.x = 0
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 15, 100)
paddleB.rect.x = 685
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195
#List of Sprites used in game
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
#Loop Variable
gameLoop = True

#Screen Update Clock
clock = pygame.time.Clock()

#Initial Score
scoreA = 0
scoreB = 0

#Main Program Loop
while gameLoop:
    #Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    
    keys = pygame.key.get_pressed()
    #Paddle A keys
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    
    #Paddle B keys
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    #Game Logic
    all_sprites_list.update()

    if ball.rect.x >= 690:
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        all_sprites_list.draw(screen)
        scoreA += 1
        font = pygame.font.Font(None, 150)
        text = font.render(str(scoreA), 1, RED)
        font = pygame.font.Font(None, 74)
        screen.blit(text,(250,10))
        text = font.render(str(scoreB), 1, BLUE)
        screen.blit(text,(420,10))
        pygame.display.flip()
        ball.rect.x = 345
        ball.rect.y = 195
        pygame.time.delay(3000)
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        all_sprites_list.draw(screen)
        scoreB += 1
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, RED)
        screen.blit(text,(250,10))
        font = pygame.font.Font(None, 150)
        text = font.render(str(scoreB), 1, BLUE)
        screen.blit(text,(420,10))
        pygame.display.flip()
        ball.rect.x = 345
        ball.rect.y = 195
        pygame.time.delay(3000)
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    #Draw screen
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    all_sprites_list.draw(screen)

    #Scorboard
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, RED)
    screen.blit(text,(250,10))
    text = font.render(str(scoreB), 1, BLUE)
    screen.blit(text,(420,10))
    if scoreA > scoreB:
        ball.image.fill(RED)
    elif scoreB > scoreA:
        ball.image.fill(BLUE)
    else:
        ball.image.fill(WHITE)
    #Check For winner
    if scoreA == 10:
        font = pygame.font.Font(None, 112)
        text = font.render("Player A Won !!!", 1, RED)
        screen.blit(text,(80,195))
        pygame.display.flip()
        pygame.time.delay(5000)
        scoreA = 0
        scoreB = 0
        ball.rect.x = 345
        ball.rect.y = 195
        
    if scoreB == 10:
        font = pygame.font.Font(None, 112)
        text = font.render("Player B Won !!!", 1, BLUE)
        screen.blit(text,(80,195))
        pygame.display.flip()
        pygame.time.delay(5000)
        scoreA = 0
        scoreB = 0
        ball.rect.x = 345
        ball.rect.y = 195   

    pygame.display.flip()
    clock.tick(60)

pygame.quit()