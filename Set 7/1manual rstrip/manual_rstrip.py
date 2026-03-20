text = input("Enter text: ")
last_index = -1
for i in range(len(text) - 1, -1, -1):
    if text[i] != " ":
        last_index = i
        break

if last_index == -1:
    print("")
else:
    print(text[:last_index + 1])
