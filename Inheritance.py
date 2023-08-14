import math

class shape:
    def __init__(self):
        self.area = 0
        self.name = ""

    def showarea(self):
        print("The area of",self.name," is ", self.area)


class circle(shape):
    def __init__(self, r):
        self.name = "Circle"
        self.r = r

    def area(self):
        self.area = math.pi * self.r * self.r


class triangle(shape):
    def __init__(self, b, h):
        self.name = "Triangle"
        self.b = b
        self.h = h


    def area(self):
        self.area = 0.5 * self.b * self.h


class rectangle(shape):
    def __init__(self, l, b):
        self.name = "Rectangle"
        self.l = l
        self.b = b

    def area(self):
        self.area = self.l * self.b


cir = circle(5)
cir.area()
cir.showarea()

tri = triangle(10,5)
tri.area()
tri.showarea()

rec = rectangle(5,5)
rec.area()
rec.showarea()
