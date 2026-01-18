myinp=input("Give me the string banana:")
myinp=str(myinp)
print(myinp)
valuea=0
valueb=0
valuen=0
for i in myinp:
    if i=="a":
        valuea+=1
    elif i=="b":
        valueb+=1
    elif i=="n":
        valuen+=1
mydic={"b":valueb,"a":valuea,"n":valuen}
print(mydic)

