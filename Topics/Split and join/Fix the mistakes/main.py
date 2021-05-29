text = input()
words = text.split()

for word in words:
    # finish the code here
    website_prefixes = ("https://", "http://", "www.")
    if word.lower().startswith(website_prefixes):
        print(word)
