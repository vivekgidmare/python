import turtle
def draw_square(turtle_object):
    degree= 0;
    while degree < 36:
        print(degree)
        turtle_object.left(10)
        for count in range(0,4):        
            turtle_object.forward(100)    
            turtle_object.left(90)
        degree=degree+1    
    
def draw_circle(turtle_object,radius):
        turtle_object.circle(radius)

def draw_triangle(turtle_object):
     for triangle in range(0,2):
        turtle_object.forward(200)
        turtle_object.left(120)
     turtle_object.forward(200)

def draw_flower(turtle_object):

       for i in range(0,36): 
        turtle_object.forward(100)
        turtle_object.left(45)
        turtle_object.forward(100)
        turtle_object.left(135)
        turtle_object.forward(100)
        turtle_object.left(45)
        turtle_object.forward(100)
        turtle_object.left(145)
 
               
def draw_shapes():
    print("draw shapes called")
    window= turtle.Screen()
    window.bgcolor("red")
    brush_square=turtle.Turtle()
    brush_square.shape("turtle")
    brush_square.color("white")
    brush_square.speed(10)
 #   draw_square(brush_square)

    brush_circle=turtle.Turtle()    
    brush_circle.color("green")
    brush_circle.speed(10)
 #   draw_circle(brush_circle,100)

    brush_triangle=turtle.Turtle()
    brush_triangle.color("blue")
    brush_triangle.speed(2)
 #   draw_triangle(brush_triangle)

    brush_flower=turtle.Turtle()
    brush_flower.speed(0)
    draw_flower(brush_flower)
    brush_flower.left(270)
    brush_flower.forward(250)
    
    
    window.exitonclick()
draw_shapes()
