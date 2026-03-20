text = input("Enter text: ")
result = ""
for char in text:
    if ord(char) >= 65 and ord(char) <= 90:
        result = result + chr(ord(char) + 32)
    else:
        result = result + char
print(result)
