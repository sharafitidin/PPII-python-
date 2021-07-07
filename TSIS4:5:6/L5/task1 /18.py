f = open("text3.txt").read()
f.replace(","," ")
print(len(f.split(" ")))