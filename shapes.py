class Square:
    """ 
    
    Create a square class that give upper left (X, Y),
    side legnth, color, and method to draw
    """

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        #Changes slices of array into new color 
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:
    """
    
    Create a recntagle that gives upper left (X, Y),
    height, width, color, and method to draw
    """

    def __init__(self, x, y, width, height, color):
        self.x = x
        self. y = y
        self. width = width
        self. height = height
        self.color = color


    def draw(self, canvas):
        #Changes slices of array into new color 
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] =self.color
