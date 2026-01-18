class User:
    def __init__(self,name):

        #Initialize the Car with default attributes
        self.name =name 
        self.is_active=True

# Creating an instance using the default constructor
car = User("Kowshik")
print(f"User Name: {car.name}, Active Status: {car.is_active}")