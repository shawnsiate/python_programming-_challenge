numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
duplicates = set([n for n in numbers if numbers.count(n) > 1])
print("Numbers that have duplicates:", list(duplicates))
