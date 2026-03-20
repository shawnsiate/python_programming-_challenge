ares = []
while True:
    entry = input("Enter a number: ")
    if not entry.replace('.', '', 1).isdigit():
        break
    num = float(entry)
    if num in ares:
        print("Duplicate")
    else:
        print("Unique")
        ares.append(num)
