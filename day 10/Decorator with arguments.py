def repeat(times):
    def wraper(func):
        def wrap(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrap
    return wraper
    

@repeat(3)
def greet(name):
    print(name)

greet("Alice")