def count_numbers():
    numbers = [5, 3, 4, 2]
    print(len(numbers))
count_numbers()



secret_number = 10
guess = int(input("Guess the number: "))

if guess > secret_number:
    print("Too high!")
elif guess < secret_number:
    print("Too low!")
else:
    print("Correct!")