mycode = 'print("hello world")'
f = """
def prod(x,y,z):
    return x * y * z

print(prod(1,2,3))
"""
exec(mycode)
exec(f)