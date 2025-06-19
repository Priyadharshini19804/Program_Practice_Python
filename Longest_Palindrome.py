'''
Write a code to check for the longest palindrome in an array. 
This problem asks to find the longest palindrome in an array of strings. A palindrome is a word, 
phrase, or sequence that reads the same backward as forward. 
 The goal is to identify the longest string in the array that is a palindrome. 
 Example for array [“racecar”, “level”, “hello”, “madam”, “world”]: 
The longest palindrome is “racecar”. 
'''

mylist=[]
size=int(input("Enter the number of elements in the list: "))
for i in range(size):
    string = input("Enter a string :")
    mylist.append(string)
#text=string.split()
max_length=0
for word in mylist:
    if len(word)>max_length:
        max_length = len(word)
        #reverse = string[::-1]
for word in mylist:
    if len(word) == max_length:
        reverse = word[::-1]
        print(f"Longest Pallindrome: {word}")
else:
    print(f"There is no longest Pallindrome in the array.")
