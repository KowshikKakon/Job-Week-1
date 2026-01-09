def my_gen():
    yield 1
    yield 2
    yield 3
g=my_gen()

try:

    while True:
        print(next(g))
except StopIteration:
    print("Generator is exhausted.")