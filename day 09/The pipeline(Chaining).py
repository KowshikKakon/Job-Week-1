def myfun(number):
   num=  [i*i for i  in range(number)]
   return num
def second(num):
   even_num= list(filter(lambda x: x % 2 == 0,num))
   return even_num
print(second(myfun(10)))