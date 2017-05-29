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

ellX = 200.0
ellY = 300.0
circleSize = 20
overCircle = False
locked = False
xOffSet = 0.0
yOffSet = 0.0

def setup():
    size (800, 500)
    ellX = width/8.0
    ellY = height/5.0
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
    if mouseX > ellX-circleSize and mouseX < ellX+circleSize and mouseY > ellY-circleSize and mouseY < ellY+circleSize:
        overCircle = True
        if not locked:
            cursor(HAND)
    else:
        overCircle = False
        cursor(ARROW)
        
    ellipse(ellX, ellY, circleSize, circleSize)
    
def mousePressed():
    if overCircle:
        locked = True
    else:
        locked = False
        
    xOffSet = mouseX - ellX
    yOffSet = mouseY - ellY

def mouseDragged():
    if locked:
        ellX = mouseX - xOffSet
        ellY = mouseY - yOffSet
        
def mouseReleased():
    locked = False
        