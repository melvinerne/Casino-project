from tokenize import generate_tokens

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

    birth_date = input("Wat is je geboortedatum? Gebruik dd-mm-yyyy ")
    age = calculate_age(birth_date)

    if not check_age(age):
        print("Je moet minimaal 18 zijn om het casino in te mogen.")
        exit(1)

    budget, starting_budget, starting_cost = calculate_budget()

    if budget <= 0:
        print("Je hebt niet genoeg budget, tot een volgende keer.")
        exit(1)

    salutation = determine_salutation(gender)

    show_welcome_message(budget, name, salutation, starting_budget, starting_cost)

    show_main_menu(budget, starting_budget, name, salutation, birth_date, age)


def show_welcome_message(budget: float | int, name: str, salutation: str | None, starting_budget: float,
                         starting_cost: float | int):
    print(f"""Casino de Gouden Driehoek
{'-' * 35}
Welkom {salutation} {name}.

Startbudget:    €{starting_budget:.2f}
Vaste Kosten:   €{starting_cost:.2f}
Budget:         €{budget:.2f}

Je hebt genoeg budget voor een avondje casino, veel geluk!\n""")


def calculate_age(birth_date):
    birth_day, birth_month, birth_year = birth_date.split("-")
    birth_year = int(birth_year)
    age = current_year - birth_year
    return age

def check_age(age):
    if age >= LEGAL_AGE:
        return True

def calculate_budget():
    starting_budget = float(input("Wat is je budget voor vandaag? "))
    starting_cost = ENTRY_FEE + MANDATORY_DRINKS + GAMBLE_TAX
    budget = starting_budget - starting_cost
    return budget, starting_budget, starting_cost

def determine_salutation(gender):
    if gender == "M":
        gender = "meneer"
        return gender
    elif gender == "V":
        gender = "mevrouw"
        return gender
    elif gender == "X":
        gender = "persoon"
        return gender

def show_main_menu(budget, starting_budget, name, gender, birth_date, age):
    while True:
        print(f"Casino de Gouden Driehoek - hoofdmenu\n{"-"*35}\n1. Spellen\n2. Check saldo\n3. Account\n0. Stop")
        main_menu_choice = input("Kies een optie: ")
        while main_menu_choice not in ("0", "1", "2", "3"):
            main_menu_choice = input("Ongeldige invoer. Kies 0 t/m 3. ")

        if main_menu_choice == "0":
                print(f"Bedankt voor het spelen vandaag. Je bent begonnen met {starting_budget:.2f} en gaat naar huis met {budget:.2f}.")
                break
        elif main_menu_choice == "1":
            budget = spellen_menu(budget, starting_budget)
        elif main_menu_choice == "2":
            print(f"Je saldo is {budget:.2f}")
        elif main_menu_choice == "3":
            account_menu(name, gender, birth_date, age)

def spellen_menu(budget, starting_budget):
    print(f"Casino de Gouden Driehoek - spellen\n{"-" * 35}\n1. Fruitmachine\n2. Roulette\n0. Terug")
    spellen_menu_choice = input("Kies een optie: Kies uit 0 t/m 2.  ")
    while spellen_menu_choice not in ("0", "1", "2"):
        spellen_menu_choice = input("Ongeldige invoer. Kies 0 t/m 2. ")
    if spellen_menu_choice == "0":
        return
    elif spellen_menu_choice == "1":
        budget = play_fruitmachine(budget)
    elif spellen_menu_choice == "2":
        budget = play_roulette(budget)
    return budget

def account_menu(name, gender, birth_date, age):
    while True:
        print(f"Casino de Gouden Driehoek - account\n{"-" * 35}\n1. Naam\n2. Aanspreekvorm\n3. Geboortedatum\n4. Leeftijd\n0. Terug")
        account_menu_choice = input("Kies een optie: Kies uit 0 t/m 4 ")
        while account_menu_choice not in ("0", "1", "2", "3", "4"):
            account_menu_choice = input("Ongeldige invoer. Kies 0 t/m 4. ")
        if account_menu_choice == "1":
            print(f"Jouw naam is: {name} \n")
        elif account_menu_choice == "2":
            print(f"Jouw gewenste aanspreekvorm is: {gender.capitalize()}\n")
        elif account_menu_choice == "3":
            print(f"Jouw geboortedatum is: {birth_date}\n")
        elif account_menu_choice == "4":
            print(f"Jouw leeftijd is: {age}\n")
        elif account_menu_choice == "0":
            return

main()
{enter_message}"""

print(welcome_message)
print("\nLaten we roulette spelen!\n")


continue_playing = True
while continue_playing == True:
    print("Je kan kiezen uit de volgende opties:\n1: rood\n2: zwart\n3: even\n4: oneven\n5: specifiek nummer\n0: stop")

    choice = input("Kies waar je op wilt inzetten. Kies uit 0 t/m 5. ")
    if choice == "0":
        print("Tot de volgende keer.")
        break
    elif choice == "5":
        specific_number_choice = int(input("Kies je nummer. Je kan kiezen uit 0 t/m 36. "))
        while specific_number_choice not in range(0, 36):
            specific_number_choice = int(input("Ongeldige invoer. Je kan kiezen uit 0 t/m 36. "))
    while choice not in ("0", "1", "2", "3", "4", "5"):
        choice = input("Ongeldige invoer. Kies 0 t/m 5. ")


    bet_amount = float(input("Hoeveel wil je inzetten? "))

    while bet_amount <= 0 or bet_amount > budget:
        bet_amount = float(input("Je moet minimaal 1 inzetten. En niet hoger dan je budget. Hoeveel wil je inzetten? "))

    budget = budget - bet_amount
    print(f"Je hebt {bet_amount:.2f} ingezet. Je resterend budget is {budget:.2f}")


    spin = random.randint(0, 36)
    color = ("")
    odd_even = ("")

    if spin % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"


    if spin <= 18 and odd_even == "even":
        color = "zwart"
    elif spin > 18 and odd_even == "even":
        color = "rood"
    elif spin <= 18 and odd_even == "odd":
        color = "rood"
    else:
        color = "zwart"

    if spin == 0:
        print(f"Je hebt {spin} gegooid. Helaas verlies je deze keer. Je resterend budget is nu {budget:.2f}")
    elif choice == "1" and color == "rood":
        budget = budget + (bet_amount * 2)
        print(f"Je hebt {spin} {color} gegooid. Je wint {bet_amount * 2:.2f}. Je budget is nu {budget:.2f}")
    elif choice == "2" and color == "zwart":
        budget = budget + (bet_amount * 2)
        print(f"Je hebt {spin} {color} gegooid. Je wint {bet_amount * 2:.2f}. Je budget is nu {budget:.2f}")
    elif choice == "3" and odd_even == "even":
        budget = budget + (bet_amount * 2)
        print(f"Je hebt {spin} {color} gegooid. Je wint {bet_amount * 2:.2f}. Je budget is nu {budget:.2f}")
    elif choice == "4" and odd_even == "odd":
        budget = budget + (bet_amount * 2)
        print(f"Je hebt {spin} {color} gegooid. Je wint {bet_amount * 2:.2f}. Je budget is nu {budget:.2f}")
    elif choice == "5" and spin == specific_number_choice:
        budget = budget + (bet_amount * 35)
        print(f"Je hebt {spin} {color} gegooid. Je wint {bet_amount * 35:.2f}. Je budget is nu {budget:.2f}")
    else:
        print(f"Je hebt {spin} {color} gegooid. Helaas, je verliest deze keer. Je resterend budget is nu {budget:.2f}")
    keep_on_playing = input("Wil je doorspelen? Kies ja of nee. ")
    if keep_on_playing == "ja":
        continue
    else:
        continue_playing = False
        print(f"Bedankt voor het spelen vandaag. Je bent begonnen met {starting_budget:.2f} en gaat naar huis met {budget:.2f}.")
        break

