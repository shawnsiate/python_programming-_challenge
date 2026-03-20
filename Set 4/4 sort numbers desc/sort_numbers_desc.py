num = []
while True:
    entry = input("Enter a number: ")
    try:
        num.append(float(entry))
    except ValueError:
        break

num.sort(reverse=True)
print("Sorted (Highest to Lowest):", num)
