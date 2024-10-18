# # Find the leap_year
#
# a = int(input("Enter a year:"))
# if a % 4 == 0 :
#     print("This ia leap_year:",a)
# else:
#     print("Not a leap year:")
#
# # find prime number:
#
# a = int(input("Enter a Number:"))
#
# if a >= 1 and a % 2 != 0 :
#     print("This ia prime number:",a)
# else:
#     print("Not a prime number:")
#
# # factorial number:
#
# def find_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * find_factorial(n-1)
# print(find_factorial(5))
#
# # fibnocci series
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(10))
#
# # Simple Calculator
# def simple_calculator(a, b, operation):
#     if operation == '+':
#         return a + b
#     elif operation == '-':
#         return a - b
#     elif operation == '*':
#         return a * b
#     elif operation == '/':
#         return a / b
#     else:
#         return "Invalid operation"
# print(simple_calculator(5,6, "+"))

# #  Count Vowels in a String
# def count_vowels(s):
#     vowels = 'aeiouAEIOU'
#     return sum(1 for char in s if char in vowels)
# print(count_vowels("alimurad"))

# #Swap Two Numbers
# def swap(a, b):
#     return b, a
# print(swap(3,4))

# # is paindrome:
# def ispalindrome(str):
#     startindex = 0
#     endindex = len(str) -1
#
#     for x in range(len(str)):
#         if str[startindex] != str[endindex]:
#             return False
#     return True
# print(ispalindrome('racecar'))

# Largest of Three Numbers
# def largest_of_three(a, b, c):
#     return max(a, b, c)
# print(largest_of_three(5,6,7))

#  Find the Second Largest Number
numbers = [4, 1, 2, 7, 5, 9, 2, 4]
unique_numbers = list(set(numbers))
unique_numbers.sort()
# Get the second largest number
second_largest_number = unique_numbers[-2]
print("Second Largest Number:", second_largest_number)

# Second Smallest Number
numbers = [4, 1, 2, 7, 5, 9, 2, 4]
unique_numbers = list(set(numbers))
unique_numbers.sort()
second_smallest_number = unique_numbers[1]
print("Second Smallest Number:", second_smallest_number)





















# # Problem 5: Simple Interest Calculator
# def simple_interest(principal, rate, time):
#     return (principal * rate * time) / 100
#
# # Problem 6: Multiplication Table Generator
# def multiplication_table(n):
#     return [n * i for i in range(1, 11)]
#
# # Problem 7: Count Positive and Negative Numbers
# def count_positive_negative(numbers):
#     positive = sum(1 for num in numbers if num > 0)
#     negative = sum(1 for num in numbers if num < 0)
#     zero = sum(1 for num in numbers if num == 0)
#     return positive, negative, zero
#
#
#
# # Problem 9: Temperature Converter
# def celsius_to_fahrenheit(celsius):
#     return celsius * 9/5 + 32
#
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9
#
#
#
# # Problem 11: Add Two Numbers without the + Operator
# def add_without_plus(a, b):
#     while b != 0:
#         carry = a & b
#         a = a ^ b
#         b = carry << 1
#     return a



# # Problem 15: Reverse a String
# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str
#


#
# # Problem 18: Find the GCD of Two Numbers
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
# # Problem 19: Armstrong Number
# def is_armstrong_number(n):
#     digits = [int(d) for d in str(n)]
#     return n == sum(d ** len(digits) for d in digits)
#

#
# # Problem 22: Second Largest in a Sorted Array
# def second_largest_sorted(numbers):
#     return numbers[-2]
#
# # Problem 23: Remove Duplicates and Find Second Largest
# def remove_duplicates_and_second_largest(numbers):
#     unique_numbers = list(set(numbers))
#     unique_numbers.sort()
#     return unique_numbers[-2]
#
# # Problem 24: Second Largest Using a Single Pass
# def second_largest_single_pass(numbers):
#     first = second = float('-inf')
#     for num in numbers:
#         if num > first:
#             second = first
#             first = num
#         elif first > num > second:
#             second = num
#     return second
#
# # Problem 25: Second Largest in a 2D Array
# def second_largest_2d_array(matrix):
#     flat_list = [item for sublist in matrix for item in sublist]
#     unique_numbers = list(set(flat_list))
#     unique_numbers.sort()
#     return unique_numbers[-2]
#
#
# # Problem 2: Sum of Digits
# def sum_of_digits(n):
#     return sum(int(digit) for digit in str(n))
#
# # Problem 3: Sum of First N Natural Numbers
# def sum_of_first_n(n):
#     return n * (1 + n) // 2
#
#
#
