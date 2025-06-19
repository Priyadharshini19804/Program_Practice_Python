'''

Write a Program to Convert Digits to Words. 
Example: 
 Input: 123 
 Process: 
o 1 → “One” 
o 2 → “Two” 
o 3 → “Three” 
 Output: Digits 123 in words are: One Two Three

'''
# Create a dictionary to map digits to words
digit_to_word = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

# Input from user
number = input("Enter a number: ")

# Loop through each character in input and convert to word
for digit in number:
    if digit in digit_to_word:
        print(digit_to_word[digit], end=' ')
    else:
        print("Invalid character:", digit)
