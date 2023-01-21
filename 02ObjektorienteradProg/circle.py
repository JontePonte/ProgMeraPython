" Create circle class and test it"

from math import pi


class Circle:
    'Base class for circle, can calculate area and perimeter'
    def __init__(self, x_val=0, y_val=0, radius=0):
        self.x_val = x_val
        self.y_val = y_val
        self.radius = radius

    @property
    def radius(self):
        'Return the circle radius'
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def x_val(self):
        'Return center x coordinate'
        return self.__x_val

    @x_val.setter
    def x_val(self, x_val):
        self.__x_val = x_val

    @property
    def y_val(self):
        'Return center y coordinate'
        return self.__y_val

    @y_val.setter
    def y_val(self, y_val):
        self.__y_val = y_val

    @property
    def area(self):
        'Calculates the circle area'
        return pi * self.__radius ** 2

    @property
    def perimeter(self):
        'Calculates the circle perimeter'
        return 2*self.__radius *pi

    def __str__(self):
        return f'Circle with center {self.x_val},{self.y_val} and radius {self.radius}. \
The area = {self.area:.2f} and the perimeter = {self.perimeter:.2f}'


circle1 = Circle(radius=5)

print(circle1)
