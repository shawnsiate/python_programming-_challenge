text = input("Enter text: ")
words = text.split()
new_words = []
for w in words:
    first = w[0]
    if 97 <= ord(first) <= 122:
        first = chr(ord(first) - 32)
    rest = ""
    for i in range(1, len(w)):
        char = w[i]
        if 65 <= ord(char) <= 90:
            rest = rest + chr(ord(char) + 32)
        else:
            rest = rest + char
    new_words.append(first + rest)
print(" ".join(new_words))
