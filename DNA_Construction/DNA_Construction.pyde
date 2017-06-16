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
class Circle():
    def __init__(self, centerX, centerY, radius):
        self.r = radius
        self.x = centerX
        self.y = centerY
    def overCircle(self):
        #cursor distance from circle centre is less than radius
        #distance from from cursor to centre of circle
        if sqrt((self.x-mouseX)**2 + (self.y-mouseY)**2)<self.r:
            return True
        else: 
            return False
    def locked(self):
        if mousePressed and self.overCircle():
            return True
        else:
            return False
    def drag(self):
        if mouseDragged and self.locked():
            self.x = mouseX
            self.y = mouseY

            
class Pentagon():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def overSugar(self):
        #radius of a pentagon with side length of 15
        radius = 12.75976
        if sqrt((self.x-mouseX)**2 + (self.y-mouseY)**2)<radius:
            return True
        else:
            return False
    def locked(self):
        if mousePressed and self.overSugar():
            return True
        else: 
            return False
    def drag(self):
        if mouseDragged and self.locked():
            self.x = mouseX
            self.y = mouseY
    
class Rectangle():
    def __init__(self, x, y, l, w):
        self.x = x
        self.y = y
        self.l = l
        self.w = w
    def overRect(self):
        if mouseX > (self.x - self.l/2) and mouseX < (self.x + self.l/2) and mouseY > (self.y-self.w/2) and mouseY < (self.y+self.w/2):
            return True
        else:
            return False
    def locked(self):
        if mousePressed and self.overRect():
            return True
        else: 
            return False
    def drag(self):
        if mouseDragged and self.locked():
            self.x = mouseX
            self.y = mouseY

#phosphate group
phosphate = Circle(200, 400, 10)
#Sugar molecule
sugar = Pentagon(375, 400)
#amino acid
amino = Rectangle(530, 400, 28, 13)
minutes = 0 


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
    distance = abs(sqrt((bx-ax)**2 + (by-ay)**2))
    if distance < 20:
        return True
    else:
        return False
   
def draw():
    global minutes
    background(255)
    fill(0)
    text("Phosphate", 175, 375)
    text("5-Carbon Sugar", 325, 375)
    text("Nitrogenous Base", 485, 375)
    #TIMER#
    millisecs = int(millis()/100)%10
    seconds = int(millis()/1000)%60
    if seconds >= 60:
        minutes+= 1
    s = "Time Elapsed: " + str(minutes) + ":" + str(seconds) + "." + str(millisecs)
    text(s, 600, 100)
    #if mouse over circle
    if phosphate.overCircle() or sugar.overSugar() or amino.overRect():
        cursor(HAND)
        if not phosphate.locked() or not sugar.locked() or not amino.locked():
            fill(100)
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
        
    if not lockA:
        rect(amino.x, amino.y, amino.l, amino.w)
        amino.drag()
    elif lockA:
        rect(sugar.x+30, sugar.y, amino.l, amino.w)
        sugar.drag()
    
def mouseDragged():
    " "
        