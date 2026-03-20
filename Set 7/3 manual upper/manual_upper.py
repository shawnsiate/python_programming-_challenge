text = input("Enter text: ")
result = ""
for char in text:
    if 97 <= ord(char) <= 122:
        result = result + chr(ord(char) - 32)
    else:
        result = result + char
print(result)
