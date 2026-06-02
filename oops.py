vowels="aeiou"
letter=input("enter your name")
count=0
for i in letter:
    if i.lower() in vowels:
        count=count+1
print(count)   