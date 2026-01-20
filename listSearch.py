# 4. Search element in list.
l=[14,23,645,87,29]
for i in l:
    print(i, end=" ")
print()
key=int(input("Enter a number you want to search in the list: "))
if key in l:
    print(f"{key} found in list.")
else:
    print(f"{key} does not exist in the list.")