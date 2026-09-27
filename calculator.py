def add(a, b):
    return round(a + b, 4)


def subtract(a, b):
    return round(a - b, 4)


def multiply(a, b):
    return round(a * b, 4)

def divide(a, b):
    pass

def get_numbers():
    while True:
        try:
            a = float(input("Enter first number:  "))
            b = float(input("Enter second number:  "))
            return a,  b
         except ValueError:
             print("Invalid input. Please enter numeric values.")


def main():
    while True:
        print("\n--- Calculator Master ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break
        elif choice in ("1", "2", "3", "4"):
            a, b = get_numbers()
            if choice =="1":
                print(f"Result: {add(a, b)}")
            elif choice == "2":
                print(f"Result: {subtract(a, b)}")
            elif choice == "3":
                print(f"Result: {multiply(a, b)}")
            elif choice == "4":
                print(f"Result: {divide(a, b)}")

          else:
              print("Invalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()
