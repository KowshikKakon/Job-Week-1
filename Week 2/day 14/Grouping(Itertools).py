


from itertools import groupby
data=sorted({'watermelon': 1, 'apple': 2, 'banana': 3})
for k,g in groupby(data): print(k,list(g))

