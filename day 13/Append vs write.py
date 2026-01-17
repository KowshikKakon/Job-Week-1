
try:
    with open('./my_text.txt','a') as f:
        f.write('This is a log line...')
except FileNotFoundError:
    print("File not found...")
