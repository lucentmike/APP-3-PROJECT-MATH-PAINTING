import numpy as np
from PIL import Image


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


class Canvas:
    """
    
    Create a canvas that takes in width, height, and backround
    color, creates method to make the image

    """


    def __init__(self, width, height, color):
        self.width = width
        self. height = height
        self.color = color
    
        #Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        #Change [0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
    #Converts array into image file
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


canvas = Canvas(width=20, height = 30, color = (255, 255, 255))
r1 = Rectangle(x=1, y=6, width = 10, height=7, color=(100, 200, 125))
r1.draw(canvas=canvas)
s1=Square(x=1, y=3, side=3, color=(0, 100, 222))
s1.draw(canvas=canvas)
canvas.make('canvas.png')