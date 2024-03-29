global sWidth
global sHeight
sWidth = 500
sHeight = 500

class player(object):
    def __init__(self):
        self.x  = 100
        self.y = 100
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.speed = 5
        self.h = 20
        self.w = 20
       
    def show(self):
        fill(0)
        rect(self.x, self.y, self.w, self.h)
    
    def update(self):
        self.x = self.x + (self.right - self.left) * self.speed
        self.y = self.y + (self.down - self.up) * self.speed
        if not (self.x >= 0):
            self.x = 0
        if not (self.x <= ( sWidth - self.w)):
            self.x = (sWidth - self.w)
        if not (self.y >= 0):
            self.y =  0
        if not (self.y <= (sHeight - self.h)):
            self.y = (sHeight - self.h)
        if self.y >= 0:
            self.y += 1
      
def setup():
    size(sWidth, sHeight )
    global p
    p = player()
    
def draw():
    background(100)
    p.show()
    p.update()

def keyPressed():
    if keyCode == UP:
        p.up = 1
    if keyCode == DOWN:
        p.down = 1
    if keyCode == LEFT:
        p.left = 1
    if keyCode == RIGHT:
        p.right = 1
        
def keyReleased():
    if keyCode == UP:
        p.up = 0
    if keyCode == DOWN:
        p.down = 0
    if keyCode == LEFT:
        p.left = 0
    if keyCode == RIGHT:
        p.right = 0
    
    

  
