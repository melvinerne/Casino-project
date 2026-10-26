from rich import print
from rich.table import Table
from rich.console import Console
from games.roulette import play_roulette
from games.fruitmachine import play_fruitmachine
from games.blackjack import play_blackjack
from profiles import initialize_player, show_welcome_message, get_current_balance, update_current_balance, update_current_gamesplayed, get_current_gamesplayed, show_account_menu, determine_salutation



def main():
    print("Welkom bij Casino de Gouden Driehoek, voor we beginnen wil ik graag wat van je weten.")

    budget, name, salutation, starting_budget, gender, birth_date, age = initialize_player()

    show_welcome_message(budget, name, salutation, starting_budget)

    show_main_menu(budget, starting_budget, name, gender, birth_date, age)


def show_main_menu(budget, starting_budget, name, gender, birth_date, age):
    while True:
        table = Table(title=f"\nCasino de Gouden Driehoek - Hoofdmenu")
        table.add_column("Keuze", width=5)
        table.add_column("Actie", justify="center", width=30)
        table.add_row("1", "Spellen")
        table.add_row("2", "Check Saldo")
        table.add_row("3", "Account")
        table.add_row("0", "Stop")

        console = Console()
        console.print(table)

        main_menu_choice = input("Kies een optie: ")
        while main_menu_choice not in ("0", "1", "2", "3"):
            main_menu_choice = input("Ongeldige invoer. Kies 0 t/m 3. ")

        if main_menu_choice == "0":
                print(f"Bedankt voor het spelen vandaag. Je bent begonnen met {starting_budget:.2f} en gaat naar huis met {budget:.2f}.")
                break
        elif main_menu_choice == "1":
            budget = spellen_menu(starting_budget)
        elif main_menu_choice == "2":
            print(f"Je saldo is €{get_current_balance():.2f}")
        elif main_menu_choice == "3":
            account_menu(name, gender, birth_date, age)

def spellen_menu(starting_budget):
    budget = get_current_balance()

    table = Table(title=f"\nCasino de Gouden Driehoek - Spellen")
    table.add_column("Keuze", width=5)
    table.add_column("Actie", justify="center", width=30)
    table.add_row("1", "Fruitmachine")
    table.add_row("2", "Roulette")
    table.add_row("3", "Blackjack")
    table.add_row("0", "Terug")

    console = Console()
    console.print(table)

    spellen_menu_choice = input("Kies een optie: Kies uit 0 t/m 3.  ")
    while spellen_menu_choice not in ("0", "1", "2", "3"):
        spellen_menu_choice = input("Ongeldige invoer. Kies 0 t/m 3. ")
    if spellen_menu_choice == "0":
        return
    elif spellen_menu_choice == "1":
        budget = play_fruitmachine(budget)
        update_current_balance(budget)
        update_current_gamesplayed("fruitmachine")
    elif spellen_menu_choice == "2":
        budget = play_roulette(budget)
        update_current_balance(budget)
        update_current_gamesplayed("roulette")
    elif spellen_menu_choice == "3":
        budget = play_blackjack(budget)
        update_current_balance(budget)
        update_current_gamesplayed("blackjack")
    return budget

def account_menu(name, gender, birth_date, age):
    while True:
        table = Table(title=f"\nCasino de Gouden Driehoek - Account menu")
        table.add_column("Keuze", width=5)
        table.add_column("Actie", justify="center", width=30)
        table.add_row("1", "Naam")
        table.add_row("2", "Gewenste aanspreekvorm")
        table.add_row("3", "Geboortedatum")
        table.add_row("4", "Leeftijd")
        table.add_row("5", "Gespeelde spellen")
        table.add_row("6", "Account opties")
        table.add_row("0", "Terug")
        console = Console()
        console.print(table)

        account_menu_choice = input("Kies een optie: Kies uit 0 t/m 6 ")
        while account_menu_choice not in ("0", "1", "2", "3", "4", "5", "6"):
            account_menu_choice = input("Ongeldige invoer. Kies 0 t/m 6. ")
        if account_menu_choice == "1":
            print(f"Jouw naam is: {name} \n")
        elif account_menu_choice == "2":
            print(f"Jouw gewenste aanspreekvorm is: {determine_salutation(gender)}\n")
        elif account_menu_choice == "3":
            print(f"Jouw geboortedatum is: {birth_date}\n")
        elif account_menu_choice == "4":
            print(f"Jouw leeftijd is: {age}\n")
        elif account_menu_choice == "5":
            print(get_current_gamesplayed())
        elif account_menu_choice == "6":
            show_account_menu()
        elif account_menu_choice == "0":
            return

main()
