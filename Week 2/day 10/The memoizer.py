
def cache(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)

            return cache[n]
        elif n in cache:
            
            return n
    
    return wrapper


@cache
def num(n):
    return n

print(num(5))