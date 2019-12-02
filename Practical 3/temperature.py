def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = get_fahr(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = get_cels(fahrenheit)
            #one of the number should be float
            print("Result: {:.2f} C". format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_cels(fahrenheit):
    celsius = 5 / 9.0 * (fahrenheit - 32)
    return celsius


def get_fahr(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()