# Week 51 21 Dec 2021

# class variables
# instance variables

# @staticmethod 
# @classmethod
# instance methods

#  what is the difference between class method and static method? What are their usages?

# by default all methods and properites are public
# use __ (double underscore) to define a variable or method as private
# __init__  initializer    special method


class Employee :
    companyName = "XYZ Technologies" # class variable
    def __init__(self, ID = None, Salary = None, Department = None, Gender = None) :
        self.ID = ID
        self.Salary = Salary
        self.Department = Department
        self.__Gender = Gender  # private member  (double underscore __ )
    def Gender(self) :
        return self.__Gender

    # private method    
    def __Salary(self):
        return self.Salary 

    @classmethod
    def getCompanyName(cls):
        return cls.companyName
    
    @staticmethod
    def demo() :
        print("this is a static method")


Steve = Employee(25, 25000, "HR" , "Male")
print("Steve.Gender() :", Steve.Gender())
print("Employee.getCompanyName() :" , Employee.getCompanyName() )   
print("Steve.getCompanyName() :", Steve.getCompanyName()); 

print("Employee.demo() :", Employee.demo());  
print("Steve.demo() :", Steve.demo());   
    