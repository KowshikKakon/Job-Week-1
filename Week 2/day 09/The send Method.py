def echo():
    while True:
        received = yield
        print(f"hi inside:{received}")
   


gen = echo()

next(gen)          
# print(msg)               

gen.send("Hi mjj!")  
gen.send("second attempt")             
      


