num = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
unique = [n for n in num if num.count(n) == 1]
print("Numbers without duplicates:", unique)
