def calculate_area(radious:float)->float:
    if radious<0:
        return 0
    return 3.14*(radious**2)
r=5
print(calculate_area(r))