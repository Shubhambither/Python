# a=int(input("Enter first operand :"))
# op=input("Enter operator : ")
# b=int(input("Enter second operand :"))

# if(op=="+"):
#     print(a+b)
# elif(op=="-"):
#     print(a-b)
# elif(op=="*"):
#     print(a*b)
# elif(op=="/"):
#     print(a/b)
# elif(op=="%"):
#     print(a%b)
# else:
#     print(f"Choose a valid operator. You choosed {op}. Choose from = - * / %")
# print(a,op,b)
# -------------------------------------------------------------------------------
# a = input("Enter first operand: ")
# op = input("Enter operator: ")
# b = input("Enter second operand: ")

# print(eval(a + op + b)) 
#eval works on input taken as string not as input
# -------------------------------------------------------------------------------
expression = input("Enter expression: ")

print(eval(expression))

    