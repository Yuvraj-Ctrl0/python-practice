# 3. Count vowels
a=input("Enter a string: ")
count=0
for ch in a:
    if(ch.lower() in "aeiou"):
        count +=1
print(count)