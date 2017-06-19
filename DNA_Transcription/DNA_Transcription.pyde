import random
from Shape_Classes import*

page = 0

#phosphate group
phosphate = Circle(200, 400, 10)
#Sugar molecule
sugar = Pentagon(375, 400)
#amino acid
amino = Rectangle(530, 400, 28, 13)
minutes = 0 
d = 0

#declare nucleotides
A = ("Adenine")
T = ("Thymine")
C = ("Cytosine")
G = ("Guanine")
U = ("Uracil")

#put nucleotides into a list
nucleotide_list = [A, T, C, G, U]

#randomly select a nucleotide to be nucleotide_1 from the nucleotide_list
nucleotide_1 = random.choice(nucleotide_list)

#declare size of nucleotides
n1Size = 30
ASize = 30
TSize = 30
CSize = 30
GSize = 30
USize = 30
back_size = 60

#declare nucleotide colours
n1color = color(0,0,0)
Acolor = color(50,10,180)
Tcolor = color(100,180,100)
Ccolor = color(250,80,200)
Gcolor = color(250,140,40)
Ucolor = color(240,0,0)
backColor = color(0,0,0)

#declare mouse over booleans
overA = False
overT = False
overC = False
overG = False
overU = False

#declare correct/incorrect answer counts
correct = 0
incorrect = 0

def setup():
    size(800, 600)
    background(300)
    #noLoop()
    
    #declare default size and background
    size (800, 500)
    background (255)
    
    #nucleotide 1 position
    global n1X, n1Y
    n1X = width / 2 - n1Size - 10
    n1Y = height / 8 - n1Size / 2
    
    #back button position
    global backX, backY
    backX = width / 2.07 - ASize - 10
    backY = height / 1.5 - ASize / 2
    
    #nucleotide A position
    global AX, AY
    AX = width / 1.55 - ASize - 10
    AY = height / 2 - ASize / 2
    
    #nucleotide T position
    global TX, TY
    TX = width / 2 - TSize - 10
    TY = height / 2 - TSize / 2
    
    #nucleotide C position
    global CX, CY
    CX = width / 2.7 - CSize - 10
    CY = height / 2 - CSize / 2
    
    #nucleotide G position
    global GX, GY
    GX = width / 4 - GSize - 10
    GY = height / 2 - GSize / 2
    
    #nucleotide U position
    global UX, UY
    UX = width / 1.3 - USize - 10
    UY = height / 2 - USize / 2

def draw():
    global page
    if page == 0:   
        background(300) 
        display_page_num()
        ####### Draw code for Game_Selection_Page #######
        fill(0)
        textSize(48) 
        text('Select a Game', 225, 100)
        fill(247, 25, 226)
        rect(225, 200, 350, 75)
        fill(25, 197, 247)
        rect(250, 350, 300, 75)
        fill(0)
        text('DNA Structure', 235, 250)
        text('Base Pairs', 275, 400)
    elif page == 1:   
        background(300)
        size (800, 500)
        ellipseMode(CENTER)
        rectMode(CENTER)
        display_page_num()
        # put draw code here for dna construction page
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
            fill(0)
            text("Back", 40, 460)
        
    elif page == 2:
        background (200)
        display_page_num()
        # put draw code here for transcription page
        #make background slightly shaded
    
        #draw correct/incorrect counters
        fill(n1color)
        textSize(30)
        text("Correct: ", 480, 70)
        text(correct, 600, 70)
        text("Incorrect: ", 458, 100)
        text(incorrect, 600, 100)
    
        #Draws, colors, and names nucleotide_1
        stroke(255)
        fill(n1color)
        rect(n1X,n1Y,n1Size,n1Size)
        for n in nucleotide_list:
            if nucleotide_1 == A:
                textSize(30)
                text ("A", 365, 110)
            elif nucleotide_1 == T:
                textSize(30)
                text ("T", 365, 110)
            elif nucleotide_1 == C:
                textSize(30)
                text ("C", 365, 110)
            elif nucleotide_1 == G:
                textSize(30)
                text ("G", 365, 110)
            elif nucleotide_1 == U:
                textSize(30)
                text ("U", 365, 110)
    
        #Draws, colors, and names nucleotide A
        updateA(mouseX, mouseY)
        if overA:
            fill(Acolor)
        else:
            fill(Acolor)
        rect(AX,AY,ASize,ASize)
        textSize(30)
        text("A",482,230)
    
        #Draws, colors, and names nucleotide T
        updateT(mouseX, mouseY)
        if overT:
            fill(Tcolor)
        else:
            fill(Tcolor)
        rect(TX,TY,TSize,TSize)
        textSize(30)
        text("T",367,230)
    
        #Draws, colors, and names nucleotide C
        updateC(mouseX, mouseY)
        if overC:
            fill(Ccolor)
        else:
            fill(Ccolor)
        rect(CX,CY,CSize,CSize)
        textSize(30)
        text("C",260,230)
    
        #Draws, colors, and names nucleotide G
        updateG(mouseX, mouseY)
        if overG:
            fill(Gcolor)
        else:
            fill(Gcolor)
        rect(GX,GY,GSize,GSize)
        textSize(30)
        text("G",165,230)
    
        #Draws, colors, and names nucleotide U
        updateU(mouseX, mouseY)
        if overU:
            fill(Ucolor)
        else:
            fill(Ucolor)
        rect(UX,UY,USize,USize)
        textSize(30)
        text("U",580,230)
        
        #Draws back button, colors, and 'back' text
        updateBack(mouseX, mouseY)
        if overBack:
            fill(backColor)
        else:
            fill(backColor)
        rect(backX, backY, back_size, back_size)
        textSize(30)
        text("Back", 345, 405)
            
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

#Calculate the distance between two objects
def distance(ax, ay, bx, by):
    global d
    d = abs(sqrt((bx-ax)**2 + (by-ay)**2))
    if d < 20:
        return True
    else:
        return False    

#logic for back button
def checkBack(x, y, width, height): 
    return x <= mouseX <= x + width and y <= mouseY <= y + height

def updateBack(x, y):
    global overBack
    overBack = checkBack (backX, backY, back_size, back_size)
        
#logic for button checking of nucleotide A
def checkA (x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height

#Checks for mouse over nucleotide A
def updateA(x, y):
    global overA
    overA = checkA (AX,AY,ASize,ASize)
 
#logic for button checking of nucleotide T
def checkT (x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height

#Checks for mouse over nucleotide T
def updateT(x, y):
    global overT
    overT = checkT (TX,TY,TSize,TSize)

#logic for button checking of nucleotide C
def checkC (x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height
 
#Checks for mouse over nucleotide C
def updateC(x, y):
    global overC
    overC = checkC (CX,CY,CSize,CSize)

#logic for button checking of nucleotide G    
def checkG (x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height

#Checks for mouse over nucleotide G
def updateG(x, y):
    global overG
    overG = checkG (GX,GY,GSize,GSize)

#logic for button checking of nucleotide U    
def checkU (x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height

#Checks for mouse over nucleotide U
def updateU(x, y):
    global overU
    overU = checkU (UX,UY,USize,USize)

def display_page_num():
    global page
    textSize(20)
    fill(200)
    stroke(0)
    strokeWeight(1.5)
    text("Page #" + str(page), 10,580)
    
def mouseClicked():
    global page
    # If on page 0 (menu) and construction game button clicked, set the page to 1 (B's page)
    if page == 0 and mouseX > 225 and mouseX < 575 and mouseY >  200 and mouseY < 275:
        page = 1
    # If on page 0 (menu) and transcription game button clicked, set the page to 2 (M's page)
    elif page == 0 and mouseX > 250 and mouseX < 550 and mouseY > 350 and mouseY < 425:
        page = 2
    elif page == 1:
        # put mouse clicked code here for DNA constructiom
        pass
    elif page == 2:
        #mouse clicked code here for DNA pairs
        #declaring nucleotide_1, correct, and incorrect to be continuously used in mousePressed()
        global nucleotide_1
        global correct, incorrect
        
        #checks if user clicked A to match with T or U, correct += 1 or incorrect += 1, generates a new nucleotide either way
        if overA:
            if nucleotide_1 == T or nucleotide_1 == U:
                correct += 1
                nucleotide_1 = random.choice(nucleotide_list)
            else:
                incorrect += 1
                nucleotide_1 = random.choice(nucleotide_list)
                
        #checks if user clicked T to match with A, correct += 1 or incorrect += 1, generates a new nucleotide either way      
        elif overT:
            if nucleotide_1 == A:
                correct += 1
                nucleotide_1 = random.choice(nucleotide_list)
            else: 
                incorrect += 1 
                nucleotide_1 = random.choice(nucleotide_list)
                
        #checks if user clicked C to match with G, correct += 1 or incorrect += 1, generates a new nucleotide either way       
        elif overC:
            if nucleotide_1 == G:
                correct += 1
                nucleotide_1 = random.choice(nucleotide_list)
            else: 
                incorrect += 1
                nucleotide_1 = random.choice(nucleotide_list)
        
        #checks if user clicked G to match with C, correct += 1 or incorrect += 1, generates a new nucleotide either way        
        elif overG:
            if nucleotide_1 == C:
                correct += 1
                nucleotide_1 = random.choice(nucleotide_list)
            else: 
                incorrect += 1
                nucleotide_1 = random.choice(nucleotide_list)
        
        #checks if user clicked U to match with A, correct += 1 or incorrect += 1, generates a new nucleotide either way   
        elif overU:
            if nucleotide_1 == A:
                correct += 1
                nucleotide_1 = random.choice(nucleotide_list)
            else: 
                incorrect += 1
                nucleotide_1 = random.choice(nucleotide_list)
        elif overBack:
            page = 0
            correct = 0
            incorrect = 0
        pass
        
def mouseDragged():
    " " 