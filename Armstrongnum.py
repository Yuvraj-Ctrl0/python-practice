# 1. Armstrong number 
n=int(input("Enter a number: "))
temp=n
mul=0
pow=len(str(n))
while(temp>1):
    num=int(temp%10)
    mul+=(num**pow)
    temp/=10
if(n==mul):
    print(f"{n} is an armstrong number.")
else:
    print(f"{n} is not armstrong number.")
