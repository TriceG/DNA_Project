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

from Shape_Classes import*

#phosphate group
phosphate = Circle(200, 400, 10)
#Sugar molecule
sugar = Pentagon(375, 400)
#amino acid
amino = Rectangle(530, 400, 28, 13)
minutes = 0 
d = 0


def setup():
    size (800, 500)
    ellipseMode(CENTER)
    rectMode(CENTER)
   
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


def distance(ax, ay, bx, by):
    global d
    d = abs(sqrt((bx-ax)**2 + (by-ay)**2))
    if d < 20:
        return True
    else:
        return False
   
def draw():
    global minutes, distance
    background(255)
    fill(0)
    textSize(15)
    text("Phosphate", 165, 375)
    text("5-Carbon Sugar", 315, 375)
    text("Nitrogenous Base", 485, 375)
    #if mouse over circle
    fill(0, 0, 255, 255-d)
    if phosphate.overCircle() or sugar.overSugar() or amino.overRect():
        cursor(HAND)
        if not phosphate.locked() or not sugar.locked() or not amino.locked():
            fill(0, 0, 255, 255-d)
    #if mouse not over circle
    else:
        cursor(ARROW)
    #draw shapes to be dragged
    sugarMol(sugar.x, sugar.y)
    if distance(sugar.x, sugar.y, phosphate.x, phosphate.y):
        lockP = True
        phosphate.x = sugar.x
        phosphate.y = sugar.y
    else:
        lockP = False
    fill(0, 0, 255, 255-d)
    
    if not lockP:
        ellipse(phosphate.x, phosphate.y, 2*phosphate.r, 2*phosphate.r)
        phosphate.drag()
        sugar.drag()
    elif lockP:
        ellipse(sugar.x-20, sugar.y-20, 2*phosphate.r, 2*phosphate.r)
        sugar.drag()
        
    if distance(sugar.x, sugar.y, amino.x, amino.y):
        lockA = True
        amino.x = sugar.x
        amino.y = sugar.y
    else:
        lockA = False
    fill(0, 0, 255, 255-d)
        
    if not lockA:
        rect(amino.x, amino.y, amino.l, amino.w)
        amino.drag()
    elif lockA:
        rect(sugar.x+30, sugar.y, amino.l, amino.w)
        sugar.drag()
        
    if lockP and lockA:
        fill(53, 10, 250)
        textSize(30)
        text("You Got It!!!", 300, 100)
        fill(238, 18, 255)
        rect(75, 450, 75, 45)
        #Next Level button
        rect(700, 450, 160, 45)
        fill(0)
        text("Back", 40, 460)
        text("Next Level", 625, 460)
        
    if mouseX > 37.5 and mouseX < 112.5 and mouseY > 427.5 and mouseY < 572.5:
        cursor(HAND)
    elif mouseX > 620 and mouseX < 780 and mouseY > 427.5 and mouseY < 572.5:
        cursor(HAND)
    else:
        cursor(ARROW)

        
    
def mouseDragged():
    " "
        