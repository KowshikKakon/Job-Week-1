import random
num= [random.randrange(-10, 990990) for _ in range(1000000)]
num=set(num)
# print(num)
if -5 in num:
    print("Yes -5 is there...")
else:
    print("No -5 is not there...")