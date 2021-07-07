from collections import *
def word_count(name):
    with open(name) as f:
        return Counter(f.read().split())
        

print(word_count("text1.txt"))