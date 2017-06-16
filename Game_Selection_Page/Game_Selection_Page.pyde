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

from ButtonClass import*
page = "Main"

button = Button()

def setup():
    size(800, 500)
    background(150)

def draw():
    global page
    #Main Page: Game Selection Page
    if page == "Main":
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
    #Page for Game1 Level Selection
    elif page == "DNA_LevelSelection":
        #Put page code here
        " "
    #Intro Page for GAME1
    elif page == "DNA_Intro":
        #Put page code here
        " "
    #DNAConstruction - Easy
    elif page == "Game1_Easy":
        #put page code here
        " "
    #DNAConstruction - Medium
    elif page == "Game1_Med":
        #put page code here
        " "
    
    
def mouseClicked():
    global page
    if page == "Main" and button.game1Btn():
        background(100)
        page = "DNA_LevelSelection"
    elif page == "Main" and button.game2Btn():
        background(200)
        page = #your page name