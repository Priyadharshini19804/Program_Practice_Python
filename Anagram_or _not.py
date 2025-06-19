'''Write code to Check if two strings are Anagram or not 
Two strings are called anagrams if they contain the same characters in the same frequencies, but 
possibly in different orders. 
This code checks whether two given strings are anagrams of each other. 
Example: Are “listen” and “silent” anagrams? 
Sort both: 
“listen” → “eilnst” 
“silent” → “eilnst” 
Both are the same, so “listen” and “silent” are anagrams.'''


Logic 1:

s1 = input()
s2 = input()
str1 = s1.lower()
str2 = s2.lower()
if sorted(s1) == sorted(s2):
    print("Yes")
else:
    print("No")

Logic 2:

str1 = "Race"
str2 = "Care"

# convert both the strings into lowercase
str1 = str1.lower()
str2 = str2.lower()

# Check if the length is the same
if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # if sorted char arrays are the same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")

else:
    print(str1 + " and " + str2 + " are not anagram.")
