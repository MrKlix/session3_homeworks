# print welcome to user
print("Welcome to the great Calculator Program!!")
print("="*50)
print("="*50)
print("\n")


    # read user input for operation
    # read user input for first value
    # read user input for second value
    # calculate
    # print result
    # User can continue using the calculator


zahl1 = None
zahl2 = None
operator = None

while True:
        operator = input("Welche Rechenart möchten Sie nutzen? ('+'-'/'*') ").strip()
        if operator in ["+","-","/","*"]:
            try:
                zahl1 = int(input("Wie lautet die erste Zahl? ").strip())
                zahl2 = int(input("Wie lautet die zweite Zahl? ").strip())
            except Exception as error:
                print("\n")
                print("Bitte Prüfen Sie Ihre Eingabe. Es muss eine Zahl eingegeben werden!")
                continue

            if operator == "-":
                ergebnis = zahl1 - zahl2
                print("\n")
                print("Das Ergebnis ist " + str(ergebnis))
                print("=" * 50)
                print("=" * 50)
                print("\n")
                decision = str(input("Möchten Sie es erneut versuchen? (Type: yes / no : ").strip())
                if decision == "yes":
                    continue
                else:
                    break

            elif operator == "+":
                ergebnis = zahl1 + zahl2
                print("\n")
                print("Das Ergebnis ist " + str(ergebnis))
                print("=" * 50)
                print("=" * 50)
                decision = str(input("Möchten Sie es erneut versuchen? (Type: yes / no : ").strip())
                if decision == "yes":
                    continue
                else:
                    break

            elif operator == "/":
                ergebnis = zahl1 / zahl2
                print("\n")
                print("Das Ergebnis ist " + str(ergebnis))
                print("=" * 50)
                print("=" * 50)
                decision = str(input("Möchten Sie es erneut versuchen? (Type: yes / no : ").strip())
                if decision == "yes":
                    continue
                else:
                    break

            elif operator == "*":
                ergebnis = zahl1 * zahl2
                print("\n")
                print("Das Ergebnis ist " + str(ergebnis))
                print("=" * 50)
                print("=" * 50)

                decision = str(input("Möchten Sie es erneut versuchen? (Type: yes / no : ").strip())
                if decision == "yes":
                    continue
                else:
                    break



