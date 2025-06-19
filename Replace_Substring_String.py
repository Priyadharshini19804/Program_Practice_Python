'''

Write a code to Replace a Substring in a string 
Example : 
o Input String: 
“I love programming in Python!” 
o Substitute: 
Replace “Python” with “Java”. 
o Output: 
“I love programming in Java!”

'''

# Input string
input_string = "I love programming in Python!"
target = "Python"
replacement = "Java"

# Find the starting index of the target substring manually
i = 0
while i <= len(input_string) - len(target):
    match = True
    for j in range(len(target)):
        if input_string[i + j] != target[j]:
            match = False
            break
    if match:
        break
    i += 1

# Construct new string manually
if match:
    # Part before the match + replacement + part after the match
    new_string = ""
    for k in range(i):
        new_string += input_string[k]
    new_string += replacement
    for k in range(i + len(target), len(input_string)):
        new_string += input_string[k]
else:
    new_string = input_string  # No match found

# Output
print("Output:", new_string)
