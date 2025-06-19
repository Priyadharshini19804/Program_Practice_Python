'''Find non-repeating characters in a string 
This problem asks to find the characters in a string that appear only once, i.e., the non-repeating 
characters. 
These characters are unique and do not appear multiple times in the string. 
Example for string “swiss”: 
Non-repeating characters are „w‟ and „i‟, since „s‟ repeats. '''


String = input("Enter a string: ")
for i in String:
    count = 0
    for j in String:
        if i == j:
            count+=1
        if count > 1:
            break
    if count == 1:
        print(i,end = " ")
