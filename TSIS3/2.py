a = input().split() 
mini = 1e9
for i in a:
    if int(i) > 0 and int(i) < mini:
        mini = int(i) 
print(mini)