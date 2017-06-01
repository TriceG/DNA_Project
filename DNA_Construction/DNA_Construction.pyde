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

global ellX, ellY, circleSize, locked, overCircle, xOffSet, yOffSet
ellX = 200.0
ellY = 300.0
circleSize = 20
overCircle = 'false'
locked = 'false'
xOffSet = 0.0
yOffSet = 0.0

def setup():
    size (800, 500)
    ellX = width/2.0
    ellY = height/2.0
    ellipseMode(CENTER)

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
    DNAshape()
    #if mouse over circle
    if mouseX > ellX-circleSize and mouseX < ellX+circleSize and mouseY > ellY-circleSize and mouseY < ellY+circleSize:
        overCircle = 'true'
        cursor(HAND)
        if not locked:
            fill(100)
    #if mouse not over circle
    else:
        overCircle = 'false'
        cursor(ARROW)
    
    #draw circle to be dragged
    ellipse(ellX, ellY, circleSize, circleSize)

#lock the button on the cursor when mouse is pressed    
def mousePressed():
    if overCircle == 'true':
        locked = 'true'
        stroke(0)
    else:
        locked = 'false'
        stroke(100)
        
    xOffSet = mouseX - ellX
    yOffSet = mouseY - ellY

#change the circle position as mouse is dragged
def mouseDragged():
    if locked:
        ellX = mouseX - xOffSet
        ellY = mouseY - yOffSet
        
#release the shape when mouse is released
def mouseReleased():
    locked = 'false'
        