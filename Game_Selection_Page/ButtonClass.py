#Create a class to access all buttons
class Button():
    
    def __init__(self):
        " "
    
    def game1Btn(self):
        if mouseX > 225 and mouseX < 575 and mouseY >  200 and mouseY < 275:
            return True
        else:
            return False
        
    def game2Btn(self): 
        if mouseX > 250 and mouseX < 550 and mouseY > 350 and mouseY < 425:
            return True
        else:
            return False
    