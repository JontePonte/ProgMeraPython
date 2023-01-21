" File for car class and test of car class"

class Car:
    'Base class for cars'
    def __init__(self, model='', color='', reg_nr='', tax_weight= 0):
        # Call methods for car properties
        self.set_model(model)
        self.set_color(color)
        self.set_reg_nr(reg_nr)
        self.set_tax_weight = tax_weight

    def model(self):
        'Returns the model of the car'
        return self.__model

    def color(self):
        'Returns the color of the car'
        return self.__color

    def reg_nr(self):
        'Returns the registration number of the car'
        return self.__reg_nr

    @property
    def tax_weight(self):
        'Returns the taxation weight of the car'
        return self.__tax_weight

    def set_model(self, model):
        'Set the car model'
        self.__model = model

    def set_color(self, color):
        'Sets the car color'
        self.__color = color

    def set_reg_nr(self, reg_nr):
        'Sets the car registration number'
        self.__reg_nr = reg_nr

    @tax_weight.setter
    def set_tax_weight(self, tax_weight):
        'Set the taxation weight of the car'
        assert tax_weight >= 0, ('Negative taxation weight', tax_weight)
        self.__tax_weight = tax_weight


car1 = Car(model='volvo', color='Red', reg_nr='CAR 313', tax_weight=0)


print(car1.model())
print(car1.color())
print(car1.reg_nr())
print(car1.tax_weight)
