nums=[2,7,11,15]
t=9
s={}
for i in nums:
    if (t-i) in s:
        print(i,t-i)
    s[i]=True


    