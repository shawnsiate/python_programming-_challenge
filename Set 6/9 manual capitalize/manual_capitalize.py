text = input("Enter text: ")
result = ""

for i in range(len(text)):
    char = text[i]
    if i == 0:

        if 97 <= ord(char) <= 122:
            result = result + chr(ord(char) - 32)
        else:
            result = result + char
    else:

        if 65 <= ord(char) <= 90:
            result = result + chr(ord(char) + 32)
        else:
            result = result + char
print(result)
