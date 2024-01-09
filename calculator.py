num1=int(input("Enter the first operand : "))
num2=int(input("Enter the second operand : "))
print("Enter the operation which you have to perform: \n")
operator=int(input("1: Addition \t 2: Subtraction \t 3: Multiplication \t 4: Division \n"))
if(operator==1):
    sum=num1+num2
    print("Addition of ", num1 , " and ", num2 ," is = ", sum)
elif(operator==2):
    diff=num1-num2
    print("Subtraction of ", num1 , " and ", num2 ," is = ", diff)
elif(operator==3):
    mul=num1*num2
    print("Multiplication of ", num1 , " and ", num2 ," is = ", mul)
elif(operator==4):
    div=num1//num2
    print("Division of ", num1 , " and ", num2 ," is = ", div)
else:
    print("You have entered the wrong choice of the operator")
