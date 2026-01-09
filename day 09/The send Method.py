def echo():
    received = yield "Hey I am from inside..."
    print(f"hi outside:{received}")
    yield received


gen = echo()

msg = next(gen)          
print(msg)               

msg2 = gen.send("Hi mjj!")  
print(msg2)             
      


