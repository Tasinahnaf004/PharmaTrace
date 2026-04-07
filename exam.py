def square(num):
    return num * num

print(square(5))


numbers = [2 ,4, 6, 8, 10]
for num in numbers:
    if num > 5:
        print(num)


text = "Hello world"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(count)





num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")





class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello " + self.name)
Person1 = Person("tasin")
Person1.greet()





import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

# Ask user to input radius
user_radius = float(input("Enter the radius of the circle: "))

# Create Circle object
circle = Circle(user_radius)

# Print area and perimeter
print(f"Area of the circle: {circle.area():.2f}")
print(f"Perimeter of the circle: {circle.perimeter():.2f}")
