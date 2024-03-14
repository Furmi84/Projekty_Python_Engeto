print('Sčítání:    "+",')
print('Odčitání:   "-",')
print("-" * 20)
while True:
    operation = input("Vyber si operaci:")
    if operation in ("+", "-"):
        print("operace", operation)
        number_1 = int(input("Zadej prvni cislo: "))
        number_2 = int(input("Zadej druhe cislo cislo: "))
        if operation in ("+"):
            print(f" {number_1} {operation}{number_2} = {number_1+number_2}")
        elif operation in ("-"):
            print(f" {number_1} {operation} {number_2} = {number_1 - number_2}")
        print("Chcete provést další operaci?('a' pro ano, jakákoliv jiná klávesa pro ne):")
        if str(input()) == "a":
            continue
        else:
            print("Konec programu")
            break

    else:
        print("Nezadali jste platný operátor, zkuste to znovu")
        continue
