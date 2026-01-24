# 3. Prime number check
n=int(input("Enter a number to check if it is prime or not: "))
prime=True
for i in range(2,n):
    if(n%i==0):
        prime=False
        break
    elif(n%i!=0):
        prime=True
if(prime==False):
    print(f"{n} is not a prime number.")
elif(prime==True):
    print(f"{n} is a prime number.")