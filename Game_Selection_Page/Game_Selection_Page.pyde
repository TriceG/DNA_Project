#-------------------------------
#
# Name: Game_Selection_Page.pyde
#
# Purpose: Allow the user to choose between the two mini games
#
# Author: Goyette.Beatrice
#
# Collaborator: Macduff.Marshall
#
# Date: 14/06/2017
#
#-------------------------------

def setup():
    size(800, 500)
    background(150)

def draw():
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
    
def mouseClicked():
    if mouseX > 225 and mouseX < 575 and mouseY >  200 and mouseY < 275:
        background(100)
    elif mouseX > 250 and mouseX < 550 and mouseY > 350 and mouseY < 425:
        background(200)