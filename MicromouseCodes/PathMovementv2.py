"""
Program for Path Movement with step simulator
"""

"""
Taking path input from user

User Input Format:
    
    Straight - Number of Cells
    Left Turn - L
    Right Turn - R
    End of Path - x
    
    Direction Nomenclature:
        East - 1
        North - 2
        West - 3
        South - 4
        
Bot is Initially at Cell 1 , Facing South Direction.

Turns and Movements would be decided according 
to the path entered by user with reference to the
Initial Position of the Bot.




        
    
    
"""

""" Import Lib"""
import pygame
import rotateImage as rotator
import time


""" Initialize Pygame"""
pygame.init()


""" Set the Dimension of the Screen"""
Width = 483
Height = 484

""" Set the Screen"""

screen = pygame.display.set_mode((Width,Height))

""" Set The Title of Screen"""

pygame.display.set_caption("Display Text")

""" Load the Image"""
screenImg = pygame.image.load("Images/MicroMouse Grid.jpg")

""" Display Image at Specific Co-Ordinate"""

screen.blit(screenImg,(0,0))


"""Load the Bot Image"""
botImg= pygame.image.load("Images/Grid BOt.png")
# screen.blit(botImg,(15,15))
rotator.blitRotate(screen,botImg,(15,15),180)

path=[]

pathInput = ""

stepNum=1

currentAngle=180
currentDirection=4
state=""
steps=0
cellX=15
cellY=15

def decideAngle(turn,currentAngle):
    global currentDirection
    
    if turn=="L":
        currentAngle=currentAngle+90
        
        if currentDirection==4:
            currentDirection=1
        else:
            currentDirection=currentDirection+1
        
    elif turn=="R":
        currentAngle=currentAngle-90
        if currentDirection==1:
            currentDirection=4
        else:
            currentDirection=currentDirection-1
        
    return currentAngle,currentDirection

def UpdateBackground():
    """ Set the Dimension of the Screen"""
    Width = 483
    Height = 484
    
    """ Set the Screen"""
    
    screen = pygame.display.set_mode((Width,Height))
    
    """ Set The Title of Screen"""
    
    pygame.display.set_caption("Display Text")
    
    """ Load the Image"""
    screenImg = pygame.image.load("Images/MicroMouse Grid.jpg")
    
    """ Display Image at Specific Co-Ordinate"""
    
    screen.blit(screenImg,(0,0))
    
def Move(angle,cellX,cellY):
    UpdateBackground()
    
    
    """Load the Bot Image"""
    botImg= pygame.image.load("Images/Grid BOt.png")
    # screen.blit(botImg,(15,15))
    rotator.blitRotate(screen,botImg,(cellX,cellY),angle)

def getCoordinates(steps,cellX,cellY,currentDirection,currentAngle):
    
    if steps==0:
        if currentDirection==1:
            cellX=cellX+(steps*30)
        if currentDirection==2:
            cellY=cellY-(steps*30)
        if currentDirection==3:
            cellX=cellX-(steps*30)
        if currentDirection==4:
            cellY=cellY+(steps*30)
        Move(currentAngle,cellX,cellY)
              
    else:
        for i in range (steps):
            time.sleep(1)
            print("Taking Step ", i)
            if currentDirection==1:
                cellX=cellX+(30)
                Move(currentAngle,cellX,cellY)
            if currentDirection==2:
                cellY=cellY-(30)
                Move(currentAngle,cellX,cellY)
            if currentDirection==3:
                cellX=cellX-(30)
                Move(currentAngle,cellX,cellY)
            if currentDirection==4:
                cellY=cellY+(30)
                Move(currentAngle,cellX,cellY)
            pygame.display.update()
             
            
    return cellX,cellY
        
        

def parsePath(element,currentAngle):
    global state
    global steps
    global currentDirection
    global cellX
    global cellY
    
    
   #Check each element in the List
    if element =="L":
        
       currentAngle,currentDirection= decideAngle("L",currentAngle)
       steps=0
       cellX,cellY=getCoordinates(steps,cellX,cellY,currentDirection,currentAngle)
       state="NotReached"
       print("Taking Left Turn with angle ", currentAngle)
       
    elif element =="R":
       currentAngle,currentDirection= decideAngle("R",currentAngle)
       steps=0
       cellX,cellY=getCoordinates(steps,cellX,cellY,currentDirection,currentAngle)
       state="NotReached"
       print("Taking Right Turn with angle ", currentAngle)
      
    elif element=='x':
        state="Reached"
        
    else:
        steps=int(element)
        print("currentAngle ",currentAngle)
        cellX,cellY=getCoordinates(steps,cellX,cellY,currentDirection,currentAngle)
        
        state="NotReached" 
        

       
    return state,currentAngle    
            

while pathInput!='x':
    pathInput=input("Enter the Path Step "+ str(stepNum))
    stepNum+=1
    path.append(pathInput)


while state !="Reached" :
    # pygame.display.update()
    for element in path:
        pygame.display.update()
        state,currentAngle=parsePath(element,currentAngle)
        time.sleep(2)

        if state=="Reached":
    
            time.sleep(5)
            print("closing")
            pygame.quit()
    
        time.sleep(1)
