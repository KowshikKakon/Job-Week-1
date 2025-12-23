dict = [
    {'Course': "C++", 'Author': "Jerry"},
    {'Course': "Python", 'Author': "Mark"},
    {'Course': "Java", 'Author': "Paul"}
]

res = [sub for sub in dict if sub['Course'] == "Java"]
res = res[0] 
print(res)