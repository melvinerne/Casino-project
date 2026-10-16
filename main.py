from games.roulette import play_roulette
from games.fruitmachine import play_fruitmachine

ENTRY_FEE = 10.00
MANDATORY_DRINKS = 15.00
GAMBLE_TAX = 5.00
current_year = 2026
LEGAL_AGE = 18

def main():
    print("Welkom bij Casino de Gouden Driehoek, voor we beginnen wil ik graag wat van je weten.")

    first_name = input("Wat is je voornaam? ").capitalize()
    second_name = input("Wat is je achternaam? ").capitalize()
    middle_name = input("Heb je nog tussenvoegsels? Ja of nee: ").lower()

    while middle_name != "ja" and middle_name != "nee":
        middle_name = input("Ongeldige invoer. Vul ja of nee in: ").lower()

    if middle_name == "ja":
        middle_name = input("Wat is je tussenvoegsel? ").lower()

        while not middle_name:
            middle_name = input("Je invoer mag niet leeg zijn, wat is je tussenvoegsel?").lower()

        name = f"{first_name} {middle_name} {second_name}"
    else:
        name = f"{first_name} {second_name}"

    gender = input("Wat is je geslacht? Kies M/V/X ").upper()
    while gender != "M" and gender != "V" and gender != "X":
        gender = input("Ongeldige invoer. Wat is je geslacht? Kies M/V/X ").upper()

    if not check_age(calculate_age()):
        print("Je moet minimaal 18 zijn om het casino in te mogen.")
        exit(1)

    budget, starting_budget, starting_cost = calculate_budget()

    if budget <= 0:
        print("Je hebt niet genoeg budget, tot een volgende keer.")
        exit(1)

    print(f"""Casino de Gouden Driehoek
{'-' * 35}
{determine_salutation(gender, name)}

Startbudget:    €{starting_budget:.2f}
Vaste Kosten:   €{starting_cost:.2f}
Budget:         €{budget:.2f}

Je hebt genoeg budget voor een avondje casino, veel geluk!\n""")

    show_main_menu(budget, starting_budget)


def calculate_age():
    birth_date = input("Wat is je geboortedatum? Gebruik dd-mm-yyyy ")
    birth_day, birth_month, birth_year = birth_date.split("-")
    birth_year = int(birth_year)
    age = current_year - birth_year
    return age

def check_age(age):
    if age >= LEGAL_AGE:
        return age >= 18


def calculate_budget():
    starting_budget = float(input("Wat is je budget voor vandaag? "))
    starting_cost = ENTRY_FEE + MANDATORY_DRINKS + GAMBLE_TAX
    budget = starting_budget - starting_cost
    return budget, starting_budget, starting_cost


def determine_salutation(gender, name):
    if gender == "M":
        return f"Welkom Dhr. {name}"
    elif gender == "V":
        return f"Welkom Mevr. {name}"
    elif gender == "X":
        return f"Welkom {name}"


# def show_welcome_message(startbudget, balance, salutation):


def show_main_menu(budget, starting_budget):
    while True:
        print(f"""Casino de Gouden Driehoek - hoofdmenu
{"-"*35}
1. Spellen
2. Check saldo
3. Account
0. Stop""")
        main_menu_choice = input("Kies een optie: ")
        while main_menu_choice not in ("0", "1", "2", "3"):
            main_menu_choice = input("Ongeldige invoer. Kies 0 t/m 3. ")
        if main_menu_choice == "0":
                print(f"Bedankt voor het spelen vandaag. Je bent begonnen met {starting_budget:.2f} en gaat naar huis met {budget:.2f}.")
                break
        elif main_menu_choice == "1":
            spellen_menu(budget, starting_budget)
        elif main_menu_choice == "2":
            print(f"Je saldo is {budget:.2f}")
        elif main_menu_choice == "3":
            account_menu()


def account_menu():
    print(f"""Casino de Gouden Driehoek - account
{"-" * 35}
1. Naam
2. Aanspreekvorm
3. Geboortedatum
4. Leeftijd
0. Terug""")
    account_menu_choice = input("Kies een optie: Kies uit 0 t/m 4")
    while account_menu_choice not in ("0", "1", "2", "3", "4"):
        account_menu_choice = input("Ongeldige invoer. Kies 0 t/m 4. ")
    if account_menu_choice == "0":
        return

def spellen_menu(budget, starting_budget):
    print(f"""Casino de Gouden Driehoek - spellen
{"-" * 35}
1. Fruitmachine
2. Roulette
0. Terug""")
    spellen_menu_choice = input("Kies een optie: Kies uit 0 t/m 2.  ")
    while spellen_menu_choice not in ("0", "1", "2"):
        spellen_menu_choice = input("Ongeldige invoer. Kies 0 t/m 2. ")
    if spellen_menu_choice == "0":
        show_main_menu(budget, starting_budget)
    elif spellen_menu_choice == "1":
        play_fruitmachine(budget, starting_budget)
    elif spellen_menu_choice == "2":
        play_roulette(budget, starting_budget)




main()

