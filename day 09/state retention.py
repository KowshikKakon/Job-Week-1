def num_sum():
    total = 0
    count = 0
    average = 0
    while True:
        val = yield average   
        
        total += val
        count += 1
        average = total / count

    

gen = num_sum()
print(next(gen))      
print(gen.send(10))   
print(gen.send(20))   
print(gen.send(30))   
print(gen.send(40))   