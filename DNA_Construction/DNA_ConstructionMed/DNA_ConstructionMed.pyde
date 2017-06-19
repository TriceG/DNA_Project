from Shape_Classes import*

#phosphate group
phosphate = Circle(200, 400, 10)
#Sugar molecule
sugar = Pentagon(375, 400)
#amino acid
amino = Rectangle(530, 400, 28, 13)
minutes = 0 
start = True


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
s = ""
def draw():
    global minutes, start, s
    background(255)
    fill(0)
    text("Phosphate", 175, 375)
    text("5-Carbon Sugar", 325, 375)
    text("Nitrogenous Base", 485, 375)
    #TIMER#
    if start: 
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
    
    if lockP and lockA:
        start = False
        text(s, 100, 100)
    
def mouseDragged():
    " "