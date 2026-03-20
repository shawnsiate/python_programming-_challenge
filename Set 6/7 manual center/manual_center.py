text = input("Enter text: ")
width = int(input("Enter total width: "))

spaces_to_add = width - len(text)
if spaces_to_add > 0:
    left_spaces = spaces_to_add // 2
    right_spaces = spaces_to_add - left_spaces
    result = (" " * left_spaces) + text + (" " * right_spaces)
    print("'" + result + "'")
else:
    print(text)
