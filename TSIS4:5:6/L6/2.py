def summa(a):
    sum = 0
    for i in a:
        sum += i
    return sum
a = list(map(int, input().split()))
print(summa(a))