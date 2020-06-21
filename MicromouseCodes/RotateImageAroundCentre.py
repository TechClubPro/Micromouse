"""
To Rotate Image around it's centre
"""

""" Import Lib"""
import pygame
import time
import rotateImage as rotator




""" Initialize Pygame"""
pygame.init()


""" Set the Dimension of the Screen"""
Width = 1000
Height = 560

""" Set the Screen"""

screen=pygame.display.set_mode((Width,Height))

""" Set The Title of Screen"""

pygame.display.set_caption("Rotate Image")

""" Load the Image"""
screenImg = pygame.image.load("Images/Background.png")

""" Display Image at Specific Co-Ordinate"""

screen.blit(screenImg,(0,0))


"""Load the Image to be Rotated"""
Image = pygame.image.load("Images/Stepper Motor Symbol.png")

EventStatus="None"
angle=0


while True:
             
    pygame.display.update()
    
    rotator.blitRotate(screen,Image,(100,100),angle)
    
    angle = angle-20
    time.sleep(1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            EventStatus="Quit"
            break
       
        
    if EventStatus == "Quit":
        break
    
print("Closing")