operators = ['+', '-', '*', '/']
user_input = ''

while True:
    print("\nSimple Calculator")
    user_input = input("Type ON to start or OFF to end: ")

    if user_input.lower() == 'off':
        print("Goodbye!")
        break

    elif user_input.lower() == 'on':
        print("Calculator is ON...")
        user_input = input("Enter a calculation (e.g. 3 * 4): ")

        # Remove all spaces
        equation = user_input.replace(" ", "")

        # Check if expression contains a valid operator
        if any(operators in equation for operators in operators):
            allowed_chars = "0123456789." + ''.join(operators)

            if all(char in allowed_chars for char in equation):
                # Check for division by zero
                if '/' in equation:
                    parts = equation.split('/')
                    if len(parts) == 2 and parts[1] == '0':
                        print("Error: Cannot divide by zero.")
                        continue  # Skip this round and restart the loop

                # Evaluation is made sure to be safe
                # Exception is if all of these cases are not true (pairs with the try case)
                try:
                    result = eval(equation)
                    print("Result:", float(result))
                except Exception as error_case:
                    print("Something went wrong. Invalid expression.", error_case)
            else:
                print("Invalid characters detected. Use numbers and + - * / only.")
        else:
            print("No valid operator found. Use one of '+', '-', '*', '/'")

    else:
        print("Calculator is ON...")