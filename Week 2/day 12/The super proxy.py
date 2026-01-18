class user():
    def __init__(self,name):
        self.name=name
        print(f"User {self.name} has been created.")

class Admin(user):
    def __init__(self,name,level):
        super().__init__(name)
        self.level=level
        print(f"Admin level {self.level} assigned to user {self.name}.")

admin1=Admin("Alice",5)