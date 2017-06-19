#Create a class to access all buttons
class Button():
    
    def __init__(self):
        " "
    
    #DNA Construction Game button
    def game1Btn(self):
        if mouseX > 225 and mouseX < 575 and mouseY >  200 and mouseY < 275:
            return True
        else:
            return False
    #DNA Transcription Game button
    def game2Btn(self): 
        if mouseX > 250 and mouseX < 550 and mouseY > 350 and mouseY < 425:
            return True
        else:
            return False
        
    #Play button on page 4(Game1 Intro)
    def game1Play(self):
        if mouseX > 640 and mouseX < 765 and mouseY > 375 and mouseY < 425:
            return True
        else:
            return False
        
    #Back button on game1 easy level
    def game1Back(self):
        if mouseX > 37.5 and mouseX < 112.5 and mouseY > 427.5 and mouseY < 572.5:
            return True
        else:
            return False
    
    #Next level button on game1 easy level
    def game1Next(self):
        if mouseX > 620 and mouseX < 780 and mouseY > 427.5 and mouseY < 572.5:
            return True
        else:
            return False
        
    #Quit button on level2 game 1
    def game1Quit(self):
        if mouseX > 37.5 and mouseX < 112.5 and mouseY > 427.5 and mouseY < 572.5:
            return True
        else:
            return False
    