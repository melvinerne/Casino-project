from os import name

from games.roulette import play_roulette
from games.fruitmachine import play_fruitmachine
from games.blackjack import play_blackjack
from profiles import initialize_player, show_welcome_message, get_current_balance, update_current_balance, update_current_gamesplayed, get_current_gamesplayed, show_all_accounts, create_new_account, change_account, delete_account, show_account_menu



def main():
    print("Welkom bij Casino de Gouden Driehoek, voor we beginnen wil ik graag wat van je weten.")

    budget, name, salutation, starting_budget, gender, birth_date, age = initialize_player()

    show_welcome_message(budget, name, salutation, starting_budget)

    show_main_menu(budget, starting_budget, name, gender, birth_date, age)


def show_main_menu(budget, starting_budget, name, gender, birth_date, age):
    while True:
        print(f"Casino de Gouden Driehoek - hoofdmenu\n"
              f"{"-"*35}\n"
              f"1. Spellen\n"
              f"2. Check saldo\n"
              f"3. Account\n"
              f"0. Stop\n")
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

    print(f"Casino de Gouden Driehoek - spellen\n"
          f"{"-" * 35}\n"
          f"1. Fruitmachine\n"
          f"2. Roulette\n"
          f"3. Blackjack\n"
          f"0. Terug\n")
    spellen_menu_choice = input("Kies een optie: Kies uit 0 t/m 3.  ")
    while spellen_menu_choice not in ("0", "1", "2", "3"):
        spellen_menu_choice = input("Ongeldige invoer. Kies 0 t/m 3. ")
    if spellen_menu_choice == "0":
        show_main_menu(budget, starting_budget)
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
        print(f"Casino de Gouden Driehoek - account\n"
              f"{"-" * 35}\n"
              f"1. Naam\n"
              f"2. Aanspreekvorm\n"
              f"3. Geboortedatum\n"
              f"4. Leeftijd\n"
              f"5. Gespeelde spellen\n"
              f"6. Account opties\n"
              f"0. Terug\n")
        account_menu_choice = input("Kies een optie: Kies uit 0 t/m 6 ")
        while account_menu_choice not in ("0", "1", "2", "3", "4", "5", "6"):
            account_menu_choice = input("Ongeldige invoer. Kies 0 t/m 6. ")
        if account_menu_choice == "1":
            print(f"Jouw naam is: {name} \n")
        elif account_menu_choice == "2":
            print(f"Jouw gewenste aanspreekvorm is: {gender.capitalize()}\n")
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
