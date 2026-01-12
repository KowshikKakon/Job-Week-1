mylist = [1,2,3,4,4,-5,-8,5,5,-1,0,9,8,7]
x = any(mylist1<0 for mylist1 in mylist)
if(x==True):
    print("There is at least one negative number in the list")
else:
    print("There is no negative number in the list")

x = all(mylist2>0 for mylist2 in mylist)
if(x==True):
    print("All numbers in the list are positive")
else:
    print("Not all numbers in the list are positive")