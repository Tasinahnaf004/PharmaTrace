#swap two numbers
a = 10
b = 20
a , b = b, a
print(a,b)

#celcius to fahrenheit
c = float(input("Enter in celcius"))
f = (c * 9/5) + 32
print(f)

#even and odd
n = int(input("Enter a number"))
if n % 2 == 0:
    print("even")
else:
    print("odd")

#name and age
class Name:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = "Ahnaf"
age = 27

person = Name(name, age)

print(person.name)
print(person.age)
