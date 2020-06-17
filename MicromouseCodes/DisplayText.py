"""How to Display Text on Screen """

""" Import Lib"""
import pygame


""" Initialize Pygame"""
pygame.init()


""" Set the Dimension of the Screen"""
Width = 1000
Height = 560

""" Set the Screen"""

screen = pygame.display.set_mode((Width,Height))

""" Set The Title of Screen"""

pygame.display.set_caption("Display Text")

""" Load the Image"""
screenImg = pygame.image.load("Images/Background.png")

""" Display Image at Specific Co-Ordinate"""

screen.blit(screenImg,(0,0))



"""To Dispaly Text"""

font = pygame.font.SysFont("Eras Bold ITC",50)
text=font.render("My First Text",True,(255,0,0),(255,255,0))
screen.blit(text,(100,200))


""" Update the Display Continuously"""


EventStatus="None"


while True:
             
    pygame.display.update()
    
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            EventStatus="Quit"
            break
       
        
    if EventStatus == "Quit":
        break
    
print("Closing")
    