'''
Write a code to check for the longest palindrome in an array. 
This problem asks to find the longest palindrome in an array of strings. A palindrome is a word, 
phrase, or sequence that reads the same backward as forward. 
 The goal is to identify the longest string in the array that is a palindrome. 
 Example for array [“racecar”, “level”, “hello”, “madam”, “world”]: 
The longest palindrome is “racecar”. 
'''

print("Enter words separated by space:")
input_line = input()
words = []
word = ""
i = 0
while i < len(input_line):
    ch = input_line[i]
    if ch != ' ':
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""
    i += 1
if word != "":
    words.append(word)
longest_palindrome = ""
max_length = 0
i = 0
while i < len(words):
    word = words[i]
    length = 0
    for ch in word:
        length += 1
    j = 0
    while j < length // 2:
        if word[j] != word[length - j - 1]:
            break
        j += 1
    if j == length // 2:
        if length > max_length:
            max_length = length
            longest_palindrome = word

    i += 1
print("The longest palindrome is:", longest_palindrome)
