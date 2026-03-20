text = input("Enter text: ")
is_all_lower = True

for char in text:

    if 65 <= ord(char) <= 90:
        is_all_lower = False
        break

print(is_all_lower)
