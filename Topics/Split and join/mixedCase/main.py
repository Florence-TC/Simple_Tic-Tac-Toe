text = input().split()
camel_text = [text[0]]
for word in text[1:]:
    word = word.title()
    camel_text.append(word)
print("".join(camel_text))
