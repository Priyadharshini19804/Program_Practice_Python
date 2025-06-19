""" 
Find the Missing Number

Input:
An integer array nums containing n distinct numbers from the range 0 to n-1 
(inclusive). 

Output: 
The missing number in the array nums. 

Example: 
Input: nums = [3,0,1] 
Output: 2 (Since 2 is missing from the range 0 to 2) 

"""

num = []
size = int(input("Enter the size of array: "))
print("Enter the numbers (0 to", size, "excluding one number):")
for i in range(size):
    num = int(input())
    num.append(num)
n = len(num)
expected_sum = (n * (n + 1)) // 2
actual_sum = sum(num)
missing = expected_sum - actual_sum
print(f"Missing number is: {missing}")
