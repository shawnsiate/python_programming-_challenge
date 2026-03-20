num_1 = int(input("Enter start number: "))
num_2 = int(input("Enter end number: "))
start, end = min(num_1, num_2), max(num_1, num_2)
for i in range(start + 1, end):
    print(i)
