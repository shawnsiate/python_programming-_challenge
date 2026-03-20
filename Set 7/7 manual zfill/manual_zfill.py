text = input("Enter text: ")
length = int(input("Enter total length: "))

while len(text) < length:
    text = "0" + text
print(text)
