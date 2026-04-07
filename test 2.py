total = 0

for i in range(1, 101):
    total = total + i

print("Sum of numbers from 1 to 100 is:", total)


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
    if b == 0:
        print("Cannot divide by zero!")
    else:
        print(a / b)
else:
    print("Invalid operator")






for i in range(1, 11):
    # Check if prime
    if i > 1:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, "is a prime number")
        elif i % 2 == 0:
            print(i, "is an even number")
        else:
            print(i, "is an odd number")
    else:
        print(i, "is neither prime nor composite")