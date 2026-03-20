text = input("Enter text: ")
sub = input("Enter character to count: ")
counter = 0

for char in text:
    if char == sub:
        counter = counter + 1
print(counter)
