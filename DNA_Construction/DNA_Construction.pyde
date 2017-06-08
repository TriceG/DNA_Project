#------------------------------
#
# Name: DNA_Construction
#
# Description: Game #1 - assembling DNA elements
# 
# Main Author: goyette.beatrice
#
# Collaborator: macduff.marchall
#
# Date: 29/05/2017
#
#------------------------------

# Make a class that creates dragable objects
class circle():
    
    def __init__(self, centerX, centerY, radius):
        self.r = radius
        self.x = centerX
        self.y = centerY
        
    def overCircle(self):
        #cursor distance from circle centre is less than radius
        #distance from from cursor to centre of circle
        if sqrt((self.x-mouseX)^2 + (self.y-mouseY)^2)<self.r:
            return True
        else: 
            return False
        
    #def drawCircle(self):
        #ellipse(centerX, centerY, radius)
    '''
    def locked(self):
        if mouseClicked and self.overCircle:
            return True
        else:
            return False
    '''


class Sugar():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def overSugar(self):
        #number of sides
        n = 5
        #formula for finding the radius
        radius = 15/(2*sin(180/n))
        if sqrt((self.x-mouseX)^2 + (self.y-mouseY)^2)<radius:
            return True
        else:
            return False
        
    
#phosphate group
phosphate = circle(200, 300, 10)
global ellX, ellY, circleSize, locked, overCircle, xOffSet, yOffSet
ellX = phosphate.x
ellY = phosphate.y
locked = False
xOffSet = 0.0
yOffSet = 0.0

#Sugar molecule
sugar = Sugar(400.0, 300.0)
sugarX = sugar.x
sugarY = sugar.y

    
def setup():
    size (800, 500)
    ellipseMode(CENTER)
   
#create a polygon with side length 15.
def sugarMol(x, y):
    beginShape()
    vertex(x-12.14, y-3.94)
    vertex(x, y-12.76)
    vertex(x+12.14, y-3.94)
    vertex(x+7.5, y+10.32)
    vertex(x-7.5, y+10.32)
    vertex(x-12.14, y-3.95)
    endShape()

#draw a DNA element
def DNAshape():
    beginShape()
    ellipseMode(CENTER)
    ellipse(400, 250, 20, 20)
    line(410, 260, 415, 265)
    vertex(415, 265)
    vertex(430, 255)
    vertex(445, 265)
    vertex(438, 280)
    vertex(422, 280)
    vertex(415, 265)
    line(445, 265, 455, 265)
    rectMode(CENTER)
    rect(469, 265, 28, 13)
    endShape() 
           
def draw():
    background(255)
    DNAshape()
    sugarMol(100, 100)
    global ellX, ellY, circleSize, locked, overCircle
    #if mouse over circle
    if phosphate.overCircle():
        #overCircle = True
        cursor(HAND)
        if not locked:
            fill(100)
    #if mouse not over circle
    else:
        #overCircle = False
        cursor(ARROW)
    
    #draw circle to be dragged
    ellipse(phosphate.x, phosphate.y, 2*phosphate.r, 2*phosphate.r)

#lock the button on the cursor when mouse is pressed    
def mousePressed():
    global ellX, ellY, locked, overCircle, xOffSet, yOffSet
    if phosphate.overCircle():
        locked = True
        stroke(0)
        fill(0)
    else:
        locked = False
        stroke(100)
        fill(100)
        
    xOffSet = mouseX - ellX
    yOffSet = mouseY - ellY

#change the circle position as mouse is dragged
def mouseDragged():
    global ellX, ellY, locked, xOffSet, yOffSet
    if locked:
        ellX = mouseX - xOffSet
        ellY = mouseY - yOffSet
        
#release the shape when mouse is released
def mouseReleased():
    global locked
    locked = False
        