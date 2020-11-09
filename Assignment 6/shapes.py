import turtle

s = turtle.Screen()
s.bgcolor("light green")
s.title("Turtle")
t = turtle.Turtle()
t.color("red")


class shape:
    def __init__(self, length = 0) :
        self.length = length


class polygon(shape):
    def info(self):
        print("In geometry, a polygon can be defined as a flat or plane, two-dimensional  with straight sides.")
        
class square(polygon):
    def show(self):
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
    

class pentagon(polygon):
    def show(self):
        for i in range(5):
           t.forward(self.length) 
           t.right(72) 

class hexagon(polygon):
    def show(self):
        for i in range(6):
           t.forward(self.length) 
           t.right(60)

class octagon(polygon):
    def show(self):
        for i in range(6):
           t.forward(self.length) 
           t.right(45)

class triangle(polygon):
    def show(self):
        t.forward(self.length) 
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)

class star(polygon):
    def show(self):
        for i in range(5):
            t.forward(self.length)
            t.right(144)

class circle(polygon):
    def show(self):
        t.circle(self.length)


shape = circle(80)
shape.info()
shape.show()




turtle.done()




