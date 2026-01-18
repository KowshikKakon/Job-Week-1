class User():
    def delete(self):
        return "User Class"
    
class Admin(User):
    def delete1(self):
        return "Admin Class"
    
a = Admin()
print(a.delete())
        