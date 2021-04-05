# Week 15 Monday 5 April 2021

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
#result = num1 + num2
#print(result)

#O/P
#Enter a number: 5
#Enter another number: 8.03
# 58.03    why 58.03    because it treats num1 and num2 as string
#  num1 + num2   -->  "5" + "8.03"    = 58.03

#result = int(num1) + int(num2)
#print(result)

# type conversion
#Enter a number: 5
#Enter another number: 8.03       num2 is float
#Traceback (most recent call last):
#  File "/applgns/my_new_data/calc/calc.py", line 14, in <module>
#    result = int(num1) + int(num2)
#ValueError: invalid literal for int() with base 10: '8.03'

result = float(num1) + float(num2)
print(result)

# num1^2
exp = int(num1)**2
print(exp)