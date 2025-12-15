
total=input("Enter a number:")
total=int(total)
hours=total//3600
remaining_seconds=total%3600
minutes=remaining_seconds//60
seconds=remaining_seconds%60
print(f"hours:{hours} , minutes:{minutes} , seconds:{seconds}")