# the calculator  
a=int(input("Enter the first number: "))
b=input("Enter the required operation: ")
c=int(input("Enter the second number: "))

if b=="+":
    print(f"The addition of {a} + {c} is: {a + c}")
elif b=="-":
    print(f"The subtraction of {a} - {c} is: {a - c}")
elif b=="*":
    print(f"The multiplication of {a} * {c} is: {a * c}")
elif b=="/":
    print(f"The division of {a} / {c} is: {a / c}")
elif b=="**":
    print(f"The exponentiation of {a} ** {c} is: {a ** c}")
else:
    print("Invalid operation")