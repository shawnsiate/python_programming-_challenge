num = []
while True:
    entry = input("Enter a number: ")
    if not entry.replace('.', '', 1).isdigit():
        break
    num.append(float(entry))

if num:
    print("Lowest number:", min(num))
