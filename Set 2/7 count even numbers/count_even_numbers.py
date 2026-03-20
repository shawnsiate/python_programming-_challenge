even_numbers = 0
for i in range(10):
    if float(input(f"Enter number {i+1}: ")) % 2 == 0:
        even_numbers += 1
print(even_numbers)
