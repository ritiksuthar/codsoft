print("**********************************SIMPLE CALCULATOR**************************************************")
number1 = float(input("Enter first number:"))
number2 = float(input("Enter second number:"))

while True:
    opration = input("Enter oparation(+,-,*,/) and for EXIT (E or e):")
    if opration == 'E' or opration == 'e':
        break

    elif opration == '+':
        sum = number1 + number2
        print(f"sum of two number {number1} + {number2} = {sum}")

    elif opration == '-':
        diff = number1 - number2
        print(f"diffrent of two number {number1} - {number2} = {diff}") 
            
    elif opration == '*':
        mult = number1 * number2
        print(f"multiplication of two number {number1} * {number2} = {mult}")

    elif opration == '/':
        if number2 != 0:
            div = number1 / number2
            print(f"division  of two number {number1} + {number2} = {div}")

        else:
            print("not divide by 0")
    else:
        print("wrong choice...Try again.!")
    print("\n")

print("****************************************END*******************************************************")
   