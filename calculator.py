def calculator():
       # global a,b
       a = int(input("Enter first number: "))
       b = int(input("Enter first number: "))
       oper = (input("Enter operator: "))

       if oper == "+" :
           sum = a + b
           print(f"Sum of two numbers is : {sum}")
       elif oper == "-" :
           diff = a - b
           print(f"Difference of two numbers is: {diff}")
       elif oper == "*":
           product = a * b
           print(f"Product of two numbers is: {product}")
       elif oper == "/":
           division = a/b
           print(f"Division of two numbers is: {division}")
       else:
           print("Sorry! Invalid Choice")

       r =  input("Do you want to continue using calculator?")
       if r == "Yes":
            calculator()
       else:
            print("See you!")
calculator()






S



