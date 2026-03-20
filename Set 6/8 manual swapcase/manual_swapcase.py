text = input("Enter text: ")
result = ""
for char in text:
    if 65 <= ord(char) <= 90:
        result = result + chr(ord(char) + 32)
    elif 97 <= ord(char) <= 122:
        result = result + chr(ord(char) - 32)
    else:
        result = result + char
print(result)
