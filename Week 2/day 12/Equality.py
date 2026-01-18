class User:
    def __init__(self, user_id):
        self.user_id = user_id
# Except doing __eq__ method here will a erroor to compare User1==User2
    def __eq__(self, other):
        
        return self.user_id == other.user_id


User1 = User(101)
User2 = User(101
             )
if(User1==User2):
    print("User1 and User2 are the same")       
else:
    print("User1 and User2 are different")