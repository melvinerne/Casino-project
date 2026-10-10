from idlelib.format import get_indent
from operator import truediv
from os import WCONTINUED

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


birth_date = input("Wat is je geboortedatum? Gebruik dd-mm-yyyy ")


birth_day, birth_month, birth_year = birth_date.split("-")
birth_day = int(birth_day)
birth_month = int(birth_month)
birth_year = int(birth_year)
current_year = 2026
LEGAL_AGE = 18

if current_year - birth_year < LEGAL_AGE:
    print("Je moet minimaal 18 zijn om het casino in te mogen.")
    exit(1)


gender = input("Wat is je geslacht? Kies M/V/X ").upper()
while gender != "M" and gender != "V" and gender != "X":
    gender = input("Ongeldige invoer. Wat is je geslacht? Kies M/V/X ").upper()
if gender == "M":
    gender = "meneer"
elif gender == "V":
    gender = "mevrouw"
elif gender == "X":
    gender = "persoon"

starting_budget = float(input("Wat is je budget voor vandaag?"))
ENTRY_FEE = 10.00
MANDATORY_DRINKS = 15.00
GAMBLE_TAX = 5.00
starting_cost = (ENTRY_FEE + MANDATORY_DRINKS + GAMBLE_TAX)
budget = (starting_budget - starting_cost)

can_enter = False
enter_message = ""
if budget > 0:
    can_enter = True
    enter_message = "Je hebt genoeg budget voor een avondje casino, veel geluk!"
else:
    enter_message = "Je hebt niet genoeg budget, tot een volgende keer."

welcome_message = f"""Casino de Gouden Driehoek
{'-' * 35}
Welkom {gender} {name}.

Startbudget:    €{starting_budget:.2f}
Vaste Kosten:   €{starting_cost:.2f}
Budget:         €{budget:.2f}

{enter_message}"""

print(welcome_message)
print("\nLaten we roulette spelen!\n")


# round_number = 1
import random

continue_playing = True
while continue_playing == True:
    print("Je kan kiezen uit de volgende opties:\n1: rood\n2: zwart\n3: even\n4: oneven\n0: stop")

    choice = input("Kies waar je op wilt inzetten. Kies uit 0 t/m 4. ")
    if choice == "0":
        print("Tot de volgende keer.")
        break
    while choice not in ("0", "1", "2", "3", "4"):
        choice = input("Ongeldige invoer. Kies 0 t/m 4. ")


    bet_amount = float(input("Hoeveel wil je inzetten? "))

    while bet_amount <= 0 or bet_amount > budget:
        bet_amount = float(input("Je moet minimaal 1 inzetten. En niet hoger dan je budget. Hoeveel wil je inzetten? "))

    budget = budget - bet_amount
    print(f"Je hebt {bet_amount:.2f} ingezet. Je resterend budget is {budget:.2f}")


    # spin = (round_number * 7) % 37
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

    print(f"Je hebt {spin} {color} gegooid.")
    if choice == "1" and color == "rood":
        budget = budget + (bet_amount * 2)
        print(f"Je wint {bet_amount * 2:.2f}. Je budget is nu {budget:.2f}")
    elif choice == "2" and color == "zwart":
        budget = budget + (bet_amount * 2)
        print(f"Je wint {bet_amount * 2:.2f}. Je budget is nu {budget:.2f}")
    elif choice == "3" and odd_even == "even":
        budget = budget + (bet_amount * 2)
        print(f"Je wint {bet_amount * 2:.2f}. Je budget is nu {budget:.2f}")
    elif choice == "4" and odd_even == "odd":
        budget = budget + (bet_amount * 2)
        print(f"Je wint {bet_amount * 2:.2f}. Je budget is nu {budget:.2f}")
    else:
        print(f"Helaas je verliest deze keer. Je resterend budget is nu {budget:.2f}")
    keep_on_playing = input("Wil je doorspelen? Kies ja of nee. ")
    if keep_on_playing == "ja":
        # round_number += 1
        continue
    else:
        continue_playing = False
        print(f"Bedankt voor het spelen vandaag. Je bent begonnen met {starting_budget:.2f} en gaat naar huis met {budget:.2f}.")
        break

