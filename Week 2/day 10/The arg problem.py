import time
from functools import wraps

def timing_decorator(func):
        
   

        def wrapper(*args, **kwargs):

            start_time = time.perf_counter()  
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f" {execution_time:.4f} seconds to execute.")
            return result
        return wrapper

@timing_decorator
def heavy_computation(duration):
    
    time.sleep(duration)
    

# Example Usage
heavy_computation(1)
