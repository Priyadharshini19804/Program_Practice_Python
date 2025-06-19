'''
Reverse Words in a String 
Example: 
Input: "Hello world this is a string" 
Output: "string a is this world Hello".
'''

sentence = input("Enter a sentence: ")
words = []
word = ""
i = 0
length = 0
for ch in sentence:
    length += 1
while i < length:
    ch = sentence[i]
    if ch != ' ':
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""
    i += 1
if word != "":
    words.append(word)
i = len(words) - 1
print("Reversed sentence:")
while i >= 0:
    print(words[i], end=" ")
    i -= 1
