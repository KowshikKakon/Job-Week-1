num=[1,222,3,4,5,66,7,2,3,4,4,4]
num2=[]

for i in num:
    if i not in num2:
        num2.append(i)
print(num2)


