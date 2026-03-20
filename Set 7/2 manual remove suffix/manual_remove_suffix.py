text = input("Enter text: ")
suffix = input("Enter suffix to remove: ")
start_check = len(text) - len(suffix)
if text[start_check:] == suffix:
    result = text[:start_check]
    print(result)
else:
    print(text)
