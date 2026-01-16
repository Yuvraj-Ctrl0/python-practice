# 2. Palindrome string
a=input("Enter a string:")
rev=a[::-1]
if(a==rev):
    print(f"{a} is a palindrome.")
else:
    print(f"{a} is not a palindrome.")