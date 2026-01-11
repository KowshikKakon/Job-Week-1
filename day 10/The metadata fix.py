from functools import wraps
def myy_func(func):
    @wraps(func)
    def copy_metadata(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return copy_metadata
@myy_func
def example():
    """This is an example function."""
    pass

print(example.__name__)
print(example.__doc__)