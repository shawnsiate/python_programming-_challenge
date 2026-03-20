odds = 0
for i in range(10):
    if int(input(f"Enter number {i+1}: ")) % 2 != 0:
        odds += 1
print(odds)
