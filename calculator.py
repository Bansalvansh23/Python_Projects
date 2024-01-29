num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operation (+,*,-,/,%): ")

if (operator == "+"):
    print("The sum is: ",(num1 + num2))
elif (operator == "-"):
    print("The Subtract is: ",(num1 - num2))
elif (operator == "*"):
    print("The multiplication is: ",(num1 *num2))
elif (operator == "/"):
    if(num2 == 0):
        print("The answer is Zerooo")
    else:
        print("The division is: ",float((num1 /num2)))
elif (operator == "%"):
    print("The remainder is: ",(num1 % num2))
else:
    print("Invalid Operator!!!")
    