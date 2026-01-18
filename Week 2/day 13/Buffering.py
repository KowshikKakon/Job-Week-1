try:
    with open('./myfile.txt','w+',buffering=1) as f:
        for i in range(1000000):
            f.write(str(i)+'\n')
        f.seek(0)
        print(f.read())
except FileNotFoundError:
    print("File not found...")