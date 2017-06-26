#!/usr/bin/python

import pygame
import time
import random

pygame.init()
width = 800
height = 600
car_width = 185
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('MrKat Racey')
clock = pygame.time.Clock()

#danceImg = pygame.image.load('racingCarOK.jpg')
#danceImg = pygame.image.load('racingCarOK1.png')
danceImg = pygame.image.load('KatRacingCar.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+ str(count), True, green)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def dance(x, y):
    gameDisplay.blit(danceImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 70)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2), (height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display('You crashed')

def game_loop():
    x = (width * 0.45)
    y = (height * 0.73)
    x_change = 0
    thing_startx = random.randrange(0, width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    gameExit = False
    dodged = 0
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        if (x < -3) and x_change < 0:
            x_change = 0
        elif (x > width - car_width) and x_change > 0:
            x_change = 0
        x += x_change
        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, blue)
        thing_starty += thing_speed 
        dance(x,y)
        things_dodged(dodged)
        if thing_starty > height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, width)
            things(thing_startx, thing_starty, thing_width, thing_height, blue)
            dodged += 1
            thing_speed += 1
        if (y < thing_starty + thing_height):
            if (x > thing_startx) and (x < thing_startx + thing_width) or \
               (x + car_width > thing_startx) and (x + car_width < thing_startx + thing_width):
                crash()
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
