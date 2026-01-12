import time

num = 1000000
start_time = time.time()
squares = [i * i for i in range(num)]
end_time = time.time()
print("Time taken by list comprehension:", end_time - start_time)

start_time1= time.time()
squares1=list(map(lambda x:x*x,range(num)))
end_time1 = time.time()
print("Time taken by map:", end_time1 - start_time1)