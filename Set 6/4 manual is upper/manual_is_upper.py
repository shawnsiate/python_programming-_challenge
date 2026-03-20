text = input("Enter text: ")
all_upper = True

for char in text:
    if ord(char) < 97 or ord(char) > 122:
        continue
    all_upper = False

print(all_upper)
