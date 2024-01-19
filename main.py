def Calculator(first, second, Symbols):
    if Symbols == '+':
        temp = first + second

    elif Symbols == '-':
        temp = first - second

    elif Symbols == '*':
        temp = first * second

    elif Symbols == '/':
        temp = first / second

    elif Symbols == '%':
        temp = first % second

    elif Symbols == '**':
        temp = first ** second

    elif Symbols == '//':
        temp = first // second

    else:
        print("Enter a valid Operator and Values !")

    return f"{first} {Symbols} {second} = {temp}"


print("Select Arithmetic Operators: ")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. reminder (%)")
print("6. Exponent (**)")
print("7. Floor Division (//)")


choose = input("Enter choice (+, -, *, /, %, **, //): ")
sym = choose
a = int(input("Enter the first Values: "))
b = int(input("Enter the second Values: "))
print(Calculator(a, b, sym))
