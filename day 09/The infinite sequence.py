def counntFibo(n):
    
    a = 0
    b = 1
    next = b  
    count = 1

    while count <= n:

        print(a, end=" ")
        count += 1
        a, b = b, next
        next = a + b
    

first=list(counntFibo(10))
print(first)

# If we give such a condition that the while loop will always be true then it will never stop and memory will be full/overflow...