numbers=[]
def large_sequence(n):
  for i in range(n):

    yield i

gen = large_sequence(6)
numbers.extend(gen)
print(numbers)


# In sense of generator the loop initiate once so just 0 or first value is only printed ...
# If we want to see all values then we have to use extend...