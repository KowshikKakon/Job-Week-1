def even_numbers(n):
    for i in range(0, n+1,2):
        yield i

def odd_numbers(n):
    for i in range(1, n+1,2):
        yield i

def combined_numbers(n):
    yield from even_numbers(n)
    yield from odd_numbers(n)



for num in combined_numbers(10):
    print(num)
