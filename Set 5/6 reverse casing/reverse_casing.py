name = input("Enter your name: ")
result = ""
for char in name:
    if char.isupper():
        result = result + char.lower()
    else:
        result = result + char.upper()
print(result)
