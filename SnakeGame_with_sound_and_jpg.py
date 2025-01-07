# Snake Game
# In lines 36-38 please find sound and image option that can be loaded for effects.

import pygame, sys, random, time, pygame_menu

check_errors = pygame.init()

if check_errors[1] > 0:
    print("Had {0} errors, exiting...".format(check_errors[1]))
    sys.exit()
else:
    print("Game successfully initialized")

# Play surface
playsurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Leon eats - Snake Game')

# Colors
red = pygame.Color(255, 0, 0) #gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food

#FPS controller
fpsController = pygame.time.Clock()

# Important variables
snakePos = [100, 50]
snakeBody = [[100,50], [90,50], [80,50]]
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True
direction = 'RIGHT'
changeto = direction
score = 0
sound_mniam = pygame.mixer.Sound("C:\\Users\\Desktop\\Python\\other\\eats_sound.wav") # Sound played when snake eats - change to your favourite .wav file.
background = pygame.image.load("C:\\Users\\Desktop\\Python\\other\\background.jpg") # Background image - change to your favourite .jpg file.
background2 = pygame.image.load("C:\\Users\\Desktop\\Python\\other\\eats_image.jpg") # Image displayed when snake eats - change to your favourite .wav file.
time_to_blit = 0

#Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playsurface.blit(GOsurf,GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit() #game exit
    sys.exit() #console exit


def showScore(choice = 1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score: ' + str(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (40, 10)
    else:
        Srect.midtop = (360, 120)
    playsurface.blit(Ssurf, Srect)


# Game logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Below code updates snake position [x,y]
    if direction == 'RIGHT':
        snakePos[0] += 10 # we would get the same with "snakePos[0] = snakePos[0] + 10"
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # Snake body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
        playsurface.blit(background2, (150, 0))
        pygame.display.update()
        pygame.time.wait(1000)

    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
        pygame.mixer.Sound.play(sound_mniam,0)
        foodSpawn = True

    playsurface.fill(white)
    playsurface.blit(background, (160, 0))
    pygame.display.update()
    for pos in snakeBody:
        pygame.draw.rect(playsurface, green, pygame.Rect(pos[0],pos[1],10,10)) #snake body grafics

    pygame.draw.rect(playsurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10)) #food graphics and mechanism

    #boundaries
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    # hitting tail
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore()
    pygame.display.flip() # update screen function, should be at the end so all updates are visible
    fpsController.tick(14)
