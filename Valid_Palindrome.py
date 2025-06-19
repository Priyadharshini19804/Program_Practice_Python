'''
Valid Palindrome 
Example: 
Input: "racecar" 
Output: True 
Input: "hello" 
Output: False 

'''

text = input("Enter a word: ")
length = 0
for char in text:
    length += 1
i = 0
is_not_palindrome = 0 
while i < length // 2:
    if text[i] != text[length - 1 - i]:
        is_not_palindrome = 1 
        break
    i += 1
if is_not_palindrome == 0:
    print("Output: True")
else:
    print("Output: False")
