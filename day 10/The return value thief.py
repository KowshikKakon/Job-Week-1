

def timing_decorator(func):
        
   

        def wrapper():

              
            func()
            
            
        return wrapper

@timing_decorator
def heavy_computation():
      return 10
    
    

# Example Usage
print(heavy_computation())
