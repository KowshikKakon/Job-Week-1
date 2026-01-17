import json
data={
"name":"kowshik",
"age":21,
"roll":11


}
try:
    with open("./my_text.txt",'w+') as f:
        json.dump(data,f)
        f.seek(0)
        print(json.load(f))
except FileNotFoundError:
    print("File not found...")