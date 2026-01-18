try:
    with open('./my_text.txt','w+') as f:
        f.write("This is a new line.I am wrinting.My name is kowshik...")
        f.seek(0)
        print(f.read())
except FileNotFoundError:
    print("File not found...")
