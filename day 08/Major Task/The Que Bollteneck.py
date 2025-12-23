from collections import deque

dq = deque([10, 20, 30,1,2,2,3,4,5,6,7,8,9])
dq.pop()
print(dq)


# dq.pop(0) is not possible, instead of we can use dq.popleft() 
