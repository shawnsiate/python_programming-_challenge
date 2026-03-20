text = input("Enter text: ")
pref = input("Enter prefix to remove: ")

if text[0:len(pref)] == pref:
    result = text[len(pref):]
    print(result)
else:
    print(text)
