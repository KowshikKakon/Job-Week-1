while True:
    pwd=input("set password(5 min chars):")

    
    if len(pwd)>=5:

        print("Password Set")
        break
    print("Too short. Try again.")