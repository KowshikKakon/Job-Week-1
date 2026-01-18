raw_val=input("enter Principal:")
try:
    principal=float(raw_val)
    print(f"Accepted:${principal:,.2f}")
except ValueError:
    print("Error:Invalid Number")