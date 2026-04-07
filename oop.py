class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def save(self):
        with open("student.txt", "a") as file:
            file.write(f"{self.name} - {self.age}\n")

s1=Student("Tasin", 27)
s1.save()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r1 = Rectangle(100, 200)
print(r1.area())
print(r1.perimeter())



class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
account=Bankaccount("Tasin", 10000)
account.deposit(3000)
account.withdraw(1000)
print(account.balance)
