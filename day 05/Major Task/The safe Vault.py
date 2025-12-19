user={"id":1}
try:

    print(user["Email"])
except Exception as  e:
    print(f"some problem:{e}")

correctWay=user.get("Email","Email is not present...")
print(correctWay)