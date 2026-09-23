list1 = ["python","C++","Java"]
print(list1)
##['python', 'C++', 'Java']

list1.append("Kotlin")
print(list1)
##['python', 'C++', 'Java', 'Kotlin']

list1.extend(["JS","C"])
print(list1)
##['python', 'C++', 'Java', 'Kotlin', 'JS', 'C']

list1.remove("C++")
#remove(idx) = Value Error
print(list1)
##['python', 'Java', 'Kotlin', 'JS', 'C']

list1.pop()
print(list1)
##Removes Last Element
##['python', 'Java', 'Kotlin', 'JS']

list1.pop(1)
print(list1)
##Removes the element @ that prticular index
##['python', 'Kotlin', 'JS']

print(len(list1))
##length of the list
##3

##Looping in list - without index
tools = ["Python", "OpenCV", "PyTorch"]

for tool in tools:
    print(tool)

# Python
# OpenCV
# PyTorch

# Looping thru list - with index
for i, tool in enumerate(tools):
    print(i, tool)
# 0 Python
# 1 OpenCV
# 2 PyTorch

#List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers if n % 2 == 0]
print(squares)  # [4, 16]

list2 = ["Java",101,True]
print(list2)
#['Java', 101, True]
#List eith different d_types