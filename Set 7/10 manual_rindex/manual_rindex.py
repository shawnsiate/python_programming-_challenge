text = input("Enter text: ")
target = input("Search for: ")
location = -1

for i in range(len(text) - 1, -1, -1):
    if text[i] == target:
        location = i
        break

if location != -1:
    print("Found at index:", location)
else:
    print("Not found")
