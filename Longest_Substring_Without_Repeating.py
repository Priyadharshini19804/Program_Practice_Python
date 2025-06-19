'''
Longest Substring Without Repeating Characters 
Input: "abcabcbb" 
Output: 3 (The longest substring is "abc") 
'''

text = input("Enter a string: ")
n = len(text)
max_len = 0
i = 0
while i < n:
    j = i
    sub = ""
    while j < n:
        k = 0
        repeat = 0
        while k < len(sub):
            if sub[k] == text[j]:
                repeat = 1
                break
            k += 1
        if repeat == 1:
            break
        sub += text[j]
        j += 1
    if len(sub) > max_len:
        max_len = len(sub)

    i += 1
print("Length of the longest substring without repeating characters:", max_len)
