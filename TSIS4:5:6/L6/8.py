def f(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b
a = list(map(int, input().split()))
print(f(a))