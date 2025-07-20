# cook your dish here
string = input().split()
for i in string:
    reverse = string[::-1]
    result = " ".join(reverse)
print(result)