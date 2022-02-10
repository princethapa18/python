# Week 14   4 April 2021 Sunday
# Type conversion

birth_year = input("Birth year: ")
#age = 2021 - birth_year
# even if birth_year is an integer valuer python treats it as a string
# therefore it gives the following error
#Traceback (most recent call last):
#  File "D:/2021/Python/type_conversion.py", line 5, in <module>
#    age = 2021 - birth_year
#TypeError: unsupported operand type(s) for -: 'int' and 'str'

#how to fix this
age = 2021 - int(birth_year) ; # birth_year is converted to int
print(age)

