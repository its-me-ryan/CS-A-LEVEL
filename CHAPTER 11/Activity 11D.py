Num1 = int(input("Please input a Number : "))
Num2 = int(input("Please input another Number : "))
Operator = str(input("Please input an operator : "))

if Operator == "+" : 
    print(Num1 + Num2)
elif  Operator == "/":
     print(Num1 / Num2)
elif  Operator == "*" : 
      print(Num1 * Num2)
elif Operator == "-" : 
      print(Num1 - Num2)
else :
     print("Invalid Operator")