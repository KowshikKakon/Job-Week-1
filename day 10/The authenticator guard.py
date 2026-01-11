user="admin"
def my_func(func):
    def wrapper():
        if user != "admin":
            raise PermissionError("User is not authorized to access this function.")
        else :
            print("Access granted.")
            return func()
    return wrapper

@my_func
def sensitive_operation():
    return 
sensitive_operation()


