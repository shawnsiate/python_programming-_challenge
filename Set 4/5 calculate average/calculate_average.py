num = []
while True:
    entry = input("Enter a number: ")
    try:
        num.append(float(entry))
    except ValueError:
        break

if num:
    print("Average:", sum(num) / len(num))
