listTest = [1,"a",2,"b"]
print(listTest)

dict1 = {
    "name":"abc",
    "age":16
}

print(dict1)
print(dict1["name"])
print(dict1["age"])
dict1["name"] = "xyz"
print(dict1["name"])
#new value
dict1["hello"] = "world"
print(dict1["hello"])

del dict1["age"]
print(dict1)

for key , value in dict1.items():
    print(key+" = "+value)
print("-------------")
for key  in dict1.keys():
    print(key+"")
print("-------------")
for value  in dict1.values():
    print(value+"")
print("-------------")
for key in sorted(dict1.keys()):
    print(key + "")
print("-------------")

dictn1 = {
    "name" : "abc",
    "age" : 20
}
dictn2 = {
    "name" : "xyz",
    "age" : 21
}
dictn3 = {
    "name" : "efg",
    "age" : 22,
    "subjects" : [],
    "marks" : {
        "Java" : 50,
        "JS" : 100,
        "Python" : 70,
    }
}


students = [dictn1,dictn2,dictn3]
print(students)
print("-------------")
for student in students:
    print(student["name"])

students.append({
    "name":"hello",
    "age" : 100,
    "subjects" : ["Java","JS","Python"],
    "marks" : {
        "Java" : 50,
        "JS" : 100,
        "Python" : 70,
    }
})

print("-------------")
for student in students:
    if("subjects" in student):
        print(student["subjects"])
    if("marks" in student):
        print(student["marks"])
    print("-------------")

