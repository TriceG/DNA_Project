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
    DNAShape()
    text("")