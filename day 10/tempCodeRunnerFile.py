

def timing_decorator(func):
        
   

        def wrapper(*args, **kwargs):

              
            result = func(*args, **kwargs)
            
            print(f" args: {args}, kwargs: {kwargs}")
            return result
        return wrapper

@timing_decorator
def heavy_computation(x,y):
    summation=x + y
    print(summation)
   
    

# Example Usage
heavy_computation(1,2)
