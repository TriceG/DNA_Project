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

def mouseDragged():
    " "