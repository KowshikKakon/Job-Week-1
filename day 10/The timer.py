
import time


def changecase(func):
  def myinner(*args, **kwargs):
    start=time.time()
    result= func(*args, **kwargs).upper()
    end=time.time()
    print(f"Time taken: {end - start} seconds")
    return result
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("Johnijuuihh8hujuh8hhjuihh"))