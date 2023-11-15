import math


class Shape:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    def print_details(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__setitem__('radius', radius)

    def __setitem__(self, key, value):
        if key == "radius":
            self.radius = value
            self.perimeter = 2 * math.pi * self.radius
            self.area = math.pi * self.radius * self.radius

    def print_details(self):
        return ("We have a circle with radius " + str(self.radius) +
                '. It\'s perimeter is ' + str(self.perimeter) + ' and it\'s area is ' + str(self.area) + '.')


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = 0
        self.width = 0

        self.__setitem__('length', length)
        self.__setitem__('width', width)

    def __setitem__(self, key, value):
        if key == "length":
            self.length = value
            self.perimeter = 2 * (self.length + self.width)
            self.area = self.length * self.width
        elif key == "width":
            self.width = value
            self.perimeter = 2 * (self.length + self.width)
            self.area = self.length * self.width

    def print_details(self):
        return ("We have a rectangle with length " + str(self.length) + " and width " + str(self.width) +
                '. It\'s perimeter is ' + str(self.perimeter) + ' and it\'s area is ' + str(self.area) + '.')


class Triangle(Shape):
    def __init__(self, l1, l2, l3):
        super().__init__()
        self.l1 = self.l2 = self.l3 = 0
        self.__setitem__('l1', l1)
        self.__setitem__('l2', l2)
        self.__setitem__('l3', l3)

    def __setitem__(self, key, value):
        if key == 'l1':
            self.l1 = value
        elif key == 'l2':
            self.l2 = value
        elif key == 'l3':
            self.l3 = value

        if self.l1 != 0 and self.l2 != 0 and self.l3 != 0:
            self.perimeter = self.l1 + self.l2 + self.l3
            self.sp = self.perimeter / 2
            self.area = math.sqrt(self.sp*(self.sp - self.l1)*(self.sp - self.l2)*(self.sp - self.l3))

    def print_details(self):
        return ("We have a triangle with l1, l2, l3:  " + str(self.l1) + ', ' +
                str(self.l2) + ', ' + str(self.l3) +
                '. It\'s perimeter is ' + str(self.perimeter) + ' and it\'s area is ' + str(self.area) + '.')


c = Circle(7)
r = Rectangle(2,3)
t = Triangle(3,4, 5)
print(c.print_details())
print(r.print_details())
print(t.print_details())
