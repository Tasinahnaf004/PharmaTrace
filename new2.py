fruits = ["apple" , "banana" , "mango"]
for fruit in fruits:
    if fruit == "banana":
        print("I love banana")
    else:
        print("I love all")



favourite = input("Enter your favourite fruit: ")

if favourite == "mango":
    print("I love mango")
else:
    print("I love apple and banana")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("Invalid operator")