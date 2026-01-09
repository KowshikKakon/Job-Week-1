def num_sum():
    total = 0
    count = 0
    average = None
    while True:
        num = yield average   # pause, yield current average, and receive new number
        if num is None:       # optional stop signal
            break
        total += num
        count += 1
        average = total / count

    

gen = num_sum()
print(next(gen))      # Start generator, average is None

print(gen.send(10))   # 10 / 1 = 10.0
print(gen.send(20))   # (10+20)/2 = 15.0
print(gen.send(30))   # (10+20+30)/3 = 20.0
print(gen.send(40))   # (10+20+30+40)/4 = 25.0