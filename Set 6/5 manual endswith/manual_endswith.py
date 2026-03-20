text = input("Enter text: ")
suffix = input("Enter suffix to check: ")

start_index = len(text) - len(suffix)
if text[start_index:] == suffix:
    print(True)
else:
    print(False)
