val=["100px", "20px", "3px"]
val.sort(key=lambda x: int(x[:-2]))
print(val)

