"""
Input: [1, 2, 3, 4, 5, 6]
Output: [9] (1 + 3 + 5 = 9)
"""

nums = list(map(int,input().split()))
total = 0
for i in range(0,len(nums),2):
    total += nums[i]
print(total)