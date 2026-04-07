nums = [1,2,3,4,5,6]

def sums_list(nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sums_list(nums))

def get_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count
print(get_vowels('python'))

def max_number(nums):
    max_val = nums[0]

    for num in nums:
        if num > max_val:
            max_val = num

    return max_val
print(max_number(nums))

def reverse_string(ch):
    return ch[::-1]
ch = "hello"
print(reverse_string(ch))

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
print(two_sum(nums, 10))


def is_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
print(is_palindrome("madam"))

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result
print(remove_duplicates(nums))

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


s = "hello"
print(char_frequency(s))
