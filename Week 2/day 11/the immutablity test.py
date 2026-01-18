data = (1, 2, 3)
def modify_tuple(t):
    return (99,) + t[0:]

result = list(map(modify_tuple, [data]))
print("Original tuple:", data)
print("New tuple:", result[0])
# we can modify tuple by the help of list...
