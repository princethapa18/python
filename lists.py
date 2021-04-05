# Week 15 Monday 5 April 2021
# Working with lists

friends = ["Arvind", "Satheesh", "Bagal", "Arvind"]

print(friends)
print(friends[1])
print(friends[-1])  ; #access elements from the last
print(friends[-2])
#print(friends[-4])
#IndexError: list index out of range

# O/P
#['Arvind', 'Satheesh', 'Bagal']
#Satheesh
#Bagal
#Satheesh

idx = friends.index("Satheesh")

print("idx : " + str(idx) ); # gives type error bc we tried concatinating string with int value . therefore idx is converted to string

#print("idx of Baghel : " + str(friends.index("Baghel")))
#ValueError: 'Baghel' is not in list

#idx1 = friends.index("Baghel") ; #ValueError: 'Baghel' is not in list

print(friends.count("Arvind")) ; # O/P 2

friends.sort()
print(friends)

friends.reverse()
print(friends)


mixed_List = ["test", 56, 45.68, "c", "info"]

print(mixed_List)
print(mixed_List[1]*2)
#print(mixed_List[1]*2 + mixed_List[2] + mixed_List[-1])
#TypeError: unsupported operand type(s) for +: 'float' and 'str'

print(mixed_List[1]*2 + mixed_List[2])   ; # ok O/P 157.68
print(mixed_List[0] + " " + mixed_List[-1]) ; # ok   O/P test info

mixed_List2 = mixed_List.copy()

print(mixed_List2)