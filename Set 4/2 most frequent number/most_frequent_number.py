num = []
while True:
    entry = input("Enter a number: ")
    try:
        num.append(float(entry))
    except ValueError:
        break

if num:
    most_frequent = max(set(num), key=num.count)
    print("Number with the most duplicates:", most_frequent)
