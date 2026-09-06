print("===CALCULATOR===")
print("------------------------------------------")

print("Available Operations:")
print("  +  Addition")
print("  -  Subtraction")
print("  *  Multiplication")
print("  /  Division")
print("  ^  Power")

print("------------------------------------------")

try:
    a = float(input("First number: "))
    op = input("Operation (+, -, *, /, ^): ").strip()
    b = float(input("Second number: "))

    if op == "+":
        result = a + b
        operation_name = "Addition"
    
    elif op == "-":
        result = a - b
        operation_name = "Subtraction"
    
    elif op == "*":
        result = a * b
        operation_name = "Multiplication"
    
    elif op == "/":
        if b == 0:
            print("------------------------------------------")
            print("Cannot divide by zero.")
            print("------------------------------------------")
            result = None

        else:
            result = a / b
            operation_name = "Division"

    elif op == "^":
        result = a ** b
        operation_name = "Power"

    else:
        print("------------------------------------------")
        print("Invalid operation. Please use +, -, *, /, or ^.")
        print("------------------------------------------")
        result = None

    if result is not None:
        print("------------------------------------------")
        print(f"{operation_name} Result")
        print("-" * 42)
        print(f"{a:g} {op} {b:g} = {result:g}")
        print("------------------------------------------")

except ValueError:
    print("------------------------------------------")
    print("Please enter valid numbers.")
    print("------------------------------------------")
