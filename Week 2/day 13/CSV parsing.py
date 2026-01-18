import csv
my_data=[]
my_col={"name":"kowshik","age":21,"roll":11}
with open("./my_csv.csv","w+",encoding="utf-8") as f:
    csv.DictWriter(f,fieldnames=my_col.keys())
    writer = csv.DictWriter(f, fieldnames=my_col.keys())
    writer.writeheader()
    writer.writerow(my_col)
    f.seek(0)
    reader=csv.DictReader(f)
    my_data = list(reader)
print(my_data)

    