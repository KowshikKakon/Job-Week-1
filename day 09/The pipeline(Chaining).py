def myfun(number):
   num=  [i*i for i  in range(number)]


   even_num= list(filter(lambda x: x % 2 == 0,num))
   return even_num
print(myfun(10))