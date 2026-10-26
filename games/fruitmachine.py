from rich import print
import random
from helperfuncties import bet_placement

def play_fruitmachine(budget):
    print("\nLaten we de fruitmachine spelen!\n")
    continue_playing = True
    while continue_playing == True:

        fruitmachine_enter_message(budget)

        bet_amount, budget = bet_placement(budget)

        budget = fruitmachine(bet_amount, budget)

        keep_on_playing = input("Wil je doorspelen? Kies ja of nee. ")
        if keep_on_playing == "ja":
            continue
        elif keep_on_playing == "nee":
            return budget


def fruitmachine_enter_message(budget):
    print(f"Huidig saldo: {budget}.")


def fruitmachine(bet_amount, budget):
    fruitslots = ["kers", "citroen", "aardbei"]
    roll1 = random.choice(fruitslots)
    roll2 = random.choice(fruitslots)
    roll3 = random.choice(fruitslots)
    uitslag = [roll1, roll2, roll3]
    print(f"\nDe uitslag is: {roll1} | {roll2} | {roll3}\n")

    for uitkomst in uitslag:
        if uitslag.count(uitkomst) == 3:
            budget = budget + (bet_amount * 3)
            print(f"3 op een rij! Je wint {bet_amount * 3:.2f}. Je budget is nu {budget:.2f}")
            break
        elif uitslag.count(uitkomst) == 2:
            budget = budget + (bet_amount * 1)
            print(f"2 op een rij! Je krijg je inzet terug en wint {bet_amount * 1:.2f}. Je budget is nu {budget:.2f}")
            break
    else:
        print(f"Helaas, geen match. Je verliest je inzet. Je budget is nu {budget}")

    return budget