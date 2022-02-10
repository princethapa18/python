"""  10 Feb 2022
 OOPs in Python
 class variable vs instance variable
 class methods, static methods, instance methods
 private members and methods
 by default public
"""

class Vehicle:
    # anything declared here is a class variable
    numVehicle = 10  # class variable     Vehcile.numVehicle
    # constructor
    def __init__(self, make, color, model):
        self.__make = make # __make   pvt member (__ two underscores for pvt function or member)  Ex:  def __pvtFun(self, arg1, arg2, ...) :
        self.__color = color
        self.__model = model
    
    # public getter and setter functions
    def getMake(self):
        return self.__make
    def setMake(self, make):
        self.__make = make

    def printDetails(self):
        print("Manufacturer: " , self.__make);
        print("Color: ", self.__color)
        print("Model: ", self.__model)

    @staticmethod    
    def fun(arg1, arg2):
        pass
    @classmethod
    def fun1(cls, arg1, arg2):
        pass

# class Car : public Vehicle
class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        Vehicle.__init__(self, make, color, model)
        self.__doors = doors
    def printDetails(self):
        Vehicle.printDetails(self)
        print("Doors: ", self.__doors)

# Python functions are virtual by default?

obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printDetails()

""" 
O/P
If Car doesn't implement its own printDetails
Manufacturer:  Suzuki
Color:  Grey
Model:  2015
"""