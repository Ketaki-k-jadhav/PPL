import turtle

wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("black")
t.color("yellow")
t.pensize(4)


class shape:
    def __init__(self, sides=0, length=0):
        self.sides = sides
        self.length = length


class polygon(shape):
    def info(self):
        print("In geometry, a polygon can be defined as a flat or plane, two-dimensional closed shape with straight sides.")


class square(polygon):
    def show(self):
        for i in range(self.sides):
            t.fd(self.length)
            t.rt(90)


class pentagon(polygon):
    def show(self):
        for i in range(self.sides):
            t.forward(self.length)
            t.right(72)


class hexagon(polygon):
    def show(self):
        for i in range(self.sides):
            t.forward(self.length)
            t.right(60)


class octagon(polygon):
    def show(self):
        for i in range(self.sides):
            t.forward(self.length)
            t.right(45)


class triangle(polygon):
    def show(self):
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)


class circle(polygon):
    def show(self):
        t.circle(self.length)


class star(polygon):
    def show(self):
        for i in range(self.sides):
            t.forward(self.length)
            t.right(144)


oct1 = octagon(8, 125)
oct1.show()


circle1 = circle(0, 125)
circle1.show()


square1 = square(4, 125)
square1.show()
