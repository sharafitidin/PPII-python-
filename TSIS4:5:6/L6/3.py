def prod(a):
    prod = 1
    for i in a:
        prod *= i
    return prod
a = list(map(int, input().split()))
print(prod(a))