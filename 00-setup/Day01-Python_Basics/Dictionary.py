student = {
    "name":"Jay",
    "age":21,
    "dept":"cs"
}

print(student)
#{'name': 'Jay', 'age': 21, 'dept': 'cs'}

print(student["name"])
#Jay

student["age"]= 22
print(student)
#{'name': 'Jay', 'age': 22, 'dept': 'cs'} --> Age is updated

student["city"] = "New York"
print(student)
#{'name': 'Jay', 'age': 22, 'dept': 'cs', 'city': 'New York'} -->New key-value pair added

print(student.get("grade","Not Available"))
#Not Available

student.pop("city")
print(student)
#{'name': 'Jay', 'age': 22, 'dept': 'cs'}

student.popitem()
print(student)
#{'name': 'Jay', 'age': 22}

print(student.keys())
#dict_keys(['name', 'age'])

print(student.values())
#dict_values(['Jay', 22])

print(student.items())
#dict_items([('name', 'Jay'), ('age', 22)])

for key, value in student.items():
    print(key, value)

# name Jay
# age 22

student.update({
    "age": 22,
    "city": "Chennai"
})

print(student)
#{'name': 'Jay', 'age': 22, 'city': 'Chennai'}

student.clear()
print(student)
#{}

