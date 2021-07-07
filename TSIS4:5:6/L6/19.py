def test(a):
        def add(b):
                nonlocal a
                a += 1
                return a+b
        return add 
func = test(5)
print(func(5))