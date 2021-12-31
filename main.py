from canvas import Canvas
from shapes import Rectangle, Square


#Get canvas information from user

while True:

    colors = { 'black' : (0, 0, 0,), 'white' : (255, 255, 255)}
    
    while True:
        try:
            canvas_width = int(input("Enter the canvas width: "))
            break
        except:
            print("That is an invalid entry")

    while True:
        try:
            canvas_height = int(input("Enter the canvas height : "))
            break
        except:
            print("That is an invalid entry")

    while True: 
        canvas_color = input('Choose the canvas color, black or white: ')
        if canvas_color.lower() == 'black':
            break
        elif canvas_color.lower() == 'white':
            break
        else:
            print("That is an invalid entry")
            
    break


#Create the canvas using user inputs
canvas = Canvas(width= canvas_width, height=canvas_height, color= colors[canvas_color])

#Create while loop to take information to draw


while True:

    while True:

        shape_type = input("What do you want to draw? (rectangle, square) Enter quit to quit: ")

        if shape_type.lower() == 'rectangle':
            break
        elif shape_type.lower() == "square":
            break
        elif shape_type.lower() == 'quit':
            break
        else:
            print("That is an invalid entry")  

    #If rectangle ask for rectangle data and draw
    if shape_type.lower() == 'rectangle':

        while True:
            try:
                rec_x = int(input("Enter the rectangle x: "))
                break
            except:
                print("That is an invalid entry")
                
        while True:
            try:
                rec_y = int(input("Enter the rectangle y: "))
                break
            except:
                print("That is an invalid entry")

        while True:
            try:
                rec_width = int(input("Enter the rectangle width: "))
                break
            except:
                print("That is an invalid entry")

        while True:
            try:
                rec_height = int(input("Enter the rectangle height: "))
                break
            except:
                print("That is an invalid entry")

        while True:
            try:
                rec_r = int(input("Enter the rectangle red value : "))
                break
            except:
                print("That is an invalid entry")

        while True:
            try:
                rec_g = int(input("Enter the rectangle green value : "))
                break
            except:
                print("That is an invalid entry")

        while True:
            try:
                rec_b = int(input("Enter the rectangle blue value : "))
                break
            except:
                print("That is an invalid entry")


        #Draws the shape using user information
        r1 = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=(rec_r, rec_g, rec_b))
        r1.draw(canvas = canvas)


    #If square ask for data and draw
    if shape_type.lower() == 'square':

        while True:
            try:
                square_x = int(input("Enter the square x: "))
                break
            except:
                print("That is an invalid entry")

        while True:
            try:
                square_y = int(input("Enter the square y: "))
                break
            except:
                print("That is an invalid entry")

        while True:
            try:
                square_side = int(input("Enter the square side: "))
                break
            except:
                print("That is an invalid entry")

        while True:
            try:
                square_r = int(input("Enter the square red value : "))
                break
            except:
                print("That is an invalid entry")

        while True:
            try:
                square_g = int(input("Enter the square green value : "))
                break
            except:
                print("That is an invalid entry")

        while True:
            try:
                square_b = int(input("Enter the square blue value : "))
                break
            except:
                print("That is an invalid entry")
        

        #Draws the shape using user information
        s1 = Square(x=square_x, y=square_y, side=square_side, color=(square_r, square_g, square_b))
        s1.draw(canvas = canvas)

    if shape_type.lower() == 'quit':
        break

#Print the canvas
canvas.make('canvas.png')
