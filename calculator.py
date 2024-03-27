def subtract(n1, n2):
    return n1 - n2


def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def caculator():
    should_continue = True
    num1 = float(input("What's is the first number?: "))
    for symbol in operations:
        print(symbol)
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        option = input(f"Type y to continue calculating with {answer} or no to stop or n to start new  ")
        if option == "y":
            num1 = answer
        elif option == "no":
            should_continue = False
        else:
            caculator()


caculator()
