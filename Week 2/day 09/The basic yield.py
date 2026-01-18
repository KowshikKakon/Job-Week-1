def gen ():
    yield 1
    yield 2
    yield 3
g=gen()
for value in g:
    print(value)