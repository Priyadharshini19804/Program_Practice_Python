'''
Write a code to find the factorial of a number using Recursion. '''

num = int(input())
factorial = 1
for i in range(1, num + 1):
    factorial *= i
fact = [int(digit) for digit in str(factorial)]
print(f"The factorial of {num} is {factorial}")
