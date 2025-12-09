# Simple Calculator with History

class Calculator:
    def __init__(self):
        self.history = []  # Store calculation results as text

    def calculate(self, a, b, op):
        result = None

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                print("Error: Division by zero!")
                return None
            result = a / b
        else:
            print("Invalid operator!")
            return None

        record = f"{a} {op} {b} = {result}"
        self.history.append(record)
        return result

    def get_history(self):
        return self.history


def main():
        calc = Calculator()

        while True:
            print("\n=== Calculator Menu ===")
            print("1. New Calculation")
            print("2. Show History")
            print("0. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                try:
                    a = float(input("Enter first number: "))
                    op = input("Enter operator (+, -, *, /): ")
                    b = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid input!")
                    continue

                result = calc.calculate(a, b, op)
                if result is not None:
                    print("Result:", result)

            elif choice == '2':
                hist = calc.get_history()
                if not hist:
                    print("No history yet.")
                else:
                    print("\n--- Calculation History ---")
                    for record in hist:
                        print(record)

            elif choice == '0':
                print("Exiting Calculator. Goodbye!")
                break

            else:
                print("Invalid choice!")


if __name__ == "__main__":
    main()
