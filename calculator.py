def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    print("Simple Calculator")

    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value for the first number.")
        return

    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value for the second number.")
        return
    
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Enter the operation (1/2/3/4): ")

    if operation == '1':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Invalid operation choice! Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    calculator()
