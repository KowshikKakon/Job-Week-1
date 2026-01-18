class mmyClasss():
    def __init__(self,name):
        self.__password = 5500
        self.name=name

        # self.password is private variable...

obj = mmyClasss("Alice")

print("First attempt for name:", obj.name)
print("First attempt for password:", obj.__password)

# self.__password=4000 is not possible because we can't access private variable directly from outside the class.
# but name will change because it is public variable...