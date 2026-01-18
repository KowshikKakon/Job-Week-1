list1=[x for x in range(0,1000000)]
print("List size:",list1.__sizeof__())

list2=(x for x in range(0,1000000))
print("Generator size:",list2.__sizeof__())