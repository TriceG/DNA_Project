#----------------------------
#
# ConstructionGame_Intro.pyde
#
# Description: Introduce the DNA Contruction game.
#
# Author: goyette.beatrice
#
# Collaborator: macduff.marshall
#
# Date: 15/06/2017
#
#-----------------------------

def setup():
    background(255)
    size(800, 500)

#draw a DNA element
def DNAshape():
    fill(255, 132, 8)
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
    fill(0)
    text("P", 395, 257)
    text("S", 425, 275)
    text("N", 463, 273)
            
def draw():
    textSize(20)
    DNAshape()
    textSize(30)
    fill(139, 0, 255)
    text("The Structure of DNA", 50, 50)
    textSize(20)
    fill(0)
    text("- DNA is a double helical structure", 50, 100)
    text("- Each nucleotide is made up of a phosphate group, a 5-carbon sugar,", 50, 150)
    text(" and a nitrogenous base (ACGT).", 50, 200)
    fill(95, 203, 2)
    text("Click and drag the components DNA to form a nucleotide!", 50, 400)
    rectMode(CORNER)
    rect(640, 375, 125, 50)
    fill(0)
    textSize(35)
    text("START", 647, 410)
    
    if mouseX > 640 and mouseX < 765 and mouseY > 375 and mouseY < 425:
        cursor(HAND)
    else:
        cursor(ARROW)