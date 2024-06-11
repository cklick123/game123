
# import pgzrun
# import random
# import os 

# os.environ['SDL_VIDEO_CENTERED'] = '1'
# TITLE = "Project"
# WIDTH = 1000
# HEIGHT = 700
# street = Actor('busy_street_road' , (500,350))
# car = Actor('car_up' , (565, 600))
# over = Actor("over" , (495,415))
# police_car = Actor('police_car', (100, 400))

# speed = 5

# def update():
#     global speed 

    # print(f'car pos : {car.pos} car angle : {car.angle}')

#     if  610 <= car.x <= 965 and 765 >= car.y >= 435:
#         speed = 0 
#     elif -60 <= car.x <= 385 and 765 >= car.y >= 435:
#         speed = 0
#     elif -60 <= car.x <= 385 and 265 >= car.y >= -80:
#         speed = 0
#     elif 610 <= car.x <= 956 and 265 >= car.y >= -80:
#         speed = 0
         
#     if car.y <= -100 :
#         car.y = 800
#     elif car.y >= 800 :
#         car.y = -100
#     elif car.x <= -40 :
#         car.x = 1095
#     elif car.x >= 1100 :
#         car.x = -40
    # if keyboard.up :
    #     car.y -= speed
    # elif keyboard.down :
    #     car.y += speed
    # elif keyboard.right  :
    #     car.x += speed
    # elif keyboard.left :
    #     car.x -= speed

#     police_car.x += speed
#     if police_car.x >= 1200 :
#         police_car.x = -100 
#     if car.colliderect(police_car):
#         speed = 0
#     if keyboard.d :
#         police_car.flip_x  = True  
    
# def draw():
#     street.draw()
#     car.draw()
#     police_car.draw()
#     # if keyboard.right:
#     if car.colliderect(police_car):
#         over.draw()
#     if  610 <= car.x <= 965 and 765 >= car.y >= 435:
#         over.draw() 
#     if -60 <= car.x <= 385 and 765 >= car.y >= 435:
#         over.draw()
#     if -60 <= car.x <= 385 and 265 >= car.y >= -80:
#         over.draw()
#     if 610 <= car.x <= 956 and 265 >= car.y >= -80:
#         over.draw()
    

# pgzrun.go()

# ------------------------------------------------------------------

import pgzrun
import random
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
TITLE = "game"
WIDTH = 1000
HEIGHT = 600
back = Actor("rod")
mush = Actor("mush" , (400,400))
boom = Actor("boom" , (550,400))
coin = Actor("coin" , (25,18))
mirio = Actor("mirio" , (490,450))
box = Actor("box")
speed = 5
score = 0

def update():
    global speed
    global score 

    print(f'mirio pos : {mirio.pos}')
    if keyboard.up :
        sounds.coini.play()
    # if keyboard.up :
    #     score += 1
    if keyboard.up :
        mirio.y -= speed  
    elif keyboard.down :
        mirio.y += speed
    elif keyboard.right  :
        mirio.x += speed
    elif keyboard.left :
        mirio.x -= speed

def draw():
    back.draw() 
    mush.draw()
    boom.draw() 
    coin.draw()
    mirio.draw()
    screen.draw.text(f"{score}", color = "black" , topleft = (45,12))
    
pgzrun.go()

