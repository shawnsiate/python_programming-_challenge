numbers = []
while True:
    entry = input("Enter a number: ")
    if not entry.replace('.', '', 1).isdigit():
        break
    numbers.append(float(entry))

numbers.sort()
print("Sorted numbers:", numbers)
