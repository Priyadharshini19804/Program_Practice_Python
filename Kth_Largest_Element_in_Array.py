"""
Kth Largest Element in Array 

Input: 
An integer array nums 
An integer k representing the kth largest element 

Output: 
The kth largest element in the array nums. 

Example: 
Input: 
nums = [5,3,1,6,2] 
k = 3 

Output: 3 (The third largest element is 3.) 
"""

nums = []
size = int(input("Enter size of array: "))
print("Enter array elements:")
for i in range(size):
    nums.append(int(input()))
k = int(input("Enter k (to find kth largest element): "))
for i in range(len(nums)):
    for j in range(0, len(nums) - i - 1):
        if nums[j] < nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(f"The {k}th largest element is: {nums[k-1]}")

    # Alternative implementation:        

"""nums = []
size = int(input("Enter size of array: "))
print("Enter array elements:")
for i in range(size):
    nums.append(int(input()))
k = int(input("Enter k (to find kth largest element): "))
nums.sort(reverse=True)
print(f"The {k}th largest element is: {nums[k-1]}")"""
