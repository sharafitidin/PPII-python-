def f(s):
    s = s.replace(" ", "")
    s_1 = s[::-1]
    if s == s_1:
        return True
    else:
        return False
s = input()
print(f(s))