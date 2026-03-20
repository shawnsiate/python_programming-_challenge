name = input("Enter your name: ")
words = name.split()
pascal_name = ""
for w in words:
    pascal_name = pascal_name + w.capitalize()
print(pascal_name)
