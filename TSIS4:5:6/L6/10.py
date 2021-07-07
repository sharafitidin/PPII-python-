def f(a):
    for i in a:
        if i%2 == 0:
            print(i, end = " ")
a = list(map(int, input().split()))
f(a)