
def large_sequence(n):
 x=[i for i in range(n)]
 yield from x

    

gen = large_sequence(6)
for i in gen:
    print(i, end=" ")

for i in gen:
    print("second generator",i, end=" ")


# In sense of generator the loop initiate once so just 0 or first value is only printed ...
# If we want to see all values then we have to use extend...