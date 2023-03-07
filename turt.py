import turtle

turtle.setup(800, 600)
wn = turtle.Screen()

spiral = turtle.Turtle()
spiral.color("blue")
spiral.penup()      
          
size = 10
for i in range(35):
  spiral.dot()                
  size = size + 2             
  spiral.forward(size)          
  spiral.right(24)   
