from collections import Counter
num1=[1,2,3,4,5,7,8,9]
num2=[64,576,68,5,44,4,4,5]
actual=[]
for i in num1:
    for j in num2:
        if (i==j):
           actual.append(i)

print("The duplicate number:",set(actual))