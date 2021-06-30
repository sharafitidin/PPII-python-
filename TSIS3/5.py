a = input().split()
k = int(input())
if k < 0:
    k = abs(k)
    print(*a[k:], end = " ")
    print(*a[0:k], end = " ")
else:
    k = abs(k)
    print(*a[-k:], end = " ")
    print(*a[0:-k], end = " ")