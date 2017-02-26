cars = ["Car One","Car Two","Car Three","Car Four","Car Five"]
for car in cars:
    print(car)

for i in range(0,10):
    print(i)

numbers = list(range(1,6))
print(numbers)

answers = []
for v in range(1,10):
    answers.append(v*2)

print(answers)
print(min(answers))
print(max(answers))

sqrs = [val**2 for val in range(0,1)]
print(sqrs)

cars2 = ["Car One","Car Two","Car Three","Car Four","Car Five"]
print(cars2[2:4])
print(cars2[2:])
print(cars2[:4])
print(cars2[:-4])
print(cars2[:-6])
print(cars2[-3:])

cars3 = cars2[:]
cars3.sort(reverse=True)
print(cars3)
print(cars2)


#Toupple
rect = (200,400)
print(rect[0])
print(rect[1])
print("-------------")
for r in rect:
    print(r)

rect = (400,600)
print(rect)

#conditions
name = "Xyz"
age = 20
if(name == "Abc" or age > 10):
    print("Welcome")
elif(name == "Xyz"):
    print("hello")
else:
    print("Bye")


names = ["a","b","c"]
print("z" in names)
print("z" not in names)
if("a" not in names):
    print("Not Found")

emp = []

if emp:
    print("emp is not empty")
else:
    print("emp is empty")

#ener_name = raw_input('Enter your name')