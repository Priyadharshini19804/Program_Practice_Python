'''

Write the code to find the Fibonacci series upto the nth term. 
This problem asks to generate the Fibonacci sequence up to the nth term. In this sequence, each 
number is the sum of the two preceding ones, starting from 0 and 1. 
 The goal is to calculate and display all Fibonacci numbers from the 0th to the nth term. 
 Example for n = 10: 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34 

'''

# Number of terms
n = int(input("Enter the number of Fibonacci terms: "))

# First two Fibonacci numbers
a = 0
b = 1

# Print Fibonacci series
print("Fibonacci series:")
for i in range(n):
    print(a, end=' ')
    c = a + b
    a = b
    b = c
