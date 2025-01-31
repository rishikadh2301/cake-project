
from turtle import Screen, Turtle

def draw_layer(x, y, width, color1, color2, turta):
    """ Draws a rectangle with an icing decoration

    Args:
        x: Initial x-axis coordinate
        y: Initial y-axis coordinate
        width: Width of the cake
        color1: Color of the rectangle
        color2: Color of the icing
        turta: Name of the Turtle
    """
    turta.pencolor(color1) 
    turta.up()
    turta.goto(x,y) # Goes to coordinates (x,y) without drawing and then begins drawing
    turta.down()
    turta.begin_fill() # Will fill the shape after it is drawn and the end fill functions is called
    turta.fillcolor(color1)
    turta.forward(width/2) # Starts drawing a rectangle starting from coordinates x and y
    turta.left(90)
    turta.forward(width/2)
    turta.left(90)
    turta.forward(width)
    turta.left(90)
    turta.forward(width/2)
    turta.left(90)
    turta.forward(width)
    turta.end_fill()#we make one layer of color1

    turta.pencolor(color2)
    turta.up()
    turta.goto(x-(width/2),y+(width/2)) # Goes to the top left of the rectangle
    turta.down()
    turta.right(90)
    turta.begin_fill()
    turta.fillcolor(color2) 
    turta.circle(width/8,180) # Draws 4 semicircles along the top of the rectangle, each with a radius of width/8
    turta.right(180)
    turta.circle(width/8,180)#to make semicircles (frosting)
    turta.right(180)
    turta.circle(width/8,180)
    turta.right(180)
    turta.circle(width/8,180)
    turta.left(90)
    turta.goto(x-(width/2),y+(width/2))
    turta.left(180)
    turta.end_fill()


def draw_cake(x, y, width, color1, color2, color3, color4, turta):
    """ Draws a cake by using the draw_layer function 3 times and adds a candle on top

    Args:
        x: Initial x-axis coordinate
        y: Initial y-axis coordinate
        width: Width of the first layer of the cake
        color1: Color of the first layer of the cake
        color2: Color of the second layer of the cake
        color3: Color of the third layer of the cake
        color4: Color of the icing
        turta: Name of the Turtle
    """
    turta.pencolor("white")
    turta.up()
    turta.goto(x,y)
    turta.down()
    turta.begin_fill()
    turta.fillcolor("white")
    turta.forward((width/2)*1.15) # Draws a rectangle below the cake which servers as a plate
    turta.right(90)
    turta.forward(width/15)
    turta.right(90)
    turta.forward(width*1.15)
    turta.right(90)
    turta.forward(width/15)
    turta.right(90)
    turta.forward(width*1.15)
    turta.end_fill()

    draw_layer(x, y, width, color1, color4, turta) # Calls the draw layer function 3 times to create 3 different layers
    draw_layer(x, y + (width/2), width*(2/3), color2, color4, turta)
    draw_layer(x, y + (width/2) +(width/3), width*(1/3), color3, color4, turta) #to make the cake pyramid shaped
    
    turta.pencolor("white")#for candle
    turta.up()
    turta.goto(x, y + (width/2) + (width/3) + (width/6)) # Goes to the top of the cake without drawing
    turta.down()
    turta.begin_fill()
    turta.fillcolor("white")
    turta.forward(width/40) # Draws a rectangle which serves as a candle decoration
    turta.left(90)
    turta.forward(width/10)
    turta.left(90)
    turta.forward(width/20)
    turta.left(90)
    turta.forward(width/10)
    turta.left(90)
    turta.forward(width/20)
    turta.end_fill()

    turta.pencolor("orange") #for the flames
    turta.up()
    turta.goto(x, y + (width/2) + (width/3) + (width/6) + (width/10)) # Goes to the top of the candle without drawing
    turta.down()
    turta.begin_fill()
    turta.fillcolor("orange")
    turta.circle(width/30) # Draws a circle which servers as a flame for the candle
    turta.end_fill()

def table(x,y,len,width,color,turta):
    """ Draws a table and uses the legs_table function to draw 4 legs

    Args:
        x: Initial x-axis coordinate
        y: Initial y-axis coordinate
        len: length of the table
        width: width of the table
        color: Color of the table
        turta: Name of the Turtle
    """
    turta.pencolor(color)
    turta.penup()
    turta.goto(x-len/2,y)
    turta.pendown()
    turta.begin_fill()
    turta.fillcolor(color)
    turta.fd(len)
    turta.right(135)
    turta.fd(width)
    turta.right(45)
    turta.fd(len)
    turta.right(135)
    turta.fd(width)
    turta.end_fill()

    turta.begin_fill()
    turta.fillcolor(color)
    legs_table(turta)
    turta.penup()
    turta.goto(len+x-20-(len/2),0)  #we go to half of the lenght of table and then start drawing
    turta.pendown()
    turta.left(45)
    legs_table(turta)
    turta.penup()
    turta.right(135)  #to make 3d table
    turta.fd(width)
    turta.pendown()
    
    turta.right(45)
    turta.fd(20)
    turta.left(225)
    legs_table(turta)
    
    turta.left(180)
    turta.fd(len)
    turta.right(135)
    legs_table(turta)
    turta.end_fill()

    
def legs_table(turta):
    """ Draws a leg of a table

    Args:
        turta: Name of the Turtle
    """
    turta.right(135)    #for the legs of the table (one leg)
    turta.forward(100)  
    turta.right(90)
    turta.backward(20)
    turta.right(90)
    turta.fd(100)
    turta.right(90)