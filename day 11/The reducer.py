from functools import reduce
li = [1,2,3,5]
res = reduce(lambda x, y: x* y, li)
print(res)