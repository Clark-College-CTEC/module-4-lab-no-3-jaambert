# Lab No. 3
# CTEC 121
# Jacob Ambert

from graphics import *

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3
    circle1 = Circle(Point(400,650),125)
    circle1.draw(win)

    circle2 = Circle(Point(400,439),85)
    circle2.draw(win)

    circle3 = Circle(Point(400,290),64)
    circle3.draw(win)

    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2
    leftEye = Circle(Point(420,275),10)
    leftEye.draw(win)
    leftEye.setFill('black')
    rightEye = Circle(Point(380,275),10)
    rightEye.draw(win)
    rightEye.setFill('black')


    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose
    nose = Polygon(Point(390,285),Point(420,300),Point(400,320))
    nose.draw(win)
    nose.setFill('orange')


    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat
    hat = Rectangle(Point(370,180),Point(430,225))
    hat.draw(win)
    hat.setFill('black')


    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline
    brim = Line(Point(350,225),Point(450,225))
    brim.draw(win)




    # close the program
    
    input('Press enter to quit the program ')
    # close the graphics window
    
    win.close()


# Call the snowman() function to start the program
snowman()