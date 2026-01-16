# 4. Factorial of a number.
n=int(input("Enter a number: "))
product=1
for i in range(1,n+1):
    product*=i
print(f"{product} is the factorial of {n}.")