'''Write code Check if the given string is Palindrome or not '''

string = input("Enter a string :")
reverse = string[::-1]

if string == reverse :
    print("Palindrome")
else:
    print("Not a Pallindrome")
