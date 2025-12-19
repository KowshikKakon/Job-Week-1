
import time
num1=list(range(0,1000000))

num2=set(range(0,1000000))
# For list...
startTime1=time.perf_counter()



if -1 in num1:
    print("-1 fount in the list...")
else:
    print("Not Found in the list...")
    
endTime1=time.perf_counter()
ex1=endTime1-startTime1
print(f"List Take in seconds:{ex1:.8f}")
# for set...

startTime2=time.perf_counter()


  


if -1 in num2:
    print("-1 fount in the set...")
else:
    print("Not Found in the set...")
    
endTime2=time.perf_counter()
exi2=endTime2-startTime2
print(f"Set Take in seconds:{exi2:.8f}")