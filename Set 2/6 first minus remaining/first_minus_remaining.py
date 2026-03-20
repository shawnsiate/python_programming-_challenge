result = int(input("Enter number 1: "))
for i in range(9):
    result -= float(input(f"Enter number {i+2}: "))
print(result)
