#Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1*n2

#Divide
def divide(n1, n2):
    if n2==0:
        return "Error cannot divide by 0"
    else:
        return n1/n2
    
operations = {
    "+": add, 
    "-": substract, 
    "*": multiply, 
    "/": divide
    }

def calculator():
    num1 = float(input("Enter first number: "))


    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick operation from above: ")
    num2 = float(input("Enter second number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    cont = input(f"Type 'y' to continue claulating with {answer}, or type 'n' to exit: ")
    if cont == "n":
        calculator()

    while cont == "y":
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick operation from above: ")
        num1 = answer
        num2 = float(input("Enter next new number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        cont = input(f"Type 'y' to continue claulating with {answer}, or type 'n' to exit: ")
        if cont == "n":
            calculator()
        else:
            continue

calculator()