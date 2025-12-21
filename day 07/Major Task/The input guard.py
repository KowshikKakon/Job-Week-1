while True:
    try:
        val =int(input("enter age:"))
        print(f"Age is:{val}")
        break
    except ValueError:
        print("Please enter age in number not as text...")
        