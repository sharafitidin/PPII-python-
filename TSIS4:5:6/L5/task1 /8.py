f = open("text1.txt", "r")
words = f.read().split()
max_size = len(max(words, key = len))
for word in words:
    if len(word) == max_size:
        print(word)