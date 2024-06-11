
# ------------------------------------------------------------------

import pgzrun
import random
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

TITLE = "game"
WIDTH = 1000
HEIGHT = 600
back = Actor("rod")
mush = Actor("mush" , (700 , 0))
mush1 = Actor("mush1" , (25,60))
boom = Actor("boom" , (400 , 0))
coin = Actor("coin" , (25,18))
coin1 = Actor("coin1" , (200 , 0))
mirio = Actor("mirio" , (520,450))
ghlb = Actor("ghlb" , (25 , 102))
over = Actor("over" , (480,350))
vic = Actor("vic" , (500 , 270))
chnc = "you must to collect 500 coins and 50 mushrooms to win"
speed = 5
score = 0
point = 1
lives = 5
deth = False
gameover = False
def update():
    global speed
    global score 
    global point
    global deth
    global gameover
    global lives
    
    print(f'mirio pos : {mirio.pos}')

    
    mush.y =  mush.y + 3 + point/10  
    boom.y = boom.y + 3 + point/10
    coin1.y = coin1.y + 3 + point/10


    if mush.y >= 485:
        mush.x = random.randint(139, 944)
        mush.y = 0
    if boom.y >= 485:
        boom.x = random.randint(139 , 944)
        boom.y = 0
    if coin1.y >= 485:
        coin1.x = random.randint(139 , 944)
        coin1.y = 0


    if mirio.x <= 59 :
       mirio.x = 59
    if mirio.x >= 944 :
        mirio.x = 944


    if keyboard.right  :
        mirio.x += speed
    if keyboard.left :
        mirio.x -= speed

    

    if mush.colliderect(mirio) :
        point += 1
        speed += 0.01
        mush.x = random.randint(139, 944)
        mush.y = 0
        
        sounds.point.play()
        
    elif boom.colliderect(mirio):
        boom.x = random.randint(139 , 944)
        boom.y = 0
        speed += 0.01
        lives -= 1
        sounds.bng.play()
    elif coin1.colliderect(mirio):
        score += 5
        coin1.x = random.randint(139 , 944)
        coin1.y = 0
        speed += 0.01
        sounds.point.play()
    


    if lives == 0 :
        gameover = True

    if gameover == True :
        boom.y = 0
        coin.y = 0
        mush1.y = 0
        if deth == False:
            sounds.over.play()
        deth = True


    
def draw():
    back.draw() 
    mush.draw()
    mush1.draw()
    boom.draw() 
    coin.draw()
    mirio.draw()
    coin1.draw()
    ghlb.draw()
    
    text1 = screen.draw.text(f"{score}", color = "black" , topleft = (45 , 9) , fontsize = 30)
    text2 = screen.draw.text(f"{point}" , color = "black" , topleft = (45 , 51) , fontsize = 30)
    text3 = screen.draw.text(chnc , color = ("white") , topleft = (220, 560) , fontsize = 30)
    text4 = screen.draw.text(f"{lives}" , color = ("black") , topleft = (45 , 92) , fontsize = 30)

    if gameover :
        screen.fill("black")
        text = screen.draw.text("Game Over", color = "white" , topleft = (120 , 150) , fontsize = 100 , fontname = "pixel")
        text1 = screen.draw.text(f"{score}", color = "white" , topleft = (340 , 333) , fontsize = 40 , fontname = "pixel")
        text2 = screen.draw.text(f"{point}" , color = "white" , topleft = (690 , 335) , fontsize = 40 , fontname = "pixel")
        coin1.draw()
        mush.draw()
        coin1.x = 300
        coin1.y = 350 
        mush.x = 650
        mush.y = 350
        
        
    if score >= 10 and point >= 1 :
        screen.fill("gold")
        victory_Text = screen.draw.text("Victory", color = "white" , topleft = (225 , 220) , fontsize = 100 , fontname = "pixel")
        boom.y = 0
        coin.y = 0
        mush1.y = 0



pgzrun.go()

# --------------------------------------------------------------
