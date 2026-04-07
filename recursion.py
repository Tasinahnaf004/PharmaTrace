def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


n = int(input("Enter a number: "))
print(factorial_recursive(n))

word = "madam"
if word == word[::-1]:
    print("palindrome")
else:
    print("not palindrome")

nums = [(1, 2), (3, 1), (5, 0)]
sorted_list = sorted(nums, key= lambda x:x[1])
print(sorted_list)
