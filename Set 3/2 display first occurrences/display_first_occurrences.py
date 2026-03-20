num = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
first = []
for n in num:
    if n not in first:
        first.append(n)
print("First entries only:", first)
