text = input("Enter text: ")
result = ""
found_char = False

for char in text:
    if char != " " or found_char == True:
        result = result + char
        found_char = True
print(result)
