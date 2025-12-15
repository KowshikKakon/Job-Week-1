input_value1 = input("Enter a number1: ")
input_value2 = input("Enter another number2: ")
input_value1=round(float(input_value1),1)
input_value2=round(float(input_value2),1)
result=input_value1+input_value2
result=round(result,1)
if input_value1+input_value2==result:
    print("True")
else:
    print("False")



   