#Shravan Surve

num1=int(input("Enter num 1:"))
num2=int(input("Enter num 2:"))
choice=input("Enter your choice (+,-,*,/,//,**,%):")

if(choice=="+"):
    print("Addition :",num1+num2)
elif(choice=="-"):
    print("Subtraction :",num1-num2)
elif(choice=="*"):
    print("Multiplication :",num1*num2)
elif(choice=="/"):
    print("Division :",num1/num2)
elif(choice=="//"):
    print("Floor Division :",num1//num2)
elif(choice=="**"):
    print("Exponent :",num1**num2)
elif(choice=="%"):
    print("Mod :",num1%num2)
else:
    print("Invalid choice")


