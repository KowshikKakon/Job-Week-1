try:
    with open('./my_text.txt','w+',encoding='utf-8') as f:
        f.write("Write next...")
        f.seek(0)
        print(f.read())
except FileNotFoundError:
    print("File not found...")