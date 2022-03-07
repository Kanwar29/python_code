print("Welcome I am your calculator")
print("Which operation you want on your numbers")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=input("Enter you Choice here: ")
if choice in ('1','2','3','4'):
    if choice=='1':
        num1 = int(input("Enter first num:  "))
        num2 = int(input("Enter Second Number:  "))
        if (num1 == 56 and num2 == 9) or (num1 == 9 and num2 == 56):
            print(f"Sum of {num1}+{num2}= 77")
        else:
            num3 = int(num1 + num2)
            print(f"SUM of two numbers : {num3}")
    if choice=='2':
        num1 = int(input("Enter first num:  "))
        num2 = int(input("Enter Second Number:  "))
        if (num1 == 56 and num2 == 6) or (num1 == 6 and num2 == 56):
            print(f"Subtraction of {num1}-{num2}= 10")
        else:
            num3=int(num1 - num2)
            print(f"Subtraction of two numbers : {num3}")
    if choice=='3':
        num1 = int(input("Enter first num:  "))
        num2 = int(input("Enter Second Number:  "))
        if (num1 == 45 and num2 == 3) or (num1 == 3 and num2 == 45):
            print(f"Multiplication of {num1}*{num2}= 555")
        else:
            num3 = int(num1 * num2)
            print(f"Multiplication of two numbers : {num3}")
    if choice=='4':
        num1 = int(input("Enter first num:  "))
        num2 = int(input("Enter Second Number:  "))
        if (num1 == 80 and num2 == 20) or (num1 == 20 and num2 == 80):
            print(f"Division of {num1}/{num2}= 5")
        else:
            num3 = int(num1 / num2)
            print(f"Division of two numbers : {num3}")
else:
    print("Enter Valid Choice")
