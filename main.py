from idlelib.format import get_indent
from operator import truediv

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
