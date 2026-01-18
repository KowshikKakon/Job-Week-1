while True:
        

    try:
        num1=float(input("Enter first number:"))
        if(num1<0):

            raise ValueError("No negatives")
        
        print("The number is",num1)
        break
    except ValueError as e:
        print(e)