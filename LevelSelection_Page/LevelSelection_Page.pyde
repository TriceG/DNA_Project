def setup():
    background(37, 154, 247)
    size(800, 500)
    
def draw():
    fill(225)
    rectMode(CENTER)
    #beginerButton
    rect(400, 175, 150, 50)
    #intermediateButton
    rect(400, 275, 239, 50)
    #advancedButton
    rect(400, 375, 190, 50)
    textSize(30)
    #title
    text("Select a Level:", 300, 100)
    fill(0)
    #button text
    text("BEGINER", 337, 185)
    text("INTERMEDIATE", 292, 285)
    text("ADVANCED", 316, 385)

def mouseClicked():
    #BEGINER button clicked
    if mouseX > 325 and mouseX < 475 and mouseY > 150 and mouseY < 200:
        #go to easy mode
        #Import Easy Mode
        background(194, 247, 37)
    #INTERMEDIATE button clicked
    if mouseX > 280.5 and mouseX < 519.5 and mouseY > 250 and mouseY < 300:
        #go to medium mode
        #Import Medium mode
        background(47, 247, 37)
    #ADVANCED button clicked
    if mouseX > 305 and mouseX < 495 and mouseY > 350 and mouseY < 400:
        #go to hard mode
        #Import Hard Mode
        background(27, 167, 20)