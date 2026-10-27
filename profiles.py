from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from datetime import datetime

ENTRY_FEE = 10.00
MANDATORY_DRINKS = 15.00
GAMBLE_TAX = 5.00
TOTAL_STARTING_COST = ENTRY_FEE + MANDATORY_DRINKS + GAMBLE_TAX
current_year = 2026
LEGAL_AGE = 18

players = {}
current_player = None

def initialize_player():
    global current_player
    name = get_name()

    if name in players:
        current_player = players[name]
        budget = current_player["saldo"]
        print(f"Welkom terug {name}. Je saldo is {budget}")

        return

    birth_date, age = get_birthdate()
    if not check_age(age):
        print("Je moet minimaal 18 zijn om het casino in te mogen.")
        exit(1)

    gender = get_gender()
    salutation = determine_salutation(gender)

    budget, starting_budget = calculate_budget()
    if budget <= 0:
        print("Je hebt niet genoeg budget, tot een volgende keer.")
        exit(1)

    players[name] = create_profile(name, birth_date, gender, budget)
    current_player = players[name]

    return budget, name, salutation, starting_budget, gender, birth_date, age

def create_profile(name, birth_date, gender, budget):
    return {
        "naam": name,
        "geboortedatum": birth_date,
        "gender": gender,
        "saldo": budget,
        "gespeelde_spellen": {}
    }

def get_name():
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

    return name

def get_gender():
    gender = input("Wat is je geslacht? Kies M/V/X ").upper()
    while gender != "M" and gender != "V" and gender != "X":
        gender = input("Ongeldige invoer. Wat is je geslacht? Kies M/V/X ").upper()

    return gender

def get_birthdate():
    ask_birth_date = input("Wat is je geboortedatum? Gebruik dd-mm-yyyy ")
    age = calculate_age(birth_date)

    return ask_birth_date, age

def calculate_age(ask_birth_date):
    birth_date = datetime.strptime(ask_birth_date, "%d-%m-%Y")
    today = datetime.now()

    age = today.year - birth_date.year
    has_had_birthday_yet = (today.month, today.day) < (birth_date.month, birth_date.day)
    if has_had_birthday_yet:
        age -= 1

    return age

def check_age(age):
    if age >= LEGAL_AGE:
        return True

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

def calculate_budget():
    starting_budget = float(input("Wat is je budget voor vandaag? "))
    budget = starting_budget - TOTAL_STARTING_COST
    return budget, starting_budget

def show_welcome_message(budget: float | int, name: str, salutation: str | None, starting_budget: float):
    print(Panel.fit(f"""Welkom {salutation} {name}.

Startbudget:    €{starting_budget:.2f}
Vaste Kosten:   €{TOTAL_STARTING_COST:.2f}
Budget:         €{budget:.2f}""",
title="Casino de Gouden Driehoek",
subtitle="Veel geluk!"))


def get_current_balance():
    return current_player["saldo"]

def update_current_balance(balance):
    global current_player
    current_player["saldo"] = balance

def get_current_gamesplayed():
    return current_player["gespeelde_spellen"]

def update_current_gamesplayed(game):
    global current_player

    if game not in current_player["gespeelde_spellen"]:
        current_player["gespeelde_spellen"][game] = 1
    else:
        current_player["gespeelde_spellen"][game] += 1

def show_all_accounts():
    print("Dit zijn alle accounts:")
    table = Table()
    table.add_column("Naam")
    table.add_column("Saldo", justify="right")

    for name, profile in players.items():
        table.add_row(name, f"€{profile['saldo']:.2f}")

    console = Console()
    console.print(table)

    # return Panel(
    #     table,
    #     title="Alle Accounts")

def create_new_account():
    print("We gaan een nieuw account aanmaken.")
    initialize_player()

def change_account():
    show_all_accounts()
    name = input("Naar welk account wil je wisselen? ")
    while name not in players:
        name = input("Ongeldige invoer, voer de naam volledi in. ")
    if name in players:
        current_player = players[name]
        budget = current_player["saldo"]
        print(f"Welkom terug {name}. Je saldo is {budget}")

def delete_account():
    print("Dit zijn alle accounts:")
    show_all_accounts()
    name = input("Welk account wil je verwijderen? ")
    while name not in players:
        name = input("Ongeldige invoer, voer de naam juist in. ")
    if name in players:
        bevestig = input(f"Weet je zeker dat je {name} wilt verwijderen? Ja/nee" ).capitalize()
        while bevestig not in  ("Ja", "Nee"):
            bevestig = input(f"Kies ja of nee ").capitalize()
        if bevestig == "Ja":
            del players[name]
            print(f"{name} is verwijderd.")
        else:
            print("Er is geen profiel verwijderd")
            return

def show_account_menu():
    table = Table()
    table.add_column("Keuze", width=5)
    table.add_column("Actie", justify="center", width=30)
    table.add_row("1", "Toon alle accounts")
    table.add_row("2", "Nieuw account")
    table.add_row("3", "Wissel account")
    table.add_row("4", "Verwijder account")
    table.add_row("0", "Terug")

    print(Panel.fit(
          f"Huidige speler: {current_player['naam']}\n"
          f"Saldo: {current_player['saldo']}\n"
          f"Gespeelde spellen: {current_player['gespeelde_spellen']}\n"
          f"Beschikbare spelers: {list(players.keys())}",
    title="Casino de Gouden Driehoek - Account opties"))
    console = Console()
    console.print(table)

    account_options_choice = input("Kies een optie: Kies uit 0 t/m 4 ")
    while account_options_choice not in ("0", "1", "2", "3", "4"):
        account_options_choice = input("Ongeldige invoer. Kies 0 t/m 4. ")
    if account_options_choice == "1":
        show_all_accounts()
        show_account_menu()
    elif account_options_choice == "2":
        create_new_account()
        show_account_menu()
    elif account_options_choice == "3":
        change_account()
        show_account_menu()
    elif account_options_choice == "4":
        delete_account()
        show_account_menu()
    elif account_options_choice == "0":
        return

