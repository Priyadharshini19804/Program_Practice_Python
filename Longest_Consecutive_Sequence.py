"""
Longest Consecutive Sequence 

Input: 
An integer array nums 

Output: 
The length of the longest consecutive sequence present in the array nums. 

Example: 
Input: nums = [100, 4, 200, 1, 3, 2] 
Output: 4 (Explanation: The longest consecutive sequence is [1, 2, 3, 4].) 

"""

num = []
size = int(input("Enter size of array: "))
print("Enter the array elements:")
for i in range(size):
    num.append(int(input()))
num_set = set(num)
longest_sequence = 0
for num in num:
    if num - 1 not in num_set:
        current_num = num
        current_streak = 1
        while current_num + 1 in num_set:
            current_num += 1
            current_streak += 1
        longest_sequence = max(longest_sequence, current_streak)

print(f"Length of longest consecutive sequence: {longest_sequence}")
