print("simple calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("\n choose operation")
print("1. Add")
print("2. substract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1-4): ")

if choice == "1":
    print("Result:", num1 + num2)

elif choice == "2":
    print("Result:", num1 - num2)

elif choice == "3":
    print("Result:", num1 * num2)

elif choice == "4":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid choice")






class Student:
    def __init__(self, name, age, grade):
        self.name = name      # Student's name
        self.age = age        # Student's age
        self.grade = grade    # Student's grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


# Example usage
student1 = Student("Tasin", 20, "A")
student2 = Student("Rafi", 19, "B+")

student1.display_info()
print()
student2.display_info()
