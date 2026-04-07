numbers = [10, 20, 30, 40, 50]
new_numbers = numbers[:]  # make a copy

for i in range(len(new_numbers)):
    new_numbers[i] = new_numbers[i] * 2  # multiply each element by 2

print("Original list:", numbers)
print("New list:", new_numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []  # new list for even numbers

for num in numbers:
    if num % 2 == 0:   # check if number is even
        even_numbers.append(num)

print("Original list:", numbers)
print("Even numbers:", even_numbers)






cart = []

while True:
    item = input("Enter an item (or type 'done' to finish): ")
    if item.lower() == "done":  # stop if user types 'done'
        break
    cart.append(item)

print("\nYour full cart:", cart)
print("Number of items:", len(cart))



words = ["apple", "banana", "mango", "orange"]
uppercase_words = []

for word in words:
    uppercase_words.append(word.upper())  # convert to uppercase

print("Original list:", words)
print("Uppercase list:", uppercase_words)