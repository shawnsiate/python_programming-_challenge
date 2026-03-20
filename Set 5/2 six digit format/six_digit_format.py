number = input("Enter a number (0-1000): ")
while len(number) < 6:
    number = "0" + number
print(number)
