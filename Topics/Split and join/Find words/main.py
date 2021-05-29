sentence = input().split()
sentence = [word for word in sentence if word.endswith("s")]
print("_".join(sentence))
