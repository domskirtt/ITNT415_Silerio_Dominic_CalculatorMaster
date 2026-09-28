def add(a, b):
    return round(a + b, 4)


def subtract(a, b):
    return round(a - b, 4)


def multiply(a, b):
    return round(a * b, 4)


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return round(a / b, 4)


OPERATIONS = {
    "+": ("Addition", add),
    "-": ("Subtraction", subtract),
    "*": ("Multiplication", multiply),
    "/": ("Division", divide),
}


def show_banner():
    print("\n" + "=" * 40)
    print("   SILERIO CALCULATOR  |  ITNT415")
    print("=" * 40)
    print("   [ + ] Add        [ - ] Subtract")
    print("   [ * ] Multiply   [ / ] Divide")
    print("   [ q ] Quit")
    print("-" * 40)


def read_number(label):
    while True:
        try:
            return float(input(f"   {label}: "))
        except ValueError:
            print("   That's not a number. Try again.")


def main():
    while True:
        show_banner()
        symbol = input("   Pick an operator > ").strip().lower()

        if symbol == "q":
            print("\n   Thanks for calculating. Goodbye!\n")
            break

        if symbol not in OPERATIONS:
            print("   Unknown operator. Use + - * / or q.")
            continue

        name, func = OPERATIONS[symbol]
        print(f"\n   Mode: {name}")
        a = read_number("First number ")
        b = read_number("Second number")

        answer = func(a, b)
        if isinstance(answer, str):
            print(f"\n   {answer}")
        else:
            print(f"\n   {a} {symbol} {b} = {answer}")


if __name__ == "__main__":
    main()
