from collections import Counter
def ana(a,b):
    return Counter(a)==Counter(b)

print(ana("silent","listen"))