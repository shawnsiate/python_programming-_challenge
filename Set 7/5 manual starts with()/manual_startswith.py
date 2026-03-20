text = input("Enter text: ")
prefix = input("Enter prefix: ")

if text[:len(prefix)] == prefix:
    print(True)
else:
    print(False)
