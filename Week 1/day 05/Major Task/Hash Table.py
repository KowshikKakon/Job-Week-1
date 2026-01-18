user={"id":1,"name":"Admin"}
email=user.get("email","No Email Found")
for key,val in user.items():
    print(f"{key} : {val}")