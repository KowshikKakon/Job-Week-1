msg = next(gen)          
print(msg)               

msg2 = gen.send("Hi!")  
print(msg2)   