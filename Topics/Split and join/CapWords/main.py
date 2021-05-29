names = input().split("_")
names = [word.lower().title() for word in names]
print("".join(names))
