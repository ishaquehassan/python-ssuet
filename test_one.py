addition = 2+3
message = 'hello world hello world' + str(addition)

cars = ["City","Accord","SL65"]
cars.append("Abc")
cars.insert(0,"hello world")
cars.insert(-1,"hello world1 2")

print(cars)
cars.remove("City")
print(cars)
cars.pop(0)
print(cars)

abcArr = ["A","a","B","b","C","c"]

abcArr.sort(reverse=True)
print(sorted(abcArr))
newAbcArr = sorted(abcArr)
newAbcArr.reverse()
print(newAbcArr)
print(len(newAbcArr))

def delAll(arr):
    del arr
    return []

def add(a,b):
    return a+b

cars = delAll(cars)
print(message.rstrip())
print(cars)
print(add(2,3))