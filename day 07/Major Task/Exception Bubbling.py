while True:
    try:
        val=int(input("Enter number:"))
        print(100/val)
        break
    except ValueError:
        print("The etext is not allowed.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")